import os;
import subprocess;

def run_python_file(working_directory, file_path, args=[]):
    dir_path = "";
    try:
        
        rel_path = os.path.join(working_directory, file_path);
        abs_path = os.path.abspath(rel_path)
        dir_path = os.path.dirname(abs_path);
        
        if working_directory not in abs_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(rel_path):
            return f'Error: File "{file_path}" not found.';
        
        if not file_path[-3:] == ".py":
            return f'Error: "{file_path}" is not a Python file.'

        proc_result = subprocess.run(
            args = ["uv", "run", rel_path, *args], 
            timeout=30, 
            capture_output=True
            );
                    
        if not proc_result.stdout and not proc_result.stderr:
            return "No output produced";

        if proc_result.returncode != 0:
            return f"Process exited with code {proc_result.returncode}";

        
        return f"STDOUT: {proc_result.stdout} \n STDERR: {proc_result.stderr}"

    except Exception as e:
        return f"Error: executing Python file: {e}";