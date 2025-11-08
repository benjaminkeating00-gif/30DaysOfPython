person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    skills = (person['skills'])
    print(skills[len(skills)//2])

if 'skills' in person and 'Python' in person['skills']:
    print(person['skills'])



# determine developer title
skills = set(person.get('skills', []))

if skills == {'JavaScript', 'React'}:
    print('He is a front end developer')
elif {'React', 'Node', 'MongoDB'}.issubset(skills):
    print('He is a fullstack developer')
elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
    print('He is a backend developer')
else:
    print('unknown title')

# married and country info
if person.get('is_marred') and person.get('country') == 'Finland':
    print(f"{person.get('first_name')} {person.get('last_name')} is married and lives in {person.get('country')}.")


