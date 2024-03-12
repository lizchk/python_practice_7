from app.io.input import read_text_from_cmd, read_file_by_std, read_file_by_pandas
from app.io.output import record_to_file, output_text_to_cmd

path = "data/output.txt"

def main():
    text_from_cmd = read_text_from_cmd()
    file_contents = read_file_by_std("data/input.txt")
    dataframe = read_file_by_pandas("data/input_csv.csv")

    output_text_to_cmd(text_from_cmd)
    output_text_to_cmd(file_contents)
    output_text_to_cmd(dataframe)

    record_to_file(path, text_from_cmd)
    record_to_file(path, file_contents)
    record_to_file(path, dataframe)

if __name__ == "__main__":
    main()
