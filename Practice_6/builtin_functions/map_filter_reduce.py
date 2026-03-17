from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. map() — multiply each number by 2
print("1.", list(map(lambda x: x * 2, nums)))

# 2. map() — square each number
print("2.", list(map(lambda x: x ** 2, nums)))

# 3. map() — convert words to uppercase
words = ["hello", "world", "python"]
print("3.", list(map(str.upper, words)))

# 4. map() — get the length of each word
print("4.", list(map(len, words)))

# 5. filter() — keep only even numbers
print("5.", list(filter(lambda x: x % 2 == 0, nums)))

# 6. filter() — keep only odd numbers
print("6.", list(filter(lambda x: x % 2 != 0, nums)))

# 7. filter() — keep numbers greater than 5
print("7.", list(filter(lambda x: x > 5, nums)))

# 8. reduce() — sum all numbers
print("8.", reduce(lambda x, y: x + y, nums))

# 9. reduce() — multiply all numbers (product)
print("9.", reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))

# 10. reduce() — find the maximum number
print("10.", reduce(lambda x, y: x if x > y else y, nums))