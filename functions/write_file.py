import os;
#from config import MAX_FILE_CONTENT_LENGTH;

def write_file(working_directory, file_path, content):
    dir_path = "";
    try:
        
        rel_path = os.path.join(working_directory, file_path);
        abs_path = os.path.abspath(rel_path)
        dir_path = os.path.dirname(abs_path);
        
        if working_directory not in abs_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(dir_path):
            os.makedirs(dir_path);
        
#        return f"{file_path} found in {working_directory}";
        # Write code to read file and return results as a string

        with open(abs_path, 'w+') as fp:
        # This reads at most the first 10000 characters
            
            file_content = fp.write(content);
            
            #print(file_content);
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)';
            


    except Exception as e:
        return f"Error: An unknown error occured {e}";