#Task 1

class FormulaError(Exception):
    def __init__(self, message='We have a problem'):
        self.message = message
        super().__init__(self.message)
    

def calc(stroke: str):
    stroke = stroke.strip().split(' ')
    if len(stroke) != 3:
        raise FormulaError()
    if stroke[1] not in ('+', '-', '*', '/'):
        raise FormulaError()
    try:
        stroke[0], stroke[2] = float(stroke[0]), float(stroke[2])
    except ValueError:
        raise FormulaError()
    else:
        if stroke[1] == '+':
            return (stroke[0] + stroke[2])
        elif stroke[1] == '-':
            return (stroke[0] - stroke[2])
        elif stroke[1] == '*':
            return (stroke[0] * stroke[2])
        elif stroke[1] == '/':
            try:
                return (stroke[0] / stroke[2])
            except ZeroDivisionError:
                return 'ZeroDivisionError'


print(calc('5 + 1'))
print(calc('5 - 1'))
print(calc('5 * 1'))
print(calc('5 / 1'))
print(calc('5 / 0'))