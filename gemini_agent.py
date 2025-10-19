import os
from google import genai
from google.genai.errors import APIError

def py_code_generator(content):
    model_name = 'gemini-2.5-flash'
    api_key = os.getenv("GEMINI_API_KEY")
    split_criteria = {}
    split_criteria['head'] = '```python'
    split_criteria['tail'] = '```'

    model_name = 'gemini-2.5-flash'
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: can not find GEMINI_APY_KEY variable. Please make sure it's set up properly")
        return
    try:
        client = genai.Client()
        print("Trying to connect to Gemini API...")
        
        # input content
        response = client.models.generate_content(
            model=model_name,
            contents=content
        )
        print("Giving the answer:\n")
        answer_text = response.text.split(split_criteria['head'])[-1].split(split_criteria['tail'])[0].split('\n')
        for idx, string in enumerate(answer_text):
            # if_delete = False
            if (len(string) == 0): # empty string
                del answer_text[idx]
            else:
                print(string)

        print('Answer given. Anything else?')

    except APIError as e:
        print(f"API find to connect or other error occurs: {e}")
        print("Please check whether the GEMINI_API_KEY is valid, and the network connection isworking")
    except Exception as e:
        print(f"Unexpected error: {e}")

def create_chat(content):
    model_name = 'gemini-2.5-flash'
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: can not find GEMINI_APY_KEY variable. Please make sure it's set up properly")
        return
    try:
        client = genai.Client()
        print("Trying the connection to Gemini API...")
        
        # input content
        response = client.models.generate_content(
            model=model_name,
            contents=content
        )

        # response
        print("--- API response success ---")
        print(response.text)
        print("--------------------")

    except APIError as e:
        print(f"API find to connect or other error occurs: {e}")
        print("Please check whether the GEMINI_API_KEY is valid, and the network connection isworking")
    except Exception as e:
        print(f"Unexpected error: {e}")


def run():
    while True: 
        question = input("\nWhat you wanna ask?\nInput: ")
        if question.lower() == 'stop':
            break
        else:
            py_code_generator(question)

    print('The program has been stopped')

if __name__ == "__main__":
    run()
