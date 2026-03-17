# 1. Write down the line
with open("out.txt", "w") as f:
    f.write("Hello!\n")

# 2. We'll add it to the end
with open("out.txt", "a") as f:
    f.write("World!\n")

# 3. We write a list of lines
with open("out.txt", "w") as f:
    f.writelines(["line1\n", "line2\n", "line3\n"])

# 4. Write down the number
with open("num.txt", "w") as f:
    f.write(str(42))

# 5. We write through a loop
with open("nums.txt", "w") as f:
    for i in range(1, 6):
        f.write(str(i) + "\n")

# 6. Writing f-string
name = "Amir"
age = 20
with open("person.txt", "w") as f:
    f.write(f"Имя: {name}, Возраст: {age}\n")

# 7. We write using print()
with open("print.txt", "w") as f:
    print("Привет из print!", file=f)

# 8. We write down several variables
x, y = 10, 20
with open("vars.txt", "w") as f:
    f.write(f"x={x}, y={y}, sum={x+y}\n")

# 9. Overwriting the file
with open("out.txt", "w") as f:
    f.write("Файл перезаписан\n")

# 10. Handling a write error
try:
    with open("/root/secret.txt", "w") as f:
        f.write("test")
except PermissionError:
    print("Нет прав для записи!")