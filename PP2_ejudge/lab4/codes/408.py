def isprime(n):
    for x in range(2, n+1):
        is_prime = True
        for d in range(2, int(x**0.5)+1):
            if x%d == 0:
                is_prime = False
                break
        if is_prime:
            yield x

n = int(input())
print(" ".join(map(str, isprime(n))))