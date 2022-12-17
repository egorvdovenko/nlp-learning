import re
import nltk
import rutokenizer
import xlsxwriter
from razdel import tokenize, sentenize
from mosestokenizer import *

nltk.download("punkt")

t = rutokenizer.Tokenizer()
t.load()

workbook = xlsxwriter.Workbook("results.xlsx")
worksheet = workbook.add_worksheet()

text = open("text.txt",  encoding="utf-8").read()
tokens = []

# 1. Функции строкового объекта:

tokens.append(text.split())

# 2. Регулярные выражения:

tokens.append(re.findall("\w+|\d+", text))
tokens.append(re.findall("\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", text))

# 3. Библиотека Razdel (проект Natasha):

tokens.append([w.text for sent in list(sentenize(text)) for w in list(tokenize(sent.text))])

# 4. Токенизатор rutokenizer:

tokens.append(t.tokenize(text))

# 5. Библиотека mosestokenizer:

# mt = MosesTokenizer("ru")
# tokens.append(mt(text))
# mt.close()

# 6. Пакет nltk:

nltk_tokens = [nltk.word_tokenize(t) for t in nltk.sent_tokenize(text)]

# Вывод значений в таблицу:

for ti, t in enumerate(tokens):
    for wi, w in enumerate(t):
        worksheet.write(wi, ti, w)

for nt in nltk_tokens:
    for wi, w in enumerate(nt):
        worksheet.write(wi, len(tokens), w)

workbook.close()
