#Task 2

class ReverseIter:
    def __init__(self, lst):
        self.lst = list(reversed(lst))
        self.iterator = iter(self.lst)

    def rev(self):
        while True:
            try:
                print(next(self.iterator))
            except StopIteration:
                break
        
    def __repr__(self):
        return repr(self.rev())
    

i = [1, 2, 3, 4, 5, 6, 7, 'n']
a = ReverseIter(i)
a
