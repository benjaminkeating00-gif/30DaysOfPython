new_string = ['thirty', 'days', 'of', 'python']
print(' '.join(new_string)) 

new_string2 = ('coding', 'for', 'all')
print(' '.join(new_string2))

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())

print(company.capitalize())
print(company.title())  
print(company.swapcase())

print(company[6:]) 
print(len(company))

print(company.find('Coding') != -1)
print(company.replace('Coding', 'Python'))
print(company.split())

Companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(Companies.split(', '))
print(company[0])
print(company[-1])
print(company[10])

nickname = ''
for i in range (0, len(company)):
    if company[i].isupper():
        nickname += company[i]
print(nickname)

print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))

print('You cannot end a sentence with because because because is a conjunction'.find('because'))
print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))


n = len('because')
because_string = 'You cannot end a sentence with because because because is a conjunction'

# Option B — explicit loop using find (safe when mutating the string)
i = because_string.find('because')
while i != -1:
    because_string = because_string[:i] + because_string[i+n:]
    i = because_string.find('because')

# collapse extra spaces and trim edges
because_string = ' '.join(because_string.split())
print(because_string)

Coding = 'Coding For All'
print(Coding.startswith('Coding'))
print(Coding.endswith('Coding'))

print(' '.join('  Coding For All  '.split()))

print(('30days_of_python'.isidentifier()))
print(('thirty_days_of_python'.isidentifier()))    

print(' # '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius**2
print(f'Radius ={radius}')
print(f'area = 3.14 * {radius} ** 2')
print(f'The area of a circle with radius {radius} is {area} meters square.')

a = 8
b = 6
c = a + b   
print(f'{a} + {b} = {c}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

