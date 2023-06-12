# User inputs two numbers. One number is assigned to a variable, the other number is assigned to another variable.
# The task is to invert the variables, so that the first variable contains the second number, while the first number
# is in the second variable.

# code here
a = 4
b = 3

# 0(1)
print(f'a = {a}')
print(f'b = {b}')
# 1
# temp = a # 1
# a = b # 2
# b = temp # 3

temp = a
a = b
b = temp
# 2
 # a, b = b, a

# 3
 # a = a + b
 # b = a - b
# a = a - b

print(f'a = {a}')
print(f'b = {b}')

