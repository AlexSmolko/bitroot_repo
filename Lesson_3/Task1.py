s = input()
result = ''
if len(s) >= 2:
    result = s[0:2] + s[-2:]
    print(result)
else:
    print(s)