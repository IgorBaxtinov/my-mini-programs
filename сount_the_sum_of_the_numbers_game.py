import random
import time


n1 = random.randint(0,100)
n2 = random.randint(0,100)


print(f'{n1} + {n2} = ', end='')
answer = int(input())

if n1 + n2 == answer:
    print('Правильный ответ!')
else:
    print('ошибка')

time.sleep(40)







