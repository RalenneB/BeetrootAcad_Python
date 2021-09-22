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
phone_number = '1234567890'  # aiaidigri3


def phone_validator(number):
    if type(number) != int:
        if len(number) == 10:
            try:
                number = int(number)
                print('Valid number')
            except ValueError:
                print('Please provide an actual number')
        elif len(number) != 10 and not number.isdigit():
            print('The number should have 10 digits only, not letters!')
        elif len(number) != 10 and number.isdigit():
            print('The number should have 10 digits, no more, no less!')
        else:
            print('Please check again the number provided') #should never run

    elif type(number) == int:
        convert = str(number)
        if len(convert) == 10:
            print('Valid number')
        else:
            print('The number should have 10 digits!')


if __name__ == '__main__':
    phone_validator(phone_number)


