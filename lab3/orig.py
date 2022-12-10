import os
import pymorphy2
import matplotlib.pyplot as plt

os.system('cls')

def get_word_list(text):
    text_set = set(text)
    digit_list = []
    for char in text_set:
        if not char.isalpha():
            digit_list.append(char)
    digit_list.remove(' ')
    for char in digit_list:
        while char in text:
            text = text.replace(char, ' ')
    word_list = text.split()
    temp = []
    for word in word_list:
        if len(word) > 3: #english
            temp.append(word)
    return(temp)

text = open('text.txt', encoding='UTF-8').read()
morph = pymorphy2.MorphAnalyzer()
word_list = get_word_list(text)
word_list = [word.lower() for word in word_list]
word_set = set(word_list)
stop_list = ['NPRO', 'PRED', 'PREP', 'CONJ', 'PRCL', 'INTJ']

temp = []
for word in word_set:
    if morph.parse(word)[0].tag.POS not in stop_list: 
        temp.append(word)

lem_set = set([morph.parse(word)[0].normal_form for word in temp])

word_dict = {}

for word in word_list:
    normal_form = morph.parse(word)[0].normal_form
    if normal_form in lem_set:
        if normal_form not in word_dict:
            word_dict[normal_form] = 1
        else: 
            word_dict[normal_form] += 1

top20 = sorted(word_dict.items(), key=lambda x: x[1], reverse = True)[:20]
word_count = len(word_dict)
chartX = [*range(1,21)] #ранг
chartY = [] #частота
for word in top20:
    chartY.append(word[1])

plt.title('Закон Зипфа') # заголовок
plt.xlabel('Ранг') # ось абсцисс
plt.ylabel('Частота') # ось ординат
plt.plot(chartX, chartY)
plt.show()

c = []
for x in range(20):
    c.append(chartY[x]*(x+1)/(word_count))
print(*c)
print(sum(c)/len(c))