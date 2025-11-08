# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['microsoft', 'Linkedin', 'Snapchat'])
print(it_companies)
it_companies.remove('IBM')
print(it_companies)

C = (A.union(B))
print(C)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))

del A
del B

print('\n\n\n')


Ages = [19, 22, 24, 20, 25, 26]


print(len(Ages))
Ages = set(Ages)
print(len(Ages))

Sentence = set("I am a teacher and I love to inspire and teach people.".split())
print(Sentence)



NewSentence = set()
while len(Sentence) != 0:
    Words = Sentence.pop()
    if Words not in NewSentence:
        NewSentence.add(Words)

print(NewSentence)
print(len(NewSentence))