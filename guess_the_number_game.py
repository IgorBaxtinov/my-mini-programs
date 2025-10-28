import random
import time


time.sleep (1)
print ('*' * 39)
print ("welcome to guess the number game")
print ('*' * 39)

time.sleep(1)

time.sleep(1)
print ('Дорогой друг!')
print ('Меня зовут Игорь. Я автор этой программы, скажи мне, как зовут тебя?')
name = input ('Введите ваше имя: ')

print (f"{name} , давай попробуем угадать число от 0 до 10, которое загадал компьютер с 10 ти попыток")

guess = 0
popytka = 0

number = random.randint (0,10)

while guess != number and popytka <=10:
    guess = int (input("Введите ваше число от 1 до 10: "))
    popytka +=1

print ('The game is over')

time.sleep(50)



