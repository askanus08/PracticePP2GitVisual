import os
import shutil

# 1. Create a folder
os.mkdir("myfolder")
print("1. Создана: myfolder")

# 2. Create nested folders
os.makedirs("a/b/c", exist_ok=True)
print("2. Созданы: a/b/c")

# 3. Current folder
print("3. Текущая папка:", os.getcwd())

# 4. List everything in the current folder
print("4. Содержимое:", os.listdir("."))

# 5. Folders only
items = os.listdir(".")
dirs = [i for i in items if os.path.isdir(i)]
print("5. Папки:", dirs)

# 6. Files only
files = [i for i in items if os.path.isfile(i)]
print("6. Файлы:", files)

# 7. Does the folder exist?
print("7. myfolder существует?", os.path.isdir("myfolder"))
print("7. xyz существует?",      os.path.isdir("xyz"))

# 8. Absolute path
print("8. Абсолютный путь:", os.path.abspath("myfolder"))

# 9. Traversing folders using os.walk()
for root, dirs_w, files_w in os.walk("a"):
    print(f"9. root={root}, dirs={dirs_w}, files={files_w}")

# 10. Create + check + delete
os.makedirs("temp", exist_ok=True)
print("10. temp создана?", os.path.isdir("temp"))
os.rmdir("temp")
print("10. temp удалена?", not os.path.isdir("temp"))

# Cleaning
shutil.rmtree("myfolder", ignore_errors=True)
shutil.rmtree("a", ignore_errors=True)