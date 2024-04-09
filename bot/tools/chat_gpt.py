from openai import OpenAI

from dotenv import load_dotenv
import os


load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url='https://api.proxyapi.ru/openai/v1',
)


def chat_with_gpt(msg):
    messages = [{'role': 'user', 'content': msg}]

    while True:
        chat_completion = client.chat.completions.create(
            model='gpt-3.5-turbo-1106',
            messages=messages
        )
        response = chat_completion.choices[0].message.content
        return response
