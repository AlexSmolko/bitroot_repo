def oops():
    raise IndexError

def trapper():
    try:
        oops()
    except IndexError:
       print("Cathed")
        
trapper()

"""So, when we replace the IndexError with KeyError, but not change the condition and it will be the same 
that will lead to raising of the IndexError, it will print the messages: 'IndexError: list index out of range'
and the next:
'During handling of the above exception, another exception occurred:' 
And the next message will be: 'raise KeyError' and on the next line: 'KeyError' """

