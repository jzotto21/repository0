"""EX03 - prime functions."""

__author__: str = "730163077"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))
    print(is_prime(5))
    print(is_prime(11))
    print(is_prime(6))
    print(is_prime(2))
    print(is_prime(99))
    print(is_prime(4))
    print(list_primes(3, 7))
    print(list_primes(10, 20))
    

def is_prime(x: int) -> bool:
    """This will state if a number is prime or not."""
    if x <= 1:
        return False 
    if x == 2:
        return True
    i = 2
    while i <= (x // 2):
        if x % i == 0:  
            return False
        i += 1
    return True
    

def list_primes(y: int, z: int) -> list[int]:
    """List range of prime numbers."""
    primes: list[int] = []
    for i in range(y, z):
        if is_prime(i):
            primes.append(i)
    return primes
    

if __name__ == "__main__":
    main()