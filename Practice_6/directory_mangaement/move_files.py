import os
import shutil

# Preparation
os.makedirs("src", exist_ok=True)
os.makedirs("dst", exist_ok=True)
for i in range(1, 6):
    with open(f"src/file{i}.txt", "w") as f:
        f.write(f"file {i}")

# 1. Moving the file
shutil.move("src/file1.txt", "dst/file1.txt")
print("1. Перемещён file1.txt в dst/")

# 2. Move to the folder
shutil.move("src/file2.txt", "dst/")
print("2. Перемещён file2.txt в dst/")

# 3. Renaming the file
os.rename("src/file3.txt", "src/file3_new.txt")
print("3. Переименован: file3.txt → file3_new.txt")

# 4. Rename via shutil.move()
shutil.move("src/file3_new.txt", "src/file3_final.txt")
print("4. Переименован через move()")

# 5. Renaming the folder
os.makedirs("old_name", exist_ok=True)
os.rename("old_name", "new_name")
print("5. Папка переименована: old_name → new_name")

# 6. Moving the folder
shutil.move("new_name", "dst/new_name")
print("6. Папка перемещена в dst/")

# 7. Getting the file name from the path
path = "dst/file1.txt"
print("7. Имя файла:", os.path.basename(path))

# 8. Getting a folder from the path
print("8. Папка:", os.path.dirname(path))

# 9. Moving with verification
if os.path.exists("src/file4.txt"):
    shutil.move("src/file4.txt", "dst/file4.txt")
    print("9. file4.txt перемещён")

# 10. Error while moving
try:
    shutil.move("src/ghost.txt", "dst/")
except FileNotFoundError:
    print("10. Файл не найден — ошибка поймана")

# Cleaning
shutil.rmtree("src", ignore_errors=True)
shutil.rmtree("dst", ignore_errors=True)