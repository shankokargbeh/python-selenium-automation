def count_odd_even(n):
    odds = 0
    evens = 0

    while n != 0:
current_digit  = n % 10

    if current_digit % 2:
        odds += 1
    else:
        evens += 1
        n = n // 10

        print(f"Evens: {evens}, Odds: {odds}")

       test_number = 18534 # Odds: 1, 3, 5 # Evens: 4, 8
    count_odd_even(test_number)