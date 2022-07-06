def getData():
    print("i am now executing as method in class")


class Calculator:
    num = 100

    def __init__(self):
        print("i am called automatically when object is created")


obj = Calculator()
getData()
print(obj.num)
