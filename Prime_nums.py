number = input('enter a number to see if its a prime number : ')
b = False
for i in range(2,int(number)):
  if int(number) % i == 0:
   b = True
   break
if b == True or number == '1' :
  print('Your number is not Prime')
else:
  print('Your number is Prime')