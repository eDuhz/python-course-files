__author__ = 'eduh'

ip = str(input('Enter an IP'))
list_of_numbers = []
number = ''


if ip == '' or ip == ' ':
    print('blank input')
elif ip[0] == '.' or ip[-1] == '.':
    print('a ip never starts or ends with a dot')
else:
    for char in ip:
        if char == '.':
            list_of_numbers.append(number)
            number = ''
        elif char in '.0123456789':
            number+=char
        else:
            number = ''
            print('invalid number')
            list_of_numbers = []
            break

    list_of_numbers.append(number)

    for each_number in list_of_numbers:
        print('The number '+each_number+' has '+ str(len(each_number)) + ' numbers')