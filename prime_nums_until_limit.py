limit = int(input('enter the limit number : '))
prime_nums = []
counter = 0
for i in range(1,limit):
  boo = False  
  for j in range(2,i):
    if i % j == 0:
      boo = True
      break
  if boo == False and i != 1:
    prime_nums.append(i)
print(prime_nums)