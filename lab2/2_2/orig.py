import re
import os

def writeStotyNames(list):
    list = sorted(list)
    fileType = [".csv", ".txt"]
    for x in range(len(list)):
        list[x] = list[x].rstrip().lstrip()
    for x in fileType:
        f = open("result"+x,"w")
        for x in range(1,len(list)):
            f.write('{}. {}\n'.format(x,list[x]))

a = lambda x: text.find(list1[x], text.find(list1[x-1],text.find(list1[x-2])))
b = lambda x: text.find(list1[x+1], text.find(list1[x],text.find(list1[x-1])))

if 'stories' not in os.listdir():
    os.mkdir('stories')
else: 
    for file in os.listdir('stories/'):
        os.remove('stories/'+file)

text = open("text.txt",  encoding="utf-8").read()
list1 = re.findall("     \n\w+\,{0,1}\ {0,1}[\w*\,{0,1}\ {0,1}]*\n", text)
del list1[0]
temp = []
stop = ['I','Пролог','Эпилог']

for x in range(len(list1)-1):
    if x in temp: continue
    if b(x) - a(x) < 50: 
        temp.append(x+1)
        continue
    if b(x) - a(x) < 500: 
        temp.append(x)

for x in range(len(list1)):
    for y in stop:
        if y in list1[x]:
            temp.append(x)

counter = 0
for x in sorted(list(set(temp))):
    del list1[x - counter]
    counter += 1

writeStotyNames(list1)

f = open('stories/{}.{}.txt'.format(1, list1[0].lstrip().rstrip()),"w",  encoding="utf-8")
f.write(text[text.find(list1[0]):text.find(list1[1])])

for x in range(2,len(list1)-1):
    f = open('stories/{}.{}.txt'.format(x, list1[x].lstrip().rstrip()),"w",  encoding="utf-8")
    f.write(text[a(x):b(x)])
else: 
    f = open('stories/{}.{}.txt'.format(x, list1[-1].lstrip().rstrip()),"w",  encoding="utf-8")
    f.write(text[a(x+1):])