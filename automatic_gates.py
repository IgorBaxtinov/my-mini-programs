import time


time.sleep (1)
print ('*' * 43)
print ("welcome to the automatic_gates version 1")
print ('*' * 43)

time.sleep(1)

print ('''Введите команду open для открытия ворот, команду close для закрытия, команду stop для остановки. 
Команда help для справки''')

is_open = False

while True:
    text = input("yours_command: ").lower()
    if text == 'open':
        if is_open:
            print ('Ворота уже открыты')
        else:
            print ('Ворота открываются')
        is_open = True
       # print ('Ворота открываются')
    elif text == 'close':
        if is_open:
            print('Ворота закрываются')
        else:
            print ('Ворота уже закрыты')
        is_open = False
    elif text == 'stop':
        print ('Закрытие программы')
        break
    elif text == 'help':
        print ('''
        Список команд:
        open - открыть ворота
        close - закрыть ворота
        help - помощь
        stop - завершить программу
        ''')
    else:
        print ('ошибка, неправильная команда')

time.sleep(40)