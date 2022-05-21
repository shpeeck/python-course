#Task 3

# 1
def fib_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for i in fib_generator(10):
    print(i)


# 2
def fib_list(n):
    def itr(n):
        a, b = 0, 1
        for i in range(n):
            yield a
            a, b = b, a + b
    lst = list(itr(n))
    return lst


print(fib_list(15))
