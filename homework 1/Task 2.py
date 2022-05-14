##Task 2

first = input("Введите первое число ")
second = input("Введите второе число ")
if first.isnumeric() and second.isnumeric():
    if int(first) > int(second):
        print("True")
    else:
        print("False")
else:
    print("Вы ввели не число!")





