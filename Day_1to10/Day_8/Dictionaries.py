dog ={'name': 'Jazzy', 'age': 7, 'breed': 'lab', 'color': 'Golden', 'legs': 4}

student = {
    'first_name': 'Benjamin',
    'last_name': 'Jones',
    'gender': 'Male',
    'age': 19,
    'marital_status': 'Single',
    'skills': ['Python', 'Git', 'SQL'],
    'country': 'USA',
    'city': 'Springfield',
    'address': '9709 Timber Ridge Pass'
}

print(student)
print(len(student))
print(type(student.get('skills')))

student['skills'].extend(['JavaScript','Reading'])
print(student['skills'])

student.keys()
print(student.keys())
student.values()
print(student.values())

print('\n' * 3)
student.items()
print(student.items())

del student['marital_status']
print(student)

del student 
