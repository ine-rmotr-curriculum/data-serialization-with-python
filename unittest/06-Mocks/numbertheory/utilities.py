from math import sqrt, log, nan
from fractions import Fraction
from collections import namedtuple
from random import randint
import requests

Ratio = namedtuple("Ratio", "numerator denominator")


def get_primes_upto(limit):
    "A list of all primes less than or equal to limit"
    is_prime = [False] * 2 + [True] * (limit-1)
    for n in range(int(sqrt(limit) + 1.5)): 
        if is_prime[n]:
            is_prime[n**2::n] = [False] * ((limit - n**2)//n + 1)
    return trues(is_prime)


def prime_count(limit):
    "Upper bound on number of primes below a limit"
    # Gauss/Legendre approx, padded to exceed π(x) for small limits
    return int(1.2 * limit/log(limit))


def get_init_primes(N):
    "Return the first N prime numbers"
    # Find "enough" primes
    limit = 8
    while N > prime_count(limit):
        limit *= 2
    many_primes = get_primes_upto(limit)
    # Return exactly N of them
    return many_primes[:N]


def trues(it): 
    "Which elements of 'bitfield iterable' are True?"
    return [n for n, target in enumerate(it) if target]


def sums_of_subset(numbers):
    "The natural numbers that are sums of subsets of initial set"
    numbers = sorted(numbers)                 # Numbers in ascending order
    sum_of_numbers = sum(numbers)
    reachable = [False] * (sum_of_numbers+1)  # Trues as one-based index
    for p in numbers:
        reachable[p] = True 
        for n, target in enumerate(reachable[:]):
            if target and  n != p:
                reachable[p+n] = True
    return trues(reachable)


def pair_sums(numbers, allow_doubles=False):
    "Sums of elements from initial set"
    sums = set()
    numbers = sorted(numbers)
    for i in numbers:
        for j in numbers:
            if allow_doubles or i != j:
                sums.add(i+j)
    return sums


def power(x, y, p):
    "Compute (x^y) % p  efficiently for large numbers"    
    result = 1  
    x = x % p      # Reduce x if larger than p
    while y > 0:
        if y % 2:  # If y odd, multiply x with result
            result = (result * x) % p
        y //= 2
        x = (x * x) % p; 
    return result


def MillerRabin(d: int, n: int) -> bool:
    "Perform one MillerRabin test on n using an odd d"
    assert d % 2
    a = 2 + randint(1, n-4); 
  
    # Compute a^d % n 
    x = power(a, d, n); 
  
    if (x == 1 or x == n - 1): 
        return True; 
  
    # Keep squaring x while one  
    # of the following doesn't  
    # happen 
    # (i) d does not reach n-1 
    # (ii) (x^2) % n is not 1 
    # (iii) (x^2) % n is not n-1 
    while (d != n - 1): 
        x = (x * x) % n 
        d *= 2
  
        if (x == 1): 
            return False
        if (x == n - 1): 
            return True 
  
    # It is composite 
    return False

  
def likely_prime(n: int, k: int=20) -> bool:
    """Test if a number is VERY LIKELY to be prime
    
    Implementation uses the Miller-Rabin Primality Test
    
    n: Natural Number to check
    k: number of rounds (default 20)
    
    Default 20 rounds wrong less than one in trillion 
    40 rounds less likely than cosmic ray interfering
    
    return:  Boolean answer
    """
    if (n <= 1 or n == 4): 
        return False; 
    if (n <= 3): 
        return True; 
  
    d = n-1 
    while not d%2: 
        d //= 2 
  
    # Iterate k times 
    for _ in range(k): 
        if not MillerRabin(d, n): 
            return False; 
  
    return True; 


def count_primes_in_file(filename: str) -> Ratio:
    """Count the fraction of primes within a text file
    
    filename: file of Natural Numbers as strings, once per line
    """
    numerator, denominator = 0, 0
    with open(filename) as fh:
        for line in fh:
            n = int(line.strip())
            denominator += 1
            if likely_prime(n):
                numerator += 1
                
    return Ratio(numerator, denominator)
            

def random_uint64_to_file(filename: str=None, count: int=10_000, _inc=[1]):
    """Create a file of Natural Numbers up to 2^64-1
    
    filename: the file where numbers will be saved
    count: number of numbers to write, one per line (default 100)
    
    Uses /dev/urandom as source of randomness rather than Python
    pseudo-random Mersenne Twister algorithm
    
    return: filename (generated if not provided)
    """
    if filename is None:
        filename = f'tmp-{_inc[0]}.txt'
        _inc[0] += 1
        
    with open('/dev/urandom', 'rb') as rnd:
        with open(filename, 'w') as nums:
            while count > 0:
                n = int.from_bytes(rnd.read(8), byteorder='little', signed=False)
                if n > 0:  # Only non-negative integers
                    count -= 1
                    print(n, file=nums)

    return filename


def get_primes_between(start=0, end=100):
    "Find all primes in interval [start, end]"
    assert start < end
    url = f'http://example.org/primes-between/json/{start}/{end}'
    response = requests.get(url)
    return response.json()
    
    
    