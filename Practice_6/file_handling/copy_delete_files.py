import os
import shutil

# Creating test files
with open("a.txt", "w") as f: f.write("file a")
with open("b.txt", "w") as f: f.write("file b")
os.makedirs("folder1", exist_ok=True)

# 1. Copying the file
shutil.copy("a.txt", "a_copy.txt")
print("1. Скопирован: a_copy.txt")

# 2. Copy to folder
shutil.copy("a.txt", "folder1/")
print("2. Скопирован в folder1/")

# 3. Copy with metadata
shutil.copy2("b.txt", "b_copy.txt")
print("3. Скопирован с метаданными: b_copy.txt")

# 4. Delete the file
os.remove("a_copy.txt")
print("4. Удалён: a_copy.txt")

# 5. Delete via unlink
os.unlink("b_copy.txt")
print("5. Удалён через unlink: b_copy.txt")

# 6. Create and delete an empty folder
os.mkdir("empty")
os.rmdir("empty")
print("6. Пустая папка удалена")

# 7. Delete the folder with its contents
shutil.rmtree("folder1")
print("7. folder1 удалена со всем содержимым")

# 8. Check before deleting
if os.path.exists("b.txt"):
    os.remove("b.txt")
    print("8. b.txt удалён")

# 9. Copying a folder tree
os.makedirs("src/sub", exist_ok=True)
with open("src/sub/data.txt", "w") as f: f.write("data")
shutil.copytree("src", "src_backup")
print("9. Дерево скопировано: src_backup/")

# 10. Error deleting non-existent file
try:
    os.remove("ghost.txt")
except FileNotFoundError:
    print("10. Файл не найден — ошибка поймана")

# Cleaning
shutil.rmtree("src", ignore_errors=True)
shutil.rmtree("src_backup", ignore_errors=True)
os.remove("a.txt") if os.path.exists("a.txt") else None