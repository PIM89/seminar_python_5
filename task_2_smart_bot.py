# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: на столе лежит 2021 конфета.
# Играют 2 игрока делая ход после друг после друга.
# Первый ход определяется жеребьевкой.
# За один ход можно забрать не более чем 28 конфект.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# а) Добавьте игру против бота


from random import randint

print('Игра с конфетами!\n\n\
Условие задачи: на столе лежит 2021 конфета.\n\
Играют 2 игрока делая ход после друг после друга.\n\
Первый ход определяется жеребьевкой.\n\
За один ход можно забрать не более чем 28 конфект.\n\
Все конфеты оппонента достаются сделавшему последний ход.\n\n\
Игра с компьютером!')

users = ['SmartBot']
users.append(input('Напишите имя игрока: ').capitalize())
print(f'Игроки: {users}\n')

print('Жеребьевка...\n\
Случайным образом загадано число от 1 до 10.\n\
Игрок который отгадает число или будет ближе к правильному числу начнет игру первым.\n')

number = randint(1, 10)

users_numbers = [randint(1, 10)]
print(f'{users[0]} думает, что это число: {users_numbers[0]}')
users_numbers.append(int(input(f'{users[1]}, введите ваше число: ')))

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
# print(users)

candy = 50
count = 0
max_take = 28
while candy > 0:
    for i in range(2):
        count += 1
        if users[i] == 'SmartBot':
            if count == 1: user_candy = 20
            elif count != 1 and candy <= max_take: user_candy = candy
            elif count != 1: user_candy = 29 - user_candy
            print(f'Осталось конфет: {candy}\nХод игрока: {users[i]}: {user_candy}') 
        else: user_candy = int(input(f'Осталось конфет: {candy}\nХод игрока: {users[i]}: '))
        while user_candy > max_take or user_candy > candy:
            user_candy = int(input(f'Брать можно не менее 1, но не более {max_take} конфет. P.S. Смотри сколько осталось!\nХод игрока: {users[i]}: '))
        candy -= user_candy
        if candy <= 0:
            break
if count % 2 == 0:
    print(f'Победитель: {users[1]}')
else:
    print(f'Победитель: {users[0]}')
