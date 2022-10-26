# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def encode(s):
    encoding = ''
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i += 1
        encoding += str(count) + s[i]
        i += 1
    return encoding


s = 'ABBBBCCCCCDD'
print(f'Строка до сжатия: {s}')
s1 = encode(s)
print(f'Строка после сжатия: {s1}')


def decode(s):
    result = ''
    for i in range(len(s)-1):
        if s[i].isdigit():
            result += s[i+1]*int(s[i])
    return result


print(f'Строка после восстановления данных: {decode(s1)}')
