# Напишите программу эмуляцию банкомата
# вы вводите сумму наличных, которую хотите получить
# доступны купюры 100, 50, 20, 5, 1

cash = int(input("Введите сумму для снятия: "))


hundret = cash // 100 # 2
rest_of = cash % 100 # 87

fifty = rest_of // 50 # 1
rest_of = rest_of % 50

twenty = rest_of // 20
rest_of = rest_of % 20

five = rest_of // 5
rest_of = rest_of % 5

one = rest_of

print (f"Будет выдано сотен: {hundret}, пятидесяток: {fifty}, двадцаток: {twenty}, пятёрок: {five}, однёрок: {one} ")






