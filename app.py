import os
import subprocess
import random
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

PROGRAMS_LIST = [
    '''Given two strings str1 and str2, prints all interleavings of the given
    two strings. You may assume that all characters in both strings are
    different. Input: str1 = "AB", str2 = "CD"
    Output: ABCD ACBD ACDB CABD CADB CDAB
    Input: str1 = "AB", str2 = "C"
    Output: ABC ACB CAB''',
    "A program that checks if a number is a palindrome.",
    "A program that finds the kth smallest element in a given binary search tree.",
    "A program that run BFS on a graph.",
    "A program that implements dijkstra's algorithm.",
]

print("I'm Super Python Coder. Tell me, which program would you like me to code for you?")
user_input = input("If you don't have an idea, just press enter, and I will choose a random program to code: ")

if not user_input:
    program_idea = random.choice(PROGRAMS_LIST)
else:
    program_idea = user_input

print(f"Chosen program idea: {program_idea}\n")

prompt = f"""Create a python program that implements: {program_idea}. 
            Do NOT write any explanations and DO NOT write example usage and DO NOT write ```python ``` in the code, just show the code itself.
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

file_path = "generatedcode.py"
with open(file_path, "w") as file:
    file.write(generated_code)

def measure_execution_time():
    start_time = time.time()
    result = subprocess.run(["python", file_path], capture_output=True, text=True)
    if result.returncode == 0 and "All tests passed successfully!" in result.stdout:
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        return execution_time
    return None


max_retries = 5
attempt = 0
while attempt < max_retries:
    result = subprocess.run(["python", file_path], capture_output=True, text=True)
    execution_time = measure_execution_time()
    
    if execution_time is not None:
        print(f"Code creation completed successfully in {execution_time:.2f} ms!")
        break
    else:  # Error or test failure
        if result.stderr:
            print(f"Error running generated code! Error: {result.stderr}. Trying again...")
        
        if "Test failed:" in result.stdout:
            print(f"Test failed. Error: {result.stdout}")
        
        # Send the error back to OpenAI for fixing
        error_message = result.stderr or result.stdout
        prompt = f"""Here is the code generated for a program that implements {program_idea}: {generated_code}. 
                   However, it failed with this error: {error_message}. Please fix the code and show me the entire corrected code.
                   IMPORTANT: The fixed code should be written in a way that it can be run directly! Do NOT include any explanations or comments in the code.
                   also DO NOT write ```python ``` in the code!"""
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for generating, improving and fix Python code."},
                {"role": "user", "content": prompt}]
        )
        
        generated_code = completion.choices[0].message.content
        with open(file_path, "w") as file:
            file.write(generated_code)
        
        attempt += 1
        print(f"Retrying... Attempt {attempt}/{max_retries}")

if attempt == max_retries:
    print("Code generation FAILED")
    exit()

original_code = generated_code
original_time = execution_time

# Optimization step
if original_time is not None:
    prompt_optimization = f"""Here is the code and unit tests generated for a program that implements {program_idea}: {generated_code}.
                         It passed all unit tests successfully in {original_time:.2f} ms.
                         Please optimize the code to make it run faster while keeping the same unit tests and functionality.
                         Show me the entire optimized code. Do NOT include any explanations or comments in the code.
                         Also DO NOT write ```python ``` in the code!"""
    completion_optimization = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for generating optimized Python code."},
            {"role": "user", "content": prompt_optimization}
        ]
    )

    optimized_code = completion_optimization.choices[0].message.content

    with open(file_path, "w") as file:
        file.write(optimized_code)

    execution_time_optimized = measure_execution_time()

    if execution_time_optimized is not None:
        if execution_time_optimized < original_time:
            print(f"Code running time optimized! It now runs in {execution_time_optimized:.2f} ms, while before it was {original_time:.2f} ms.")
        else:
            print("Optimization attempt did not improve running time.")
            with open(file_path, "w") as file:
                file.write(original_code)
    else:
        print("Optimized code failed. Restoring original code.")
        with open(file_path, "w") as file:
            file.write(original_code)
# Open the generated file using subprocess
subprocess.call(["start", file_path], shell=True) 