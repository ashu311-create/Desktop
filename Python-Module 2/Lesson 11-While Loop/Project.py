num_str = input("Enter a number: ")
digit_count = 0
try:
    num = int(num_str)
    if num < 0:
        num = abs(num)
    if num == 0:
        digit_count = 1
    else:
        while num > 0:
            num //= 10
            digit_count += 1
    print("Total number of digits:", digit_count)
except ValueError:
    print("Invalid input. Please enter a valid integer.")