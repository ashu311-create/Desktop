import random
import string
def generate_password(length=10):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    all_chars = lower + upper + digits
    password_list = random.sample(all_chars, length)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password
print("Generated Password:", generate_password(12))