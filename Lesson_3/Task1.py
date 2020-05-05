s = input()

if len(s) >= 2 and " " not in s:
    result0 = s[0:2] + s[-2:]
    print(result0)
if s[0] == " " and s[-1] == " " and len(s) > 1:
    s.strip()
    result1 = s[1:3] + s[-3:]
    print(result1)

