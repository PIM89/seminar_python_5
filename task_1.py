# Напишите программу, удаляющую из текста все слова, содержащие "абв".

import re


with open('task_1_text_input.txt', 'r', encoding="utf-8") as f:
    text = f.read()

text_list = text.split()
letters = ['а', 'б', 'в']
my_list = []
for i in text_list:
    for j in letters:
        if j in i:
            my_list.append(i)
result = [x for x in text_list if x not in my_list]

with open('task_1_text_output.txt', 'w', encoding="utf-8") as f:
   f.write(" ".join(result))
