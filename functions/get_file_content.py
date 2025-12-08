import os;
from config import MAX_FILE_CONTENT_LENGTH;

def get_file_content(working_directory, file_path):
    file_content = "";
    try:

        full_path = os.path.join(working_directory, file_path);
        abs_path = os.path.abspath(full_path)
       
        if working_directory not in abs_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
#        return f"{file_path} found in {working_directory}";
        # Write code to read file and return results as a string

        with open(abs_path, 'r') as fp:
        # This reads at most the first 10000 characters
            
            file_content = fp.read();

            if len(file_content) > MAX_FILE_CONTENT_LENGTH:
                file_content = file_content[:MAX_FILE_CONTENT_LENGTH] + f"[...File {abs_path} truncated at 10000 characters]";
            
            #print(file_content);
            return file_content;
            


    except Exception(err):
        return "Error: An unknown error occured";