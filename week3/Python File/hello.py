# print('Hello, Sparta')
# a=3
# b=a
# a=a+1
# print (b)

#num1 = a*b
#print (num1)

# a_list = []
# a_list.append(1)
# a_list.append([2,3])
# a_list.append(5)
# print (a_list)



# people = [{'name':'bob','age':20},{'name':'carry','age':38}]
# person = {'name':'john','age':7}
# people.append(person)
# print()

# def f(x):
# 	return 2*x+3

# def sum(a,b,c):
#     return a+b+c

# def mul(a,b):
#     return a*b

# result = sum(1,2,3) + mul(10,10)
# print(result)

# result = 0
# for num in num_list:
#         result += 1
# print(result)
# print (sum(num_list))

# pear_count = count_fruits('Pear')
# print(pear_count) # 3
# count = 0
# for fruit in fruits:
#     if fruit == 'Apple':
#         count +=1
# print(fruit)

# def is_adult(age):
#     if age>20:
#         print ('Adult')
#     else :
#         print ('Youth')
# is_adult(30)


# fruits = ['Apple','Pear','Pear','Banana','Watermelon','Tangerine','Strawberry','Apple','Pear','Watermelon']

# count = 0
# for fruit in fruits:
#     if fruit == 'Apple':
#         count +=1
# print(fruit)

# def count_fruits(target):
# 	count = 0
# 	for fruit in fruits:
# 		if fruit == target:
# 			count += 1
# 	return count

# watermelon_count = count_fruits('Watermelon')
# print(watermelon_count) # 2

# pear_count = count_fruits('Pear')
# print(pear_count) # 3



# people = [
#     {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
#     {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
#     {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
#     {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
# ]

## Let's print everyone's name and age.
# for person in people:
# print(people['name']['smith']['score']['science'])


# def get_science(myName):
#     for person in people:
#         if person['name'] == myName:
#             return person['score']['science']
#     return 'No such name exists'


# print(get_science('smith'))

# num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
# print(max(num_list)) 


# def check_gender(pin):
#     num = int(pin.split('-'[1][0]))
#     if num % 2 == 0:
#         print ('female')
#     else:
#         print ('male')
