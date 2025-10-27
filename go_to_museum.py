import time
import webbrowser

time.sleep (1)
print ('*' * 39)
print ("welcome to the go to museum version 1")
print ('*' * 39)

time.sleep(1)

time.sleep(1)
print ('Дорогой друг!')
print ('Меня зовут Игорь. Я автор этой программы, скажи мне, как зовут тебя?')
name = input ('Введите ваше имя: ')

print (f"{name} , давай попробуем посетить здесь и сейчас знаменитые музеи мира?")
print ('''Выбери страну,музей в которой ты бы хотел(а) посмотреть:
 1. Россия
 2. Франция
 3. Великобритания
 4. Китай
 5. Япония ''')

country = int (input ('Введи номер предпочитаемой страны: '))

print (f'Отлично, ты выбрал(а) страну под номером: {country}, музей этой страны мы и посетим, сейчас откроется браузер:')
print ('Приятного времени')

time.sleep(6)

if country == 1:
    webbrowser.open('https://virtual.rusmuseumvrm.ru/')
elif country == 2:
    webbrowser.open('https://www.louvre.fr/')
elif country == 3:
    webbrowser.open('https://artsandculture.google.com/streetview/_/AwEp68JO4NECkQ?sv_lng=-0.12660248387204245&sv_lat=51.51905371774084&sv_h=306&sv_p=0&sv_pid=JeKwUFYAMWXNWPh3IOg3jw&sv_z=1.0000000000000002')
elif country == 4:
    webbrowser.open('https://www.comuseum.com/')
elif country == 5:
    webbrowser.open('https://www.tnm.jp/?lang=en')
else:
    print ('вы ввели некорректную цифру')