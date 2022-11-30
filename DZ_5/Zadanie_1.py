# Напишите программу, удаляющую из текста 
# все слова, содержащие ""абв"".

text = input("Введите текст через пробел: \n")

def sort_text(text):
    li = list(filter(lambda x: 'абв' not in x, text.split()))
    return ' '.join(li)
new_text = sort_text(text)

print(f'Текст без слов, содержащих "абв", следующий: \n{new_text}')
