# main.py file
import string
import random
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh\

def random_printable():
    i = 0
    random_string = ''
    while i < 10:
        random_string += random.choice(string.ascii_letters + string.digits)
        i += 1
    print('Here is the random string:', random_string)

random_printable()

def user_id_gen_by_user():
    NumChars = int(input('Enter number of characters: '))
    NumIds = int(input('Enter number of IDs to generate: '))
    random_string = ''
    for count in range(NumIds):
        random_string = ''
        for i in range(NumChars):
            random_string += random.choice(string.ascii_letters + string.digits)
        print(random_string)
        i += 1
user_id_gen_by_user()


def rgb_color_gen(name, number):
        color_list = []
        for count in range(number):
                sub_color = ''
                for i in range(3):
                    our_random_num = random.randint(0, 255)
                    sub_color += (f'{our_random_num},')
                color_list.append((f'rgb({sub_color})'))
        color_list = tuple(color_list)
        print('#rgb', (color_list))
        return color_list



def random_printable1(name, number):
    hexa_list = []
    count = 0
    for count in range(number):
        random_string = ''
        for i in range(6):
            random_string += random.choice(string.hexdigits)
        hexa_list.append('#' + random_string)
    print(hexa_list)
    return hexa_list





def hexa_or_rbg(name, number):
    if name == 'hexa':
        (random_printable1(name, number))
    else:
        (rgb_color_gen(name, number))

hexa_or_rbg('hexa', 3)
hexa_or_rbg('rgb', 3)

def shuffle_list(mylist):
    random.shuffle(mylist)
    return mylist

print(shuffle_list([1, 3, 3,]))


def alot_of_ints():
    int_list = []
    while len(set(int_list)) < 7:
        int_list.append(random.randint(0, 9))
    int_list = set(int_list)
    return int_list
print(alot_of_ints())