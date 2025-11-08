slope1 = (10-2)/(6-2)
slope2 = 2
print(slope1 == slope2)
x=2
y= x**2 + 6*x + 9
print("The value of y is:", y)  

print(len('python') != len('dragon'))
print('jargon' in 'I hope this course is not full of jargon.')
print('on' not in 'jargon' and 'python')

Length_of_python = float(len('python'))
Length_of_PythonString = str(Length_of_python)
print(type(Length_of_PythonString))   

num = int(input('Enter a number: '))

print('is number even:', num % 2 == 0)

print(7//3 == int(2.7))

print(type('10') == type(10))   

print(int(float('9.8'))  == 10)

Hours = int(input("Enter hours: "))
Rate_per_hour = int(input("Enter rate per hour: "))
print("Your weekly earning is: ", Hours * Rate_per_hour)    

NumberOfYears = int(input('Enter number of years you have lived:'))
print("You have lived for ", NumberOfYears * 365 * 24 * 60 * 60, " seconds.")

for i in range (1,6):
    print(i, 1, i, i**2, i**3)