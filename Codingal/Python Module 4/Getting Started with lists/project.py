num = int(input("Enter a number: "))
odd_list = []
even_list = []
for i in range(1, num + 1):
    if i % 2 != 0:
        odd_list.append(i)
    else:
        even_list.append(i)
print("Odd numbers:", odd_list)
print("Even numbers:", even_list)
fruits = ["apple", "banana", "mango", "orange"]
new_list = []
for fruit in fruits:
    capitalized = fruit.capitalize()
    new_list.append(capitalized)
print("Original list:", fruits)
print("Updated list:", new_list)