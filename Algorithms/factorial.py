# When User enters a number, its factorial is displayed.
n = 6 #720
result  = 1
saved_n = n
while n > 0:
    result = result * n
    n = n -1

print(f'The factorial of {saved_n} = {result}')

