my_age = 21
age = int(input('How old are you?: '))

if(age >= 18):
    print('You are old enough to drive!')
elif(age < 18):
    print(f'You still need {18-age} years before you can learn how to drive')

if(age == my_age):
    print("We are the same age!")
elif(age-my_age > 1):
    print(f"You are {age-my_age} year(s) older than me")
else:
    print(f"You are {my_age-age} year(s) younger than me!")
    