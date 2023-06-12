#1
def sumn(n):
    final_sum = 0
    for x in range(n + 1):
        final_sum = final_sum + x
        # final_sum += x
    return final_sum

test_data = 8 #36
test_result = sumn(test_data)
print(test_result)

#2
def find_max(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    return c

test_result = find_max(40, 50, 60) #60
print(test_result)


reminder = 208 //10

print(reminder)


def count_odd_even(n):
    odds = 0
    evens = 0

    while n != 0:
        current_digit = n % 10
        if current_digit % 2:
            odds += 1
        else:
            evens += 1
            n = n // 10

            print(f"Evens: {evens}, Odds{odds} ")

        test_number = 15049 # odds: 1, 5, 9 evens: 4, 0
        count_odd_even(test_number)

