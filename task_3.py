# Создайте программу для игры в "Крестики-нолики"

from random import randint
from re import X


print('\nИгра в "Крестики-нолики"!\n')

users = [input(f'Введите имя {i+1} игрока: ').capitalize() for i in range(2)]
print(f'Игроки: {users}\n')

# Жеребьевка
print('Жеребьевка...\n\
Случайным образом загадано число от 1 до 10.\n\
Игрок который отгадает число или будет ближе к правильному числу начнет игру первым.\n')

number = randint(1, 10)
# print(number)

users_numbers = [input(f'{users[i]}, введите число: ') for i in range(2)]

i = 0
difference_user_name_1 = abs(number - int(users_numbers[i]))
difference_user_name_2 = abs(number - int(users_numbers[i+1]))
while users_numbers[i] == users_numbers[i+1] or difference_user_name_1 == difference_user_name_2:
    print('Ничья, попробуйте еще раз!\n')
    number = randint(1, 10)
    users_numbers = [input(f'{users[i]}, введите число: ') for i in range(2)]
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
print(f'Игроки: {users}\n')


list_elem = list(range(1, 10))


def print_scoreboard(lst):
    for i in range(3):
        print('|', lst[0+i*3], '|', lst[1+i*3], "|", lst[2+i*3], "|\n")


print_scoreboard(list_elem)

# Игра


def check_win(lst):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for elem in win_coord:
        if lst[elem[0]] == lst[elem[1]] == lst[elem[2]]:
            return True
    return False


count = 9
while count >= 0:
    for i in range(2):
        if i == 0:
            cross = 'X'
        else:
            cross = 'O'
        motion = int(input(
            f'Осталось ходов: {count}\nХод игрока: {users[i]}. Куда поставим {cross}: \n'))
        if motion in list_elem:
            list_elem[list_elem.index(motion)] = cross
        print_scoreboard(list_elem)
        if check_win(list_elem):
            print(f'Поздравляем победителя: {users[i]}')
            exit()
        count -= 1
        if count == 0:
            print(f'Ничья: {users[i]}, {users[i+1]} сыграйте ещё раз!')
            exit()
