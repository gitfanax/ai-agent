import os
from .config import MAX_CHARS

def get_file_content(working_directory, file_path):
    file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))
    working_directory_abs = os.path.abspath(working_directory)
    if not file_path_abs.startswith(working_directory_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(file_path_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(file_path_abs, "r") as f:
            file_content = f.read()
            if len(file_content) > 10000:
                file_content = file_content[0:10000] + f'[...File "{file_path}" truncated at 10000 characters]'
            return file_content
    except Exception as e:
        return f"Error opening file: {e}"
