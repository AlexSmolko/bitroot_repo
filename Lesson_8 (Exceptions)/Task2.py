def advanced_trapper():
    a, b = (input().split())
    c = int(a) ** 2 / int(b)
    print(c)
    return c


try:
    advanced_trapper()
except ValueError as te:
        print("This values are not numbers. {0}".format(te))
except ZeroDivisionError:
       print('value "b" is zero and because "a" can not be divided')
