number1 = 1
number2 = 1
x = 0
the_list = []
while True:
  the_list.append(number1) 
  x = number1
  number1 += number2
  number2 = x
  if x >= 55:
    break
print(the_list)