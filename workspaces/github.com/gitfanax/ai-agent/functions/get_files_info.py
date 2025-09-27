import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    full_path_abs = os.path.abspath(full_path)
    working_directory_abs = os.path.abspath(working_directory)
    if not full_path_abs.startswith(working_directory_abs):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    try:
        final_list = []
        list_of_items = os.listdir(full_path)
        for item in list_of_items:
            working_path = os.path.join(full_path, item)
            item_size = os.path.getsize(working_path)
            item_is_dir = os.path.isdir(working_path)
            final_list.append(f"- {item}: file_size={item_size}, is_dir={item_is_dir}")
        return "\n".join(final_list)
    except Exception as e:
        return f"Error listing files: {e}"
