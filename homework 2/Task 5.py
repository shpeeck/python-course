#Task 5

#1
##while True:
##    a = input("Enter a positive number of unicode ")
##    if a == "0":
##        print("Quit")
##        break
##    else:
##        if a.isdigit() and int(a)<65530:
##            print(chr(int(a)))
##        else:
##            print("Not a number or the number is big")
            

#2
##line = input("enter a line ")
##if len(line) > 10:
##    print("alert!")
##else:
##    print(line + "*"*(10-len(line)))
    
#3
lst = []

for i in range(6):
    num = input("Enter a number ")
    lst.append(float(num))

max = lst[0]
min = lst[0]

for i in range(len(lst)):
    if lst[i]>max:
        max = lst[i]
    if lst[i]<min:
        min = lst[i]
        
print("max ", '%.2f' % max)
print("min ", '%.2f' % min)

