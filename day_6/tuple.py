tuple = ()
brothers = ('Lackó', 'Attila', 'Ádám')
sisters  = ('Alissa', 'Veronica', 'Zsuzsi')
siblings = brothers + sisters
family_members = list(siblings)
family_members.append('Laci')
family_members.append('Eszta')
fruits = ('Apple', 'Banana')
vegetables = ('Tomato', 'Potato')
animals = ('Bird', 'Rabbit')
food_stuff_tp = fruits + vegetables + animals
food_stuff_lt = list(food_stuff_tp)
middle_stuff = food_stuff_tp[2:4]
first_three = food_stuff_lt[0:3]
last_three = food_stuff_tp[3:]
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
Estonia = 'Estonia' in nordic_countries
Iceland = 'Iceland' in nordic_countries


print(siblings)
print(len(siblings))
print(family_members)
print(family_members[:6])
print(family_members[6:])
print(food_stuff_tp)
print(middle_stuff)
print(first_three)
print(last_three)
print(Estonia)
print(Iceland)

del food_stuff_tp