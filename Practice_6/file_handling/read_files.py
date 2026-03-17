# 1. Reading files
with open("test.txt", "r") as f:
    print(f.read())

# 2. Reading one str
with open("test.txt", "r") as f:
    print(f.readline())

# 3. Reading all strings in list
with open("test.txt", "r") as f:
    print(f.readlines())

# 4. Reading string in cycle
with open("test.txt", "r") as f:
    for line in f:
        print(line.strip())

# 5. Read the first 5 characters
with open("test.txt", "r") as f:
    print(f.read(5))

# 6. Counting the number of lines
with open("test.txt", "r") as f:
    print(len(f.readlines()))

# 7. We are looking for a line with a word
with open("test.txt", "r") as f:
    for line in f:
        if "banana" in line:
            print("Найдено:", line.strip())

# 8. Read and remove spaces
with open("test.txt", "r") as f:
    lines = [line.strip() for line in f]
print(lines)

# 9. Read in uppercase
with open("test.txt", "r") as f:
    print(f.read().upper())

# 10. Error handling - file not found
try:
    with open("nofile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Файл не найден!")