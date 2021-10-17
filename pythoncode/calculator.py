class Calculator():
    def add(self, a, b):
        return a+b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def divid(self, a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            return "除数不能为0"


# if __name__ == '__main__':
#     calc = Calculator()
#     print(calc.divid(2,0))
