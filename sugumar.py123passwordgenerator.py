import random
import string

def generate_password(length=12,use_digits=True,use_special=True):
    letters = string.ascii_letters
    digits = string.digits if use_digits else ''
    special = string.puntuation if use_special else ''
    characters = letters+digits+special
    
    if not characters:
        return "Error:No character types selsected."
    
    password =''.join(random.choice(characters)for _ in range(length))
    return password

print("===Password Generator ===")
length = int(input("enter password length(e.g.12):"))
use_digits = input("Include digits?(y/n):").lower()=='y'
use_special = input("Include special characters?(y/n):").lower()=='y'
password = generate_password(length,use_digits,use_special)
print(f"\nGenerate Password: {password}")
