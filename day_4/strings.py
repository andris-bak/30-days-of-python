coding = ['Thirty', 'Days' ,'Of', 'Python']
result1 = ' '.join(coding)
print(result1)

coding2 = ['Coding', 'For', 'All']
result2 = ' '.join(coding2)
print(result2) 

company = "Coding For All"
strip = '   Coding For All      '
challenge1 = '30DaysOfPython'
challenge2 = 'thirty_days_of_python'
split = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
abbreviation1 = 'PFE'
abbreviation2 = 'CFA'
sentence = 'You cannot end a sentence with because because because is a conjunction' 
list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
list2 = '# '.join(list)
radius = 10
area = 3.14 * radius ** 2

print(len(company))
print(f'\n{company}')
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[6:])
print(company.find('Coding'))
print(company.index('Coding'))
print(company.replace('Coding', 'Python'))
print(company.replace('All', 'Everyone'))
print(company.split())
print(split.split(', '))
print(company[0])
print(company.rindex('l'))
print(company[10])
print(abbreviation1)
print(abbreviation2)
print(company.index('C'))
print(company.index('F'))
print(company.rindex('i'))
print(sentence.index('because'))
print(sentence.rindex('because'))
print(sentence[31:55])
print(sentence[0:30],sentence[55:71])
print(company.startswith('Coding'))
print(company.endswith('coding'))
print(strip.strip(' '))
print(challenge1.isidentifier())
print(challenge2.isidentifier())
print(list2)
print('\nI am enjoying this challenge.\nI Just wonder what is next.')
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')
print(f'The area of this with {radius} is {area} meters square')
print('\n{} + {} = {}'.format(8,6, 8+6))
print('{} - {}  =  {}'.format(8,6,8-6))
print('{} * {}  =  {}'.format(8,6,8*6))
print('{} / {}  =  {}'.format(8,6,8/6))
print('{} % {}  =  {}'.format(8,6,8%6))
print('{} // {} =  {}'.format(8,6,8//6))
print('{} ** {} =  {}'.format(8,6,8**6))
