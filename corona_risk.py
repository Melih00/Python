age = input('Are you a cigarette addict older than 75 years old? (answer as "Yes" or"No")').lower().strip()
chronic = input('Do you have a severe chronic disease (answer as "Yes" or"No")').lower().strip()
immune = input('Is your immune system too weak (answer as "Yes" or"No")').lower().strip()
if age == 'yes' or chronic == 'yes' or immune == 'yes':
    print('You are in risky group')
else:
    print('You are not in risky group')