import re
import csv

text = open("text.txt", encoding="utf-8").read()

# Написать программу для формирования списка названий рассказов из файла (ссылка).

titlesList = re.findall("\n {5}\n[А-Я].+?\n {5}\n {5}", text)
titlesList = list(map((lambda t: " ".join(t.split())), titlesList))

# Описать алгоритм выделения названий рассказов.
# Для каждого рассказа сформировать отдельный файл формата txt (utf-8). Файл содержит только текст рассказа. Название файла совпадает с названием рассказа.

for ti, t in enumerate(titlesList):
    f = open('stories/{}.txt'.format(t), "w", encoding="utf-8")
    if ti < len(titlesList) - 1:
        f.write(text[text.find(t):text.find(titlesList[ti + 1])])

# Отсортировать список по алфавиту.

titlesList.sort()

# Сохранить список в формате csv.

titles = open("titles.csv", "w")
write = csv.writer(titles)

for t in titlesList:
   write.writerow(t)
