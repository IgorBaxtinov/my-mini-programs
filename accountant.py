# Смысл программы: Вы сидите на кассе и получаете деньги и вносите сумму в программу
# В конце дня после написания слова stop программа должна выдать общую сумму в кассе.

import time
from time import sleep

print ('*' * 20)
print ("КАССА")
print ('*' * 20)

total = 0
n = 0

while True:
    n = input("Введите сумму чека: ")
    if n == 'stop':
        break
    if not n.isnumeric():
        print ('ошибка, введите цифру')
        continue
    price = int (n)
    total += price



print (f"Cумма за день: {total}")

time.sleep(50)

