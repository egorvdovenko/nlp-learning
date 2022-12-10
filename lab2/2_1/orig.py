import re
import nltk
from razdel import tokenize, sentenize
from mosestokenizer import *
import rutokenizer

# Для токенизации можно использовать следующие инструменты:
# 1. Функции строкового объекта:
# tokens = raw.split()

# 2. Регулярные выражения:
# tokens = re.findall('\w+|\d+',raw)
# tokens = re.findall('\w+(?:[-']\w+)*|'|[-.(]+|\S\w*',raw)

# 3. Пакет nltk:
# import nltk
# nltk.download('punkt')
# tokens = [nltk.word_tokenize(t) for t in nltk.sent_tokenize(raw)]

# 4. Библиотека Razdel (проект Natasha):
# from razdel import tokenize, sentenize
# tokens = [w.text  for sent in list(sentenize(raw)) for w in list(tokenize(sent.text))]

# 5. Токенизатор rutokenizer:
# pip install git+https://github.com/Koziev/rutokenizer
# import rutokenizer
# t = rutokenizer.Tokenizer()
# t.load()
# t.tokenize(raw)

# 6. Библиотека mosestokenizer:
# from mosestokenizer import *
# tokenize = MosesTokenizer('ru')
# tokenize(raw)
# tokenize.close()

nltk.download('punkt')
t = rutokenizer.Tokenizer()
t.load()
text = open("text.txt",  encoding="utf-8").read()
tokens = []
files = ['tokens1','tokens2_1','tokens2_2','tokens4','tokens5']

tokens.append(text.split())
tokens.append(re.findall('\w+|\d+',text))
tokens.append(re.findall("\w+(?:[-']\w+)*|'|[-.(]+|\S\w*",text))

tokens.append([w.text  for sent in list(sentenize(text)) for w in list(tokenize(sent.text))])
tokens.append(t.tokenize(text))

for x in range(len(files)):
    f = open(files[x]+'.txt', 'w', encoding="utf-8")
    for y in tokens[x]:
        f.write(y+'\n')

tok3 = [nltk.word_tokenize(t) for t in nltk.sent_tokenize(text)]
f = open('tokens3.txt', 'w', encoding="utf-8")
for sentences in tok3:
    for words in sentences:
        f.write(words+'\n')
