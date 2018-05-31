import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     future_to_prime = {executor.submit(is_prime, prime): prime for prime in PRIMES}
    #     for future in concurrent.futures.as_completed(future_to_prime):
    #         prime = future_to_prime[future]
    #         try:
    #         result = future.result()
    #         except Exception as exc:
    #             print('%r generated an exception: %s' % (prime, exc))
    #         else:
    #             print('%d is prime: %s' % (prime, result))

if __name__ == '__main__':
    main()
