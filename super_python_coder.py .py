import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Create a python program that checks if a number is prime. Do NOT write any explanations and DO NOT write example usage and DO NOT write '''python ``` , just show me the code itself"}
    ]
)

generated_code = completion.choices[0].message.content

with open("generatedcode.py", "w") as file:
    file.write(generated_code)

print("Generated Python code saved to generatedcode.py:")
print(generated_code)