fruits  = ["apple", "banana", "cherry"]
prices  = [1.2, 0.5, 2.0]
colors  = ["red", "yellow", "dark red"]

# 1. enumerate() — get index and value
for i, fruit in enumerate(fruits):
    print(f"1. {i}: {fruit}")

# 2. enumerate() — start index from 1
for i, fruit in enumerate(fruits, start=1):
    print(f"2. {i}. {fruit}")

# 3. enumerate() — create a dictionary from index-value pairs
d = {i: v for i, v in enumerate(fruits)}
print("3.", d)

# 4. enumerate() — find the index of a specific element
for i, f in enumerate(fruits):
    if f == "banana":
        print("4. banana is at index:", i)

# 5. enumerate() — iterate over characters of a string
for i, ch in enumerate("Python"):
    print(f"5. [{i}]={ch}", end=" ")
print()

# 6. zip() — combine two lists into pairs
for fruit, price in zip(fruits, prices):
    print(f"6. {fruit}: ${price}")

# 7. zip() — combine three lists at once
for fruit, price, color in zip(fruits, prices, colors):
    print(f"7. {fruit} ({color}): ${price}")

# 8. zip() — create a dictionary from two lists
d2 = dict(zip(fruits, prices))
print("8.", d2)

# 9. zip() — unzip a list of tuples back into separate lists
pairs = [(1, "a"), (2, "b"), (3, "c")]
nums, letters = zip(*pairs)
print("9. nums:", nums, "| letters:", letters)

# 10. enumerate() + zip() — combine both functions together
for i, (fruit, price) in enumerate(zip(fruits, prices), start=1):
    print(f"10. #{i} {fruit} = ${price}")