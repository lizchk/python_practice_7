import pytest
import pandas as pd
from app.io.input import read_file_by_std, read_file_by_pandas

@pytest.fixture
def tmp_text_file(tmp_path):
    file_content = "Line 1\nLine 2\nLine 3"
    file_path = tmp_path / "test_input.txt"
    file_path.write_text(file_content)
    return file_path

@pytest.fixture
def tmp_csv_file(tmp_path):
    data = {'Column1': ["Row1", "Row2", "Row3"], 'Column2': ["Row1", "Row2", "Row3"]}
    df = pd.DataFrame(data)
    csv_path = tmp_path / "test_input.csv"
    df.to_csv(csv_path, index=False)
    return csv_path

def test_read_file_by_std_success(tmp_text_file):
    assert [line.rstrip('\n') for line in read_file_by_std(str(tmp_text_file))] == ["Line 1", "Line 2", "Line 3"]

def test_read_file_by_std_file_not_found(tmp_path):
    non_existent_file = tmp_path / "non_existent_file.txt"
    assert read_file_by_std(str(non_existent_file)) == "Input file not found."

def test_read_file_by_std_empty_file(tmp_path):
    empty_file = tmp_path / "empty_file.txt"
    empty_file.touch()
    assert read_file_by_std(str(empty_file)) == []

def test_read_file_by_pandas_success(tmp_csv_file):
    expected_df = pd.DataFrame({
        'Column1': ["Row1", "Row2", "Row3"],
        'Column2': ["Row1", "Row2", "Row3"]
    })
    result = read_file_by_pandas(str(tmp_csv_file))
    assert result == expected_df.to_string(index=False)

def test_read_file_by_pandas_file_not_found(tmp_path):
    non_existent_csv = tmp_path / "non_existent_file.csv"
    assert read_file_by_pandas(str(non_existent_csv)) is None

def test_read_file_by_pandas_empty_file(tmp_path):
    empty_csv = tmp_path / "empty_file.csv"
    empty_csv.touch()
    assert read_file_by_pandas(str(empty_csv)) is None
