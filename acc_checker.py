name = 'Melih'
password = 'W@12'
username = input('enter your user name ').capitalize()
if name == username:
    print(f'Hello {name}! The password is : {password}')
else:
    print(f'Hello, {username}! See you later.')