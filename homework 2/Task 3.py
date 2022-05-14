# Task 3

def concat ():
    a = input("input the message 1 ")
    b = input("input the message 2 ")
    return (f'{a} {b}')

print(concat())

def func():
    res = 1
    while True:
        my_int = input("Введите целое число ")
        if my_int.isnumeric():
            if my_int == "0":
                print("Вы ввели 0, программа завершена")
                break
            my_int = int(my_int)
            res = res * my_int
            print(f"Результат: {res}")
        else:
            print("Не целое число")
func()