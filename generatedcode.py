def is_palindrome(n):
    """Check if the given number n is a palindrome."""
    if n < 0:
        return False
    s = str(n)
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

def run_tests():
    """Run a set of tests to validate the is_palindrome function."""
    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (12321, True),
        (123321, True),
        (12345, False),
        (1, True),
        (11111, True),
        (1001, True),
        (10001, True),
        (1234321, True)
    ]
    
    for number, expected in test_cases:
        result = is_palindrome(number)
        assert result == expected, f'Test failed: {number}, expected {expected}, got {result}'

    print('All tests passed successfully!')

run_tests()