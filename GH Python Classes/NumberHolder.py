class NumberHolder:
    def __init__(self, number):
        self.number = number

    def returnNumber (self):
        return self.number

var = NumberHolder(44)
var2 = NumberHolder(98)
print(var.returnNumber())
print(var2.returnNumber())

