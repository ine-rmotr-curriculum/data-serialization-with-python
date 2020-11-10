from math import sqrt, log, nan

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