import time
import webbrowser

time.sleep (1)
print ('*' * 39)
print ("welcome to the go to cinema version 1")
print ('*' * 39)

time.sleep(1)

time.sleep(1)
print ('Дорогой друг!')
print ('Меня зовут Игорь. Я автор этой программы, скажи мне, как зовут тебя?')
name = input ('Введите ваше имя: ')

print (f"{name} не пора ли отдохнуть и посмотреть хорошее кино?")
print ('''Выбери оператора связи, который ты предпочитаешь:
 1. МТС
 2. Билайн
 3. Мегафон
 4. Теле2
 5. Мотив ''')

operator = int (input ('Введи номер предпочитаемого оператора: '))

print (f'Отлично, ты выбрал оператора под номером: {operator}, онлайн кинотеатр от этого оператора мы и посетим, сейчас откроется браузер:')
print ('Приятного просмотра')

time.sleep(4)

if operator == 1:
    webbrowser.open('https://kion.ru/')
elif operator ==2:
    webbrowser.open('https://beeline.tv/')
elif operator ==3:
    webbrowser.open('https://start.ru/')
elif operator ==4:
    webbrowser.open('https://wink.ru/kinozal')
elif operator ==5:
    webbrowser.open('https://motivtv.ru')
else:
    print ('вы ввели некорректную цифру')