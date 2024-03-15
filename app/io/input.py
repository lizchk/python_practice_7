import pandas

def read_text_from_cmd():
    """
    Function to input text from the console.

    Returns:
        str: Text entered by the user.
    """
    return input("Enter text: ")


def read_file_by_std(path):
    """
    Function to read from a file using Python's built-in capabilities.

    Args:
        path (str): Path to the file.

    Returns:
        str: Contents of the file.
    """
    try:
        with open(path, 'r') as file:
            text = file.readlines()
        return text
    except FileNotFoundError:
        return "Input file not found."


def read_file_by_pandas(path):
    """
    Function to read from a file using the pandas library.

    Args:
        path: Path to the file.

    Returns:
        str: Contents of the file.
    """
    try:
        dataframe = pandas.read_csv(path)
        text = dataframe.to_string(index=False)
        return text
    except FileNotFoundError:
        print("Input data file not found.")
        return None
    except pandas.errors.EmptyDataError:
        print(f'CSV file with path {path} is empty')
        return None


