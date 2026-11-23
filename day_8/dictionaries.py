dog = {'color': 'gold',
       'breed': 'golden retriever',
       'legs' : 'four',
       'age'  : '3'}

student = {'first_name': 'Alice',
           'last_name' : 'Manhatann',
           'gender'    : 'female',
           'age'       : '20',
           'maritial status' : 'single',
           'skills'    : ['writing', 'cooking', 'video editing', 'drawing', 'painting'],
           'country'   : 'USA',
           'city'      : 'New York City',
           'address'   : {
                'street'  : '5th Avenue',
                'zipcode' : '122234'              
           }
}

student['skills'].append('gaming')
student['skills'].append('scouting')

print(dog)
print(len(student))
print(type(student['skills']))
print(student['skills'])
print(student.keys())
print(f'\n{student.values()}')
print(f'\n{student.items()}')

student.pop('gender')
print(f'\n{student}')

del dog
#print(dog)
