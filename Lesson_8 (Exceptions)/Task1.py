def oops():
    raise KeyError

def trapper():
    try:
       a = [1, 2, 3]
       print(a[4])
    except:
        oops()

trapper()
