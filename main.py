import os, argparse;
from google import genai;
from google.genai import types;
from dotenv import load_dotenv;
from prompts import system_prompt;
from functions.llm_function_declarations import schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file;
from call_function import call_function;

def main():

    parser = argparse.ArgumentParser(description="Sentient AI Agent");
    parser.add_argument("prompt", type=str,help="User prompt");
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output");
    args = parser.parse_args();
    AI_prompt = args.prompt;
    print_verbose = args.verbose;
    AI_CONVO_LENGTH = 10;
    counter = 0
    #results_list = [];

    available_functions = types.Tool(
    function_declarations=[schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file],
    )

    messages = [types.Content(role="user", parts=[types.Part(text=AI_prompt)])];
    

    load_dotenv();
    api_key = os.environ.get('GEMINI_API_KEY');
    if api_key is None:
        raise RuntimeError('API key not found in .env file');

    
    client = genai.Client(api_key = api_key);
    
    while(counter <= AI_CONVO_LENGTH):

        try:
            counter += 1;
            response = client.models.generate_content(
                model='gemini-2.5-flash', 
                contents=messages,
                config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
                );
            
            for vars in response.candidates:
                messages.append(vars.content);
                #print(vars.content);

            

            gemini_metadata = response.usage_metadata;
            
            if gemini_metadata is not None and print_verbose:
                print(f"User prompt: {AI_prompt}");
                print(f"Prompt tokens: {gemini_metadata.prompt_token_count}");
                print(f"Response tokens: {gemini_metadata.total_token_count - gemini_metadata.prompt_token_count}")


            if response.function_calls is not None:
                for function_call_part in response.function_calls:
                    #print(f"Calling function: {function_call_part.name}({function_call_part.args})");
                    res_types_content = call_function(function_call_part, print_verbose);
                    if not res_types_content.parts[0].function_response.response:
                        raise Exception("Error: a fatal error has occured");
                    else:
                        messages.append(res_types_content.parts[0]);

                        messages.append(
                            types.Content(
                                role="user",
                                parts=[
                                    types.Part.from_function_response(
                                    name=res_types_content.parts[0].function_response.name,
                                    response=res_types_content.parts[0].function_response.response,
                                    )
                                ],
                            )
                        )

                        if print_verbose:
                            print(f"-> {res_types_content.parts[0].function_response.response}")
            else:
                if "I want to call" not in response.candidates and response.text:
                    print(f"Final Response: {response.text}");
                    break;
                
            
            #print("Hello from agient!")
        except Exception as e:
            print(f"Error: a grave mistake has been committed {e}");

if __name__ == "__main__":
    main()