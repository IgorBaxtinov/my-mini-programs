import random
import data
import time


time.sleep (1)
print ('*' * 39)
print ("welcome to tell me a joke version 1")
print ('*' * 39)

time.sleep(1)

time.sleep(1)
print ('Дорогой друг!')
print ('Меня зовут Игорь. Я автор этой программы, скажи мне, как зовут тебя?')
name = input ('Введите ваше имя: ')

print (f"{name} , давай попробуем извлечь один случайный анекдот из нашей базы?")

time.sleep(2)

print ('Шутка дня: ')

print (random.choice(data.list_data))

time.sleep(5)

print ('На сегодня всё, жду тебя завтра')

time.sleep(50)





