list = []
list2 = ['alma', 'asda', 'aaa', 'asdas', 'sda'] # 5 db
first_item = list2[0]
middle_item = list2[2]
last_item = list2[-1]

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
first_company = it_companies[0]
middle_company = it_companies[4]
last_company = it_companies[-1]
it_companies.sort()
it_companies2 = it_companies.copy()
it_companies3 = it_companies.copy()
it_companies4 = it_companies.copy()

remove_comp  =  it_companies.copy()
remove_comp2 =  it_companies.copy()
remove_comp3 =  it_companies.copy()
remove_comp4 =  it_companies.copy()

print(list2)
print(len(list2))
print(first_item, middle_item, last_item) # változás előtt
print(f'\n{it_companies}') # változás előtt
print(len(it_companies))
print(first_company, middle_company, last_company)

it_companies.reverse()
print(it_companies)


it_companies[0] = 'Meta' # változás után
it_companies.append('OpenAI')
it_companies.insert(4, 'Asus')
it_companies[0] = it_companies[0].upper() # vagy it_companies[0] = 'Meta'.upper()
it_companies = '#'.join(it_companies)
check = 'IBM' in it_companies
it_companies2 = it_companies2[:3]
it_companies3 = it_companies3[-3:]
it_companies4 = it_companies4[3]

remove_comp.pop(0)
remove_comp2.pop(3)
remove_comp3.pop(-1)
remove_comp4.clear()

print(f'\n{it_companies}')
print(check)
print(it_companies)
print(it_companies2)
print(it_companies3)
print(it_companies4)

print(remove_comp)
print(remove_comp2)
print(remove_comp3)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
full_stack = front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(5, 'SQL')

print(front_end)
print(full_stack)

print('----------------------------LEVEL2----------------------------')
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
minimum = min(ages)
maximum = max(ages)
ages.append(minimum)
ages.append(maximum)
median = ((ages[5] + ages[6])/2)
avg = sum(ages)/12
range = maximum - minimum
compare = abs(minimum - avg) == abs(maximum - avg)
print('--------------------------------------------------------------')
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
middle = len(countries) // 2
left  =  countries[0:98]
right =  countries[98:]
excercise = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country = excercise[0]
second_country = excercise[1]
third_country = excercise[2]
scandavic_countries = excercise[3:]
print(countries[middle])
print(scandavic_countries)
