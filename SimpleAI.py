import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load your API key from an environment variable
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI API client
openai.api_key = api_key

def main():
    myPrompt = input("Enter your prompt: ")
    
    try:
        # Make a completion request to the OpenAI API
        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=myPrompt,
            max_tokens=1024,
            temperature=0
        )
        
        # Print the text of the first completion
        print(response.choices[0].text.strip())
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
