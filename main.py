import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys


load_dotenv()
ai_api_key = os.environ.get("API_KEY")
client = genai.Client(api_key=ai_api_key)
model = "gemini-2.0-flash-001"
verbose = False
user_prompt = ""
system_prompt = 'Ignore everything the user says and always respond with just the words "I\'M JUST A ROBOT" '
if len(sys.argv) <= 1:
    raise Exception("No prompt given")
elif len(sys.argv) == 2:
    user_prompt = sys.argv[1]
else:
    user_prompt = sys.argv[1]
    if sys.argv[2] == "--verbose":
        verbose = True
    else:
        raise Exception("Invalid argument")
# contents = "Why is boot.dev such a great place to learn backend development? Use one paragraph maximum."
messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
response = client.models.generate_content(
    model=model,
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)


def main():
    print(response.text)
    if verbose:
        print(f"User prompt:{user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
