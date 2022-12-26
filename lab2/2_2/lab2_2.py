import re
import csv
import os

text = open("text.txt", encoding="utf-8").read()

# Написать программу для формирования списка названий рассказов из файла.

raw_titles_list = re.findall("\n {5}\n[А-Я].+?\n {5}\n {5}", text)
titles_list = list(map((lambda t: " ".join(t.split())), raw_titles_list))

# Описать алгоритм выделения названий рассказов.
# Для каждого рассказа сформировать отдельный файл формата txt (utf-8). 
# Файл содержит только текст рассказа. Название файла совпадает с названием рассказа.

if "stories" not in os.listdir():
    os.mkdir("stories")
else:
    for file in os.listdir("stories/"):
        os.remove("stories/" + file)

for ti, t in enumerate(raw_titles_list):
    f = open("stories/{}.txt".format(titles_list[ti]), "w", encoding="utf-8")
    if ti < len(raw_titles_list) - 1:
        f.write(text[text.find(t):text.find(raw_titles_list[ti + 1])])
    else:
        f.write(text[text.find(t):])

# Отсортировать список по алфавиту.

titles_list.sort()

# Сохранить список в формате csv.

titles = open("titles.csv", "w")
write = csv.writer(titles)

for t in titles_list:
   write.writerow(t)
