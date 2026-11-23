it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

it_companies.add('Twitter')
itcomp = 'OpeanAi', 'Meta', 'Fuck'
it_companies.update(itcomp)
it_companies.remove('Twitter')

joint = A.union(B)
intersection = A.intersection(B)
subset = A.issubset(B)
disjoint  = A.isdisjoint(B)
disjoint2 = B.isdisjoint(A)
joint2 = A.union(B.union(A))
sys_diff = A.symmetric_difference(B)

convert = set(age)
sentence = "I am a teacher and I love to inspire and teach people."
convert_snt = sentence.split(' ')
convert_snt = set(convert_snt)

print(len(it_companies))
print(joint)
print(joint2)
print(intersection)
print(subset)
print(disjoint)
print(disjoint2)
print(sys_diff)
print(len(age), len(convert))
print(convert_snt)

del it_companies, A, B, age


