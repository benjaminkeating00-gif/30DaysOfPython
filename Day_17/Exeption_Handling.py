def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*first_five, es, ru = names
print(f'{first_five}, {es}, {ru}') # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']