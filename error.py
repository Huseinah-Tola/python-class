usr_input = input('Enter a number: ')
if not usr_input.isnumeric():
    print('Not a number')
else:
    try:
        print(usr_input/0)
        result = int(usr_input)
        print(result/29)
        result
    except AssertionError as e:
        print('Error only integer number is accepted', e)