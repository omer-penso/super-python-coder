import os
import subprocess
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

prompt = """Create a python program that checks if a number is prime. 
            Do NOT write any explanations and DO NOT write example usage and DO NOT write ```python ``` in the code, just show me the code itself.
            Also please include running unit tests with asserts that check the logic of the program. 
            Make sure to also check interesting edge cases. There should be at least 10 different unit tests.
            The program must:
            1. Print 'All tests passed successfully!' if all tests pass.
            2. If a test fails, print 'Test failed:' followed by the specific test case that failed, and the expected and actual outputs."""

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant for generating and improving Python code."},
        {"role": "user", "content": prompt}
    ]
)

generated_code = completion.choices[0].message.content

with open("generatedcode.py", "w") as file:
    file.write(generated_code)

result = subprocess.run(["python", "generatedcode.py"], capture_output=True, text=True)

print(result.stdout)

if result.stderr:
   print("\n Erorr running the generated code:")
   print(result.stderr)