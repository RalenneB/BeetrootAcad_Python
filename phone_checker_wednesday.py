"""
Homework. Advanced level

The valid phone number program.

Create a program that checks if a string is in the proper
format for a phone number.
The program should check that the string contains only
numeric characters and is only 10 characters long.
Print a suitable message depending on the outcome of the
string evaluation.
"""
phone_number = '1234589'  # aiaidigri3


def phone_validator(number):
    if type(number) != int:
        if len(number) == 10 and number.isdigit():
            print('Valid number!')
        elif len(number) == 10 and not number.isdigit():
            print('There should be only numbers, not letters or other special characters!')
        elif len(number) != 10 and not number.isdigit():
            print('The number should have 10 digits and to not contain other characters!')
        elif len(number) != 10 and number.isdigit():
            print('The number should have 10 digits, no more, no less!')
        else:
            print('Please check again the number provided')

    elif type(number) == int:
        convert = str(number)
        if len(convert) == 10:
            print('Valid number')
        else:
            print('The number should have 10 digits!')


if __name__ == '__main__':
    phone_validator(phone_number)


