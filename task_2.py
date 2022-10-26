# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: на столе лежит 2021 конфета.
# Играют 2 игрока делая ход после друг после друга.
# Первый ход определяется жеребьевкой.
# За один ход можно забрать не более чем 28 конфект.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# а) Добавьте игру против бота
# б) Подумайте как наделить бота "интелектом"

from random import randint


print('Игра с конфетами!\n\n\
Условие задачи: на столе лежит 2021 конфета.\n\
Играют 2 игрока делая ход после друг после друга.\n\
Первый ход определяется жеребьевкой.\n\
За один ход можно забрать не более чем 28 конфект.\n\
Все конфеты оппонента достаются сделавшему последний ход.\n')

users = [input(f'Введите имя {i+1} игрока: ').capitalize() for i in range(2)]
print(f'Игроки: {users}\n')

print('Жеребьевка...\n\
Случайным образом загадано число от 1 до 10.\n\
Игрок который отгадает число или будет ближе к правильному числу начнет игру первым.\n')

number = randint(1, 10)
print(number)

users_numbers = [input(f'{users[i]}, введите число: ') for i in range(2)]

i = 0
difference_user_name_1 = abs(number - int(users_numbers[i]))
difference_user_name_2 = abs(number - int(users_numbers[i+1]))
while users_numbers[i] == users_numbers[i+1] or difference_user_name_1 == difference_user_name_2:
    print('Ничья, попробуйте еще раз!\n')
    users_numbers = [input(f'{users[i]}, введите число: ') for i in range(2)]
    number = randint(1, 10)
    difference_user_name_1 = abs(number - int(users_numbers[i]))
    difference_user_name_2 = abs(number - int(users_numbers[i+1]))
    print(number)
if users_numbers[i] == number:
    print(f'Загаданное число равно {number}, {users[i]} начинает игру.')
elif users_numbers[i+1] == number:
    print(f'Загаданное число равно {number}, {users[i+1]} начинает игру.')
    users.reverse()
elif users_numbers[i] != number and users_numbers[i+1] != number:

    if difference_user_name_1 > difference_user_name_2:
        print(f'Загаданное число равно {number}, {users[i+1]} начинает игру.')
        users.reverse()
    else:
        print(f'Загаданное число равно {number}, {users[i]} начинает игру.')
print(users)

candy = 2021
count = 0
max_take = 28
while candy > 0:
    for i in range(2):
        count += 1
        user_candy = int(
            input(f'Осталось конфет: {candy}\nХод игрока: {users[i]}: '))
        while user_candy > max_take:
            user_candy = int(input(f'Брать можно не менее 1, но не более {max_take} конфет.\nХод игрока: {users[i]}: '))
        candy -= user_candy
        if candy <= 0:
            break
if count % 2 == 0:
    print(f'Победитель: {users[1]}')
else:
    print(f'Победитель: {users[0]}')
