ph_number = input()
if ph_number.isdigit():
    if len(ph_number) <= 10:
        print(f'Your telephone number is: {ph_number}')
    else:
        print('Your telephone number is longer than need')
elif ph_number.isalpha():
    print('Your input it\'s letters. Input digits instead letters, please')
else:
    print('You have some letters in your number. Please change it to digit(s)')