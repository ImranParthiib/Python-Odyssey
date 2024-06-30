
elif pass_len > 15:
    pass_len = 15
    print('Password length is limited to 15 characters.')  
new_password = generate_password(pass_len)
print('Your new password:', new_password)
