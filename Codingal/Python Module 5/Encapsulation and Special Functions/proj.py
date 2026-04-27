class Reverse:
    def __init__(self, s=""):
        self.s = s
    def reverse_string(self):
        return self.s[::-1]
user_input = input("Enter a word: ")
reverser = Reverse(user_input)
print(f"Reversed string: {reverser.reverse_string()}")