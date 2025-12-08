import os;

def get_file_content(working_directory, file_path):
    
    try:

        full_path = os.path.join(working_directory, file_path);
        abs_path = os.path.abspath(full_path)

        print(f"{abs_path}");
       
        if working_directory not in abs_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        else:
            return f"{file_path} found in {working_directory}";
        
        return f"{file_path} found in {working_directory}";
        # Write code to read file and return results as a string

    except Exception(err):
        return "An unknown error occured";