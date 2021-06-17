a = int(input('Введите ширину листа: '))
counter_a = 0
b = int(input('Введите длину листа: '))
counter_b = 0
while a > 12:
  for num in range(a, 12 , - (a // 2)):
    counter_a +=1
    a //= 2
print('По ширине нужно сложить', counter_a, 'раз')
while b > 12:
  for num in range(b, 12 , - (b // 2)):
    counter_b +=1
    b //= 2
print('По длине нужно сложить', counter_b, 'раз')