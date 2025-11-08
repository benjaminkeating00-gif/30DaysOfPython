list0 = []
list1 = [1, 2, 3, 4, 5]
print(len(list1))
print(list1[0::2])

mixed_data_types = ['Benjamin', 19, 5.6, False, '9709 Timber Ridge Pass']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0::(int((len(it_companies)/2)))])

del it_companies[3]
print(it_companies)

it_companies = it_companies + ['Nvidia']
print(it_companies)

(it_companies.insert(3, 'Twitter'))
print(it_companies)

it_companies[1] = it_companies[1].upper()
print(it_companies)

print('#; '.join(it_companies))

does_exist = 'Twitter' in it_companies
print(does_exist)

it_companies.sort()
print(it_companies)

it_companies.reverse()

print(it_companies[:-3])
print(it_companies[-4::-1])

print('')
print(it_companies)
print(it_companies[0:((len(it_companies)//2)-1)]+it_companies[len(it_companies)//2+1:])

del it_companies[len(it_companies)-1]

it_companies.clear()
print(it_companies)
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end

print(full_stack)
# insert two items at the boundary between front_end and back_end
idx = len(front_end)
full_stack.insert(idx, 'Python')    # insert 'Python' at index 5
full_stack.insert(idx + 1, 'SQL')   # insert 'SQL' right after
print(full_stack)