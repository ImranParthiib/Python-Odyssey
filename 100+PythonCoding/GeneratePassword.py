import string
import random

def generate_password(size):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(size))
    return password   

pass_len = int(input('How many characters in your password? '))
if pass_len < 6:
    pass_len = 6
    print('Password length is limited to 6 characters.')
elif pass_len > 15:
    pass_len = 15
    print('Password length is limited to 15 characters.')  
new_password = generate_password(pass_len)
print('Your new password:', new_password)
