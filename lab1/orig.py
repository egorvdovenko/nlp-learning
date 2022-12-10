import os

def insertCheck(word):
    word = list(word)
    for char in charList:
        for x in range(len(word)+1):
            word.insert(x,char)
            word1 = ''.join(word)
            if word1 in word_dict:
                correctSet.add(word1)
            word.pop(x)

def delCheck(word):
    word = list(word)
    for x in range(len(word)):
        a = word.pop(x)
        word1 = ''.join(word)
        if word1 in word_dict:
            correctSet.add(word1)
        word.insert(x, a)

def replace(word):
    word = list(word)
    for char in charList:
        for x in range(len(word)):
            word[x], replacedChar = char, word[x]
            word1 = ''.join(word)
            if word1 in word_dict:
                correctSet.add(word1)
            word[x] = replacedChar

def swap(word):
    word = list(word)
    for x in range(len(word)-1):
        word[x], word[x+1] = word[x+1], word[x]
        word1 = ''.join(word)
        if word1 in word_dict:
            correctSet.add(word1)
        word[x], word[x+1] = word[x+1], word[x]

def getCharFrq(char_set):
    dict_result = {a: 0 for a in char_set}
    for book in book_list:
        file = open(book,  encoding="utf-8").read()
        for c in file:
            dict_result[c]+=1
    return dict(sorted(dict_result.items(), key=lambda x: x[1], reverse = True))

def get_set_result():
    set_result = set()
    for book in book_list:
        temp_set = set(open(book,  encoding="utf-8").read())
        set_result = set.union(set_result, temp_set)
    return set_result

def get_dict(ist_alpha_list):
    set_result = set()
    exception = [' ','\n']
    for c in exception:
        ist_alpha_list.remove(c)
    for book in book_list:
        file = open(book,  encoding="utf-8").read()
        for c in ist_alpha_list:
            while c in file:
                file = file.replace(c,'')
        for c in ['-','\n']:
            while c in file:
                file = file.replace(c,' ')
        file = file.lower()
        word_list_result = file.split()
        set_result = set.union(set_result, set(word_list_result))

    dict_result = {a: 0 for a in set_result}
    for book in book_list:
        file = open(book,  encoding="utf-8").read()
        for c in ist_alpha_list:
            while c in file:
                file = file.replace(c,'')
        file = file.lower()
        word_list_result = file.split()
        for x in word_list_result:
            dict_result[x] +=1
    
    return dict(sorted(dict_result.items(), key=lambda x: x[1], reverse = True))

book_list = ['CrimeAndPunishment.txt', 'EugeneOnegin.txt', 'FathersAndSons.txt', 'MasterAndMargarita.txt', 'WarAndPeace.txt']
menu = ['2. Сформировать словарь символов по всем текстам.',
'3. Сколько различных символов встречается в текстах?',
'4. Какие небуквенные символы присутствуют в текстах?',
'5. Рассчитать частоту каждого символа, записать в словарь. Отсортировать по убыванию частоты. Какие буквы чаще всего встречаются в словах?',
'6. Сформировать словарь слов. Сколько всего слов в текстах? Сколько различных слов встречается в текстах? ',
'7. Написать программу – корректор правописания:']
flag = True
charList = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
correctSet = set()

set_result = get_set_result()
ist_alpha_list = [c for c in set_result if not c.isalpha()]
word_dict = get_dict(ist_alpha_list)

while flag == True:
    print(*menu, sep = '\n')
    menuChoise = input('Выбор 2-7, для выхода "exit" : ')
    
    if menuChoise == '2':
        os.system('cls')
        print("\033[34m{}\033[0m".format(menu[int(menuChoise)-2]))
        print(sorted(set_result), '\n')

    elif menuChoise == '3':
        os.system('cls')
        print("\033[34m{}\033[0m".format(menu[int(menuChoise)-2]))
        print(len(set_result), '\n')

    elif menuChoise == '4':
        os.system('cls')
        print("\033[34m{}\033[0m".format(menu[int(menuChoise)-2]))
        print(*sorted(ist_alpha_list))

    elif menuChoise == '5':
        os.system('cls')
        print("\033[34m{}\033[0m".format(menu[int(menuChoise)-2]))
        char_dict = getCharFrq(set_result)
        f = open('char_dict.txt', 'w', encoding="utf-8")
        i = 1
        for pair in char_dict:
            f.write('{:<3} | {:<3} | {:>6} \n'.format(str(i), '"'+str(pair)+'"' , char_dict[pair]))
            i+=1
        print("Словарь выведен в файл char_dict.txt")

    elif menuChoise == '6':
        os.system('cls')
        print("\033[34m{}\033[0m".format(menu[int(menuChoise)-2]))
        f = open('word_dict.txt', 'w', encoding="utf-8")
        i = 1
        for pair in word_dict:
            f.write('{:<5} | {:<20} | {:>5} \n'.format(str(i), str(pair) , word_dict[pair]))
            i+=1
        print("Словарь выведен в файл word_dict.txt")

    elif menuChoise == '7':
        os.system('cls')
        print("\033[34m{}\033[0m".format(menu[int(menuChoise)-2]))
        word = input('Введите слово с 1 ошибкой: ')
        insertCheck(word)
        delCheck(word)
        swap(word)
        replace(word)
        print(correctSet)
        correctSet.clear()

    elif menuChoise == 'exit': flag = False
    else: 
        os.system('cls')
        print('Ошибка')