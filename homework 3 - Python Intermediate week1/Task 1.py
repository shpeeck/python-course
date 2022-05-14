class My_Mixin:
    @staticmethod
    def sub_static(a, b):
        return f"{a.num - b.num} {a.den - b.den}"
    
    @staticmethod
    def add_static(a, b):
        return f"{a.num + b.num} {a.den + b.den}"
    
    @staticmethod
    def mul_static(a, b):
        return f"{a.num * b.num} {a.den * b.den}"
    
    @staticmethod
    def truediv_static(a, b):
        try:
            return f"{a.num / b.num} {a.den / b.den}"
        except:
            print("ZeroDivisionError")


class Fraction(My_Mixin):
    def  __init__(self, num, den):
        self.__num = num
        self.__den = den
        
    def __str__(self):
        return f"{self.num}/{self.den}"
    
    @property
    def num(self):
        return self.__num
    
    @property
    def den(self):
        return self.__den
    
    def __sub__(self, second):
        return self.__class__(self.num - second.num, self.den - second.den)
    
    def __add__(self, second):
        return self.__class__(self.num + second.num, self.den + second.den)
    
    def __mul__(self, second):
        return self.__class__(self.num * second.num, self.den * second.den)
    
    def __truediv__(self, second):
        try:
            return self.__class__(self.num / second.num, self.den / second.den)
        except:
            print(ZeroDivisionError)
            return self.__class__(0, 0)
    
    @classmethod
    def classmethod_return(cls, str):
        try:
            str = str.split("/")
            return Fraction(int(str[0]), int(str[1]))
        except:
            print("wrong string")
            return Fraction(0, 0)
        

        

a = Fraction(10, 20)
b = Fraction(1, 5)

print("a: ", a)
print("b: ", b)
c = a - b
print("sub: ", c)
c = a + b
print("add: ", c)
c = a * b
print("mul: ", c)
c = a / b
print("truediv: ", c)

print("mixin sub: ", Fraction.sub_static(a, b))
print("mixin add: ", Fraction.add_static(a, b))
print("mixin mul: ", Fraction.mul_static(a, b))
print("mixin truediv: ", Fraction.truediv_static(a, b))
d = Fraction.classmethod_return("3/2")
print(d)
print(f"d num: {d.num}, d den: {d.den}")


