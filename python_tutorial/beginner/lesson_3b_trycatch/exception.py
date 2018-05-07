

def uncaught_exception_func(num1, num2):
    print(num1 / num2)


def try_catch_done_the_lazy_way(num1, num2):
    try:
        print(num1 / num2)
    except Exception as e:
        print(f'Lazy: You caught a {e} error')


def try_catch_done_the_better_way(num1, num2):
    try:
        print(num1 / num2)
    except ZeroDivisionError as e:
        print(f'Better: You caught a {e} error')


def try_catch_the_full_way(num1, num2):
    try:
        if num1 is 42 or num2 is 42:
            raise Exception
        print(num1 / num2)
    except ZeroDivisionError as e:
        print(f'Full: You caught a {e} error in the first tier')
    except TypeError as e:
        print(f'Full: You caught a {e} error in the second tier')
    except Exception as e:
        print(f'Full: You caught a {e} error in the last tier')

def raise_exception_way(num1):
    try:
        if num1 is 12:
            raise NameError('hello')
        if num1 != 12:
            raise NameError('HiThere')
    except NameError as e:
        print('An exception flew by!')
        print(f'Raise: You caught a {e} error in the last tier')


try_catch_done_the_lazy_way(10, 2)
try_catch_done_the_lazy_way(23.5, 2)
try_catch_done_the_lazy_way(20, 20.0000001)
try_catch_done_the_lazy_way(20, 0)
print('---------------------')

try_catch_done_the_better_way(10, 2)
try_catch_done_the_better_way(23.5, 2)
try_catch_done_the_better_way(20, 0)
print('---------------------')

try_catch_the_full_way(12, 2)
try_catch_the_full_way(12, 0)
try_catch_the_full_way('jim', 0)
try_catch_the_full_way([0, 2], 0)
try_catch_the_full_way(42, 42)
print('---------------------')

raise_exception_way(12)
raise_exception_way(24)
print('---------------------')

uncaught_exception_func(12, 2)
uncaught_exception_func(12, 2)


print("All errors were caught")