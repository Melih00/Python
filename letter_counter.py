sentence = input('enter the sentence... ')
dic1 = {}
for i in sentence:
  dic = {i:sentence.count(i)}
  dic1.update(dic)
  dic = {}
print(dic1)