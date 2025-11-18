def decimal_to_binary(decimal_num):
    """
    Converts a decimal number to its binary representation.
    Args:
        decimal_num: An integer representing the decimal number.
    Returns:
        A string representing the binary equivalent.
    """
    if decimal_num == 0:
        return "0"
    binary_result = ""
    temp_num = decimal_num
    while temp_num > 0:
        remainder = temp_num % 2 
        binary_result = str(remainder) + binary_result
        temp_num //= 2

    return binary_result
try:
    user_input = int(input("Enter a decimal number: "))
    if user_input < 0:
        print("Please enter a non-negative decimal number.")
    else:
        binary_output = decimal_to_binary(user_input)
        print(f"The binary representation of {user_input} is: {binary_output}")
except ValueError:
    print("Invalid input. Please enter an integer.")
