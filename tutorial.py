# print('vini')

# X = 'hello'
# print (X)
# X = 'bye'
# print (X)


# ---------------------------- #


# print('Hello, what is your name?')
# name = input()
# print('Hello,',name)

# num1 = 10
# num2 = 10
# print(num1 + num2)

# print('Pick a number: ')
# num1 = input()
# print('Pick another number: ')
# num2 = input()

# X = int(num1) + int(num2)
# print (X)


# ---------------------------- #


# print (3 > 2)

# print (2 > 3)

# print ('hello' == 'helo')

# print ('hello' != 'helo')

# print ('hello' == 'Hello')


# ---------------------------- #


# if True:
#     print('yes')

# age = input('Qual é a sua idade: ')

# if int(age) >= 18:
#     print("You're able to drink and drive")
# else:
#     print("You're not able to drink and drive")

# height = input('Qual é a sua altura (em metros)?: ')

# if float(height) <= 1:
#     print("you're can not drive, too small")
# elif float(height) >= 2:
#     print("you're can not drive, too tall")
# else:
#     print("you're can drive!")


# ---------------------------- #


# x = 3
# y = 2

# if x == y or x + y == 5:
#     print('hello')

# if not(x == y or x + y == 5):
#     print('hello')
# else:
#     print('sad')

# if x == 3:
#     if y == 2:
#         print('x = 3, y = 2')
#     else:
#         print('x = 3, y != 2')
# else:
#     print('x != 3')


# ---------------------------- #


# for x in range(0,10): # start, stop, step
#    print(x)


# ---------------------------- #


# x = True

# while x:
#     password = input('Password: ')
#     if password == 'stop':
#         break

# y = 0

# while y <= 5:
#     print(y)
#     y = y + 1


# ---------------------------- #


# fruits = ['apple', 'pear']

# print(fruits)

# fruits.append('banana')
# fruits.append('strawberry')

# print(fruits)

# fruits[1] = 'melon'

# print(fruits)

# position = (2, 3)

# print(position)


# ---------------------------- #


# fruits = ['apple', 'banana', 'pears','strawberry','melon']

# for fruit in fruits:
#     if fruit == 'pears':
#         print(fruit)
#     else:
#         print('not pears')

# for x in range(len(fruits)):
#     if fruits[x] == 'pears':
#         print(fruits[x])
#     else:
#         print('Not pears')



# ---------------------------- #

text = input('Input someting: ')

print(text.strip())

print(len(text))

print(text.lower())

print(text.upper())

print(text.split('.'))