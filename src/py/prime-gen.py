from math import sqrt


## checks if 'n' is a prime number.
def prime(n):
    t = int(sqrt(n))
    for d in range(2, t + 1):
        if n % d == 0:
            return False
    return True


## produce a list of first 'n' primes.
def first_primes(n):
    primes = [2]  # the one and only even prime!
    n -= 1  # we have one prime in hand
    next = 3  # starting number
    while n > 0:
        if prime(next):
            primes.append(next)
            n -= 1
        next += 2  # move past the even number
    ##
    return primes


def test_first_primes():
    assert first_primes(1) == [2]
    assert first_primes(2) == [2, 3]
    assert first_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert first_primes(1024)[1023] == 8161
    assert first_primes(2048)[2047] == 17863


test_first_primes()
