test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print("Test Dictionary:", test_dict)
key = input("Enter the key to check its frequency: ")
if key in test_dict:
    print("Frequency of", key, "is:", test_dict[key])
else:
    print("Key not found in the dictionary.")