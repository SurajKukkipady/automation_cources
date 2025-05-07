# self keyword is mandatory in class methods
# class is a blueprint of an object
# instance and class variables have different memory locations
# constructor is a special method which is automatically called when an object is created

class Calculator:
    num = 100 #class variable

    #default constructor
    def __init__(self, a , b):
        print("I am a constructor of class, automatically called")
        self.first_num = a
        self.sec_num = b

    def getdata(self):
        print("I am a method of class")

    def summation(self):
        return self.first_num + self.sec_num + self.num



# calc = Calculator()
# calc.getData()
# print(calc.num)
calc1 = Calculator(10, 20)
print(calc1.summation())
