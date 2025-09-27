import os


def write_file(working_directory, file_path, content):
    file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))
    working_directory_abs = os.path.abspath(working_directory)
    if not file_path_abs.startswith(working_directory_abs):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        if not os.path.exists(file_path_abs):
            os.makedirs(os.path.dirname(file_path_abs), exist_ok = True)
        with open(file_path_abs, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing file: {e}"
