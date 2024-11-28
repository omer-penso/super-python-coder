def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def run_tests():
    test_cases = [
        (1, False),  # Edge case: 1 is not prime
        (2, True),   # Edge case: 2 is prime
        (3, True),   # 3 is prime
        (4, False),  # 4 is not prime
        (5, True),   # 5 is prime
        (16, False), # 16 is not prime
        (17, True),  # 17 is prime
        (18, False), # 18 is not prime
        (19, True),  # 19 is prime
        (25, False), # 25 is not prime
        (97, True),  # 97 is prime
        (100, False) # 100 is not prime
    ]

    for number, expected in test_cases:
        actual = is_prime(number)
        assert actual == expected, f'Test failed: is_prime({number}) expected {expected}, got {actual}'

    print('All tests passed successfully!')

run_tests()