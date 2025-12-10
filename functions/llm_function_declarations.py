from google.genai import types;

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get content of specified files, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The current directory where script is being executed from.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to file within the current working directory.",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write data to specific files, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The current directory where script is being executed from.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to file within the current working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to be written to specific file.",
            ),
        },
    ),
)


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute specified python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The current directory where script is being executed from.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to file within the current working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="arguments to be passed to the function call.",
            ),
        },
    ),
)