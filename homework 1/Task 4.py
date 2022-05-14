##Task 4

stroke = input("Введите текст ")
large = 0
small = 0
for i in stroke:
    if i.isupper():
        large += 1
    elif i.islower():
        small += 1
if small > large:
    print(stroke.lower())
elif large > small:
    print(stroke.upper())
else:
    print(stroke)