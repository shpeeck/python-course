##Task 3
    
i = 0
a = []
while i < 8:
    res = input("Введите число ")
    if res.isnumeric():
        a.append(int(res))
        i +=1
    else:
        print("Не число!")

print("Сумма введенных чисел -", sum(a))
print("Максимальное число -", max(a))
print("Минимальное число -", min(a))


