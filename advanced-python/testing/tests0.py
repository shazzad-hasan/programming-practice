from prime import is_prime 

def test_prime(n, expected):
    if is_prime(n) != expected:
        print(f"Error on is_prime({n}), expected {expected}")

if __name__ == "__main__":
    print(test_prime(5, True))
    print(test_prime(10, False))
    print(test_prime(25, False)) # this will indicate that there is a bug in the code