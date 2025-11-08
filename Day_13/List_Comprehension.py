
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive_even_numbers = [num for num in numbers if num > 0 and num % 2 == 0]
print(positive_even_numbers)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list =[num for row1 in list_of_lists for row in row1 for num in row]
print(flattened_list)

fat_ah_list = [(i, i**1, i, i**2, i**3, i**4, i**5) for i in range(0,10)]
for item in fat_ah_list:
    print(item)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
meant_to_be_flattened_countries = [(tupley[0].upper(), tupley[0][0:3].upper(), tupley[1].upper()) for row in countries for tupley in row]
print(meant_to_be_flattened_countries)

our_flattened_countries = [{'country': tupley[0], 'capital': tupley[1]} for row in countries for tupley in row]
print(our_flattened_countries)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [(f'{tupley[0]} {tupley[1]}') for row in names for tupley in row]
print(full_names)

find_m_and_b = lambda y, x, m, b: ((y - b) / x, y - m * x)
result = find_m_and_b(10, 2, 2, 4)
print(result)