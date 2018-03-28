numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def factor(x, y=2):
    return x ** y


def args(x, *args):
    print(x)
    for arg in args:
        print("arg is: ", arg)


def kwargs(**kwargs):
    if kwargs is None:
        print("No kwargs")
    else:
        for key, value in kwargs.items():
            print("%s is %s" %(key, value))


add = add(1, 2)
print(add)
sub = subtract(2, 1)
print(sub)
mul = multiply(34, 646)
print(mul)
factored = factor(4, 4)
print(factored)
args(4, 5, 7, 9)
kwarg_dict = {"Name": "Python", "Number": 1, "list": [1, 2, 3]}
kwargs()
kwargs(**kwarg_dict)