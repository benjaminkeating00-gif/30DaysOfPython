age = int(input('Enter your age: '))
if age >= 18: print('You are old enough to drive.')
else: print(f'You need {18 - age} more years to drive.')

my_age = 19
if my_age > (age + 1): 
    print(f'I am {my_age - age} years older than you.')
elif my_age - age == 1:
    print('I am 1 year older than you.')
elif my_age == age:
    print('We are the same age.')

elif my_age < (age - 1): 
    print(f'I am {age - my_age} years younger than you.')
elif my_age - age == -1:
    print('I am 1 year younger than you.')

print('\n' * 2)
number1 = int(input('Enter number 1: '))
number2 = int(input('Enter number 2: '))

difference_nums = number1 - number2
if difference_nums > 0:
    print(f'{number1} is greater than {number2}.')
elif difference_nums == 0:
    print(f'{number1} is equal to {number2}.')
else:
    print(f'{number1} is less than {number2}.')

print('\n' * 2)

score = int(input('Enter your score (0-100): '))
if score >= 80:
    print('You got an A!')
elif score >= 70 and score < 79:
    print('You got a B!')
elif score >= 60 and score < 69:
    print('You got a C!')
elif score >= 50 and score < 59:
    print('You got a D!')
else:
    print('You got an F.')

   
date = input('Enter the date (xx/xx/xxxx): ')

if len(date) == 10 and date[2] == '/' and date[5] == '/':
    month = int(date[0:2])
    if month == 12 or month < 3:
        print("Winter")
    elif 3 <= month < 6:
        print("Spring")
    elif 6 <= month < 9:
        print("Summer")
    else:
        print("Fall")
else:
    print("Wrong format. Please use xx/xx/xxxx (for example, 04/27/2025).")


print('\n' * 2)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ')
if fruit not in fruits:
    fruits.append(fruit)
    print('Fruit added to the list.')
else:
    print('Fruit already exists in the list.')


print('\n' * 2)
