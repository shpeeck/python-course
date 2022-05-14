# Task 2

def positive():
    print("Положительное")
    
def negative():
    print("Отрицательное")

def test():
    my_int = input("Введите целое число ")
    if int(my_int):
        my_int = int(my_int)
        if my_int >= 0:
            positive()
        else:
            negative()
    else:
        print("Вы ввели 0")

def func():
    test()


func()

# Порядок объявления функций значения не имеет,
# так как интерпретатор первым делом делает анализ кода, проходит
# его построчно и находя функции пропускает их. 
# Единственное, функция должна быть объявлена до ее вызова

