import subprocess
import os


def run_python_file(working_directory, file_path, args=[]):
    file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))
    working_directory_abs = os.path.abspath(working_directory)
    if not file_path_abs.startswith(working_directory_abs):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(file_path_abs):
        return f'Error: File "{file_path}" not found.'
    elif not file_path_abs.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        complete = subprocess.run(
            ["python3", file_path_abs, *args],
            timeout=30,
            capture_output=True,
            text=True,
            cwd=working_directory_abs,
        )
        if complete.stdout is None:
            return "No output produced"
        if not complete.returncode == 0:
            return f"\nSTDOUT:\n{complete.stdout}\nSTDERR:\n{complete.stderr}\n Process exited with code {complete.returncode}"
        return f"\nSTDOUT:\n{complete.stdout}\nSTDERR:\n{complete.stderr}\nStatus Code: {complete.returncode}"

    except Exception as e:
        return f"Error opening file: {e}"
