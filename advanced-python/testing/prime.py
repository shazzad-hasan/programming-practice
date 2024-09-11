import math

def is_prime(n):
    if n < 2:
        return False 
    if n % 2 == 0:
        return False
    for i in range(2, int(math.sqrt(n))): # Note: adding 1 with sqrt(n) fixes the bug
        if n % i == 0:
            return False 
    return True

if __name__ == "__main__":
    print(is_prime(5))
    print(is_prime(10))