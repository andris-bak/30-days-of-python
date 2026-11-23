import math
age = 21
height = 1.65
complex = 1 + 1j

base = int(input('Enter base: '))
t_height = int(input('Enter height: '))
area = print(f'The area of the triangle is: ' , 0.5 * base * t_height)

side_a = int(input('\nEnter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
perimeter = print(f'The perimeter of the triangle is: ', side_a + side_b + side_c)

r_length =  int(input('\nGive me a rectangles length: '))
r_width  =  int(input('Give me a rectangles width:  '))
r_area   =  print(f'The rectangle`s area is: ',  r_length*r_width)
r_perimeter = print(f'The rectangle`s perimeter is: ',  2*(r_length+r_width))

radius = int(input('\nGive me the radius of a circle: '))
c_area = print(f'The circle`s area: ', math.pi * radius * radius)
c_circumference = print(f'The circle`s circumference: ', 2 * math.pi * radius)

# m = y2-y1/x2-x1
# sqrt((x2-x1)**2+(y2-y1)**2)

# 8-as
slope_8 = 2
x_intercept = 1
y_intercept = -2

# 9-es (2,2) (6,10)
slope_9 =(10-2)/(6-2)
print(f'\nThe slope of the 9th excercise: {slope_9}')
euclidian_9 = print(f'The euclidian distance of the 9th excercise: ', math.sqrt((6-2)**2+(10-2)**2))

print(slope_9 == slope_8)

print((-3)**2+6*(-3)+9)
print(len('python') > len('dragon'))

print('on' in 'python' and 'on' in 'dragon')
print('I hope this course is not full of jargon.' ,'jargon' in 'I hope this course is not full of jargon.')
print('on' not in 'python' and 'on' not in 'dargon')

text = len('python')
float = float(text)
string = str(text)
print(float)
print(string)

print(7//3 == int(2.7))
print(type('10') == type(10))
print(int(9.8) == 10)

hours = int(input('\nEnter hours: '))
rate_per_hour = int(input('Enter the rate of hour: '))
print(f'Your weekly earning is: {hours*rate_per_hour}')

year = int(input('\nEnter number of years you have lived: '))
seconds = 31536000
print(f'You have lived for {year*seconds} seconds')
print('\n1 1 1 1 1' +
      '\n2 1 2 4 8' +
      '\n3 1 3 9 27 '+
      '\n4 1 4 16 64'+
      '\n5 1 5 25 125')