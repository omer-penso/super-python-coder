def is_palindrome(number):
    """Check if the given number is a palindrome."""
    if number < 0:
        return False
    str_num = str(number)
    left, right = 0, len(str_num) - 1
    while left < right:
        if str_num[left] != str_num[right]:
            return False
        left += 1
        right -= 1
    return True

def run_tests():
    """Run the test cases to check the is_palindrome function."""
    test_cases = [
        (121, True), ( -121, False), (10, False), (12321, True),
        (0, True), (1, True), (123454321, True), (123456, False),
        (99999, True), (12345678987654321, True), (-1, False),
        (1001, True), (10001, True), (1000021, False), (1000001, True),
    ]

    for input_value, expected in test_cases:
        result = is_palindrome(input_value)
        assert result == expected, f'Test failed: Input: {input_value}, Expected: {expected}, Actual: {result}'

    print('All tests passed successfully!')

if __name__ == "__main__":
    run_tests()