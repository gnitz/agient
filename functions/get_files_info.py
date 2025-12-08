import os;

def get_files_info(working_directory, directory="."):
    
    try:

        full_path = os.path.join(working_directory, directory);
        abs_path = os.path.abspath(full_path)
       
        if working_directory not in abs_path:
            return f"Error: Cannot list {directory} as it is outside the permitted working directory";

        if not os.path.isdir(abs_path):
            return f'Error: "{directory}" is not a directory';
        
        dir_ls = os.listdir(abs_path);

        result = "";

        for entry in dir_ls:
            file_path = os.path.join(abs_path, entry);
            if os.path.isfile(abs_path+entry):
                result += f"- {entry}: file_size={os.path.getsize(file_path)}, is_dir={os.path.isdir(file_path)}\n";
            else:
                result += f"- {entry}: file_size={os.path.getsize(file_path)}, is_dir={os.path.isdir(file_path)}\n";

        return result;


    except Exception():
        return "An unknown error occured";