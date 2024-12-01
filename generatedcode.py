def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]

def run_tests():
    tests = [
        (121, True), 
        (-121, False), 
        (10, False), 
        (0, True), 
        (12321, True), 
        (123456, False), 
        (1, True), 
        (11, True), 
        (1001, True), 
        (1234321, True)
    ]
    
    for i, (num, expected) in enumerate(tests):
        actual = is_palindrome(num)
        if actual != expected:
            print(f'Test failed: test case {i + 1} with input {num}, expected {expected}, but got {actual}')
            return
    
    print('All tests passed successfully!')

run_tests()