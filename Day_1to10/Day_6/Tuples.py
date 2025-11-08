NewTuple = ()
Brothers = ('chris', 'drew')
Sisters = ('Jacqueline',)
Siblings = Brothers + Sisters

print(len(Siblings))
print(Siblings)

Siblings = list(Siblings)
family_members = ['Andrew', 'Edward']
Siblings += family_members

print(tuple(Siblings))

Siblings = list(Siblings)
Siblings = Siblings[0:-2]
print(tuple(Siblings))

fruits = ('apple', 'banana', 'cherry', 'date')
vegatables = ('carrot', 'broccoli', 'spinach', 'kale')
food_stuff_tp = fruits + vegatables
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)

if len(food_stuff_lt) % 2 == 0:
    del food_stuff_lt[len(food_stuff_lt)//2 - 1:len(food_stuff_lt)//2 + 1]
else: del food_stuff_lt[len(food_stuff_lt)//2]
print(food_stuff_lt)

food_stuff_tp = food_stuff_tp[3:-3]
print(food_stuff_tp)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)