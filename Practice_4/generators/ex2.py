n = int(input("Enter a number: "))
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield str(i)
print(",".join(even_numbers(n)))