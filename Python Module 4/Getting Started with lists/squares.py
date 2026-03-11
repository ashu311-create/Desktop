start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
even_squares = []
odd_squares = []
for num in range(start, end + 1):
    square = num ** 2
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)
print(f"Even squares: {even_squares}")
print(f"Odd squares: {odd_squares}")