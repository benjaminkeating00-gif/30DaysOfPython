paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
import re 
from collections import *


list_of_words = re.findall(r'\b\w+\b', paragraph.lower())

print(list_of_words)
counted_words = Counter(list_of_words)
print(counted_words.most_common(5))

points = ['-12', '-4', '-3', '-1', '0', '4', '8']
points =[int(number) for number in points]
print(points)

def range_of_points(): 
    print(max(points) - min(points))

range_of_points()  

print('\n'*2)

regex_pattern = r'^[A-Za-z_]\w*$'
def is_valid_variable(variable):
    if re.match(regex_pattern, variable):
        return True
    return False

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True



sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''


regex_pattern3 = r'[^\w\s]'
matches = re.sub(regex_pattern3, '', sentence)
print(matches)

list_of_words2 = re.findall(r'\b\w+\b', matches.lower())

print(list_of_words2)
counted_words = Counter(list_of_words2)
print(counted_words.most_common(5))