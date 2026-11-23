#Day 2: 30 Days of python programming
import math 

first_name = 'Drew'
last_name  = 'Matt'
full_name  = 'Drew Matt'
country    = 'Hungary'
city       = 'Eger'
age        =  21
year       =  2026
is_married =  False
is_true    =  True
is_light_on = True
hell, nah = 'hell', 'nah' 

num_one = 5
num_two = 4
total = num_one + num_two
diff  = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
radius = 30
area_of_circle = (radius ** 2) * math.pi
circum_of_circle = 2 * radius * math.pi
print(area_of_circle)
print(circum_of_circle)

# Erre ránézni hogy miként lehetne jobban csinálni
radius = int(input('Give me the radius! '))
area_of_circle = (radius ** 2) * math.pi
print(area_of_circle)


print(nah)

#Exercises level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(hell))
print(type(nah))

print(len(first_name))
print('Length of my first name:',len(first_name), '\nLength of my last name:', len(last_name))

first_name = input('\nTell me your name: ')
last_name = input('Tell me your family name: ')
country = input('Tell me your country: ')
age = int(input('Tell me your age: '))

print(f'\n{first_name}')
print(last_name)
print(country)
print(age)
