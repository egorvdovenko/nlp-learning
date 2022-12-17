import re
import nltk
import rutokenizer
from razdel import tokenize, sentenize
from mosestokenizer import *

nltk.download('punkt')

t = rutokenizer.Tokenizer()
t.load()

text = open("text.txt",  encoding="utf-8").read()
tokens = []

# 1. Функции строкового объекта:

tokens.append(text.split())

# 2. Регулярные выражения:

tokens.append(re.findall('\w+|\d+', text))
tokens.append(re.findall("\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", text))

# 3. Библиотека Razdel (проект Natasha):

tokens.append([w.text for sent in list(sentenize(text)) for w in list(tokenize(sent.text))])

# 4. Токенизатор rutokenizer:

tokens.append(t.tokenize(text))

# 5. Библиотека mosestokenizer:

# mt = MosesTokenizer('ru')
# tokens.append(mt(text))
# mt.close()

for i, t in enumerate(tokens):
    f = open('tokens_' + str(i + 1) + '.txt', 'w', encoding='utf-8')

    for w in t:
        f.write(w + '\n')

# Пакет nltk:

nltkTokens = [nltk.word_tokenize(t) for t in nltk.sent_tokenize(text)]
f = open('tokens_nltk.txt', 'w', encoding="utf-8")

for nt in nltkTokens:
    for w in nt:
        f.write(w + '\n')

