#task 1

from contextlib import contextmanager

file_name = input("Введите название файла: ").strip() or "demo.txt"
new_file_name = input("Как назвать новый файл: ") or file_name.split(".")[0] + "_1.txt"

if ".txt" not in file_name:
    file_name = f"{file_name}.txt"

if ".txt" not in new_file_name:
    new_file_name = f"{new_file_name}.txt"

@contextmanager
def file_open(path, mode):
    try:
        file = open(path, mode)
        yield file
    except OSError:
        print("Что-то пошло не так")
    finally:
        file.close()
        
with file_open(file_name, "r") as file:
    number = 1
    for line in file:
        with file_open(new_file_name, "a") as file1:
            file1.write(f"{number}: {line}")
        number += 1
        
print("Документ создан!")
        
        