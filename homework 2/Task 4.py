#Task 4

def getInput():
    a = input("Введи число ")
    return a

def testInput(num):
    return num.isdigit()

def strToInt(num):
    return int(num)

def printInt(inf):
    print(inf)
    

res = getInput()
if testInput(res):
    printInt(strToInt(res))
    
