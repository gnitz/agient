import os, argparse;
from google import genai;
from google.genai import types;
from dotenv import load_dotenv;
from prompts import system_prompt;

def main():

    parser = argparse.ArgumentParser(description="Sentient AI Agent");
    parser.add_argument("prompt", type=str,help="User prompt");
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output");
    args = parser.parse_args();
    AI_prompt = args.prompt;
    print_vebose = args.verbose;


    messages = [types.Content(role="user", parts=[types.Part(text=AI_prompt)])];
    

    load_dotenv();
    api_key = os.environ.get('GEMINI_API_KEY');
    if api_key is None:
        raise RuntimeError('API key not found in .env file');

    
    client = genai.Client(api_key = api_key);
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
        );
    gemini_metadata = response.usage_metadata;
    
        


    if gemini_metadata is not None and print_vebose:
        print(f"User prompt: {AI_prompt}");
        print(f"Prompt tokens: {gemini_metadata.prompt_token_count}");
        print(f"Response tokens: {gemini_metadata.total_token_count - gemini_metadata.prompt_token_count}")

    print(response.text);
    
    #print("Hello from agient!")


if __name__ == "__main__":
    main()