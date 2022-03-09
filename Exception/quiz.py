num1 = 100
num2 = 0
try:
    result = num1/num2
    print(result)
except ZeroDivisionError:
    print("Zero Division Error Occurred")


def division(a, b):
    try:
        return int(a)/b
    except TypeError:
        print("Type error")
    except ValueError:
        print("Value error")
    finally:
        print("Finally")
    print("Done")


division('A', 10)


def find_sum(a, b):
    try:
        print(a+c)
    except NameError:
        print("Function name error")
    finally:
        print("Sum finally")


try:
    find_sum(12, 13)
except NameError:
    print("Invocation name error")
finally:
    print("Invocation finally")
