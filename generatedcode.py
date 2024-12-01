def is_palindrome(num):
    """Check if a number is a palindrome."""
    if num < 0:
        return False
    str_num = str(num)
    left, right = 0, len(str_num) - 1
    while left < right:
        if str_num[left] != str_num[right]:
            return False
        left += 1
        right -= 1
    return True

def run_tests():
    """Run tests for the is_palindrome function."""
    test_cases = [
        (121, True), (12321, True), (123, False),
        (1, True), (0, True), (-121, False),
        (10, False), (1001, True), (2002, True),
        (1234321, True)
    ]

    for input_val, expected in test_cases:
        actual = is_palindrome(input_val)
        assert actual == expected, f'Test failed: input({input_val}), expected({expected}), actual({actual})'

    print('All tests passed successfully!')

if __name__ == "__main__":
    run_tests()