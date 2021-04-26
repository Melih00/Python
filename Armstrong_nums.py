number = input('enter a number to see if its Armstong : ')
length = len(number)
nums = set('1234567890')
final = 0
if set(number) & nums == set(number) :
  for i in number:
    number2 = int(i)**length
    final += number2
  if final == int(number):
    print(f'{number} is an Armstrong number')
  else:
    print(f'{number} is not an Armstrong number')
else:
  print("It is an invalid entry. Don't use non-numeric, float, or negative values!")