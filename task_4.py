# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('task_4_text_input.txt', 'r', encoding="utf-8") as f:
    text = f.read()

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

print(f'Строка до сжатия: {text}')

text_new = encode(text)
print(f'Строка после сжатия: {text_new}')

with open('task_4_text_output.txt', 'w', encoding="utf-8") as f:
   f.write("".join(text_new))

def decode(s):
    result = ''
    for i in range(len(s)-1):
        if s[i].isdigit():
            result += s[i+1]*int(s[i])
    return result

print(f'Строка после восстановления данных: {decode(text_new)}')


