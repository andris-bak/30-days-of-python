age = int(input('How old are you?: '))
if(age >= 18):
    print('You are old enough to drive!')
elif(age < 18):
    print(f'You still need {18-age} years before you can learn how to drive')