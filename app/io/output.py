import pandas

def output_text_to_cmd(text):
    """
    Function to output text to the console.

    Args:
        text: The text to be printed.
    """
    print("Output to console:")
    print(text)


def record_to_file(path, data):
    """
    Function to write to a file using Python's built-in capabilities.

    Args:
        data: The text to be written.
        path: Path to the file.
    """
    try:
        with open(path, 'w') as file:
            for row in data:
                file.write(row)
        print("Output written to file:", path)
    except FileNotFoundError:
        return "File not found."
