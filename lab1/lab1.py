import os

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
books_list = [
  'stories/CrimeAndPunishment.txt', 
  'stories/EugeneOnegin.txt', 
  'stories/FathersAndSons.txt', 
  'stories/MasterAndMargarita.txt', 
  'stories/WarAndPeace.txt'
]

russian_words_set = set(open('russian_dict.txt', encoding='cp1251').read().split())
fixed_words_set = set()

def writeDictToFile(path, dict): 
  file = open(path, 'w', encoding='utf-8')

  for k, v in dict:
    file.write('{}: {}\n'.format(k, v))

  print('Словарь записан в файл:', path)

def getCharsSet():
  chars_set = set()

  for b in books_list:
    temp_set = set(open(b, encoding='utf-8').read())
    chars_set = set.union(chars_set, temp_set)

  return chars_set

def getCharsFreqDict():
  chars_freq_dict = { c: 0 for c in chars_set }

  for b in books_list:
      file = open(b, encoding='utf-8').read()

      for c in file:
          chars_freq_dict[c] += 1

  return chars_freq_dict

def getWordsSet(): 
  words_set = set()

  excepted_chars_list = [c for c in chars_set if not c.isalpha()]
  excepted_chars_list.remove(' ')

  for b in books_list:
    file = open(b, encoding='utf-8').read()

    for c in excepted_chars_list:
      while c in file:
        file = file.replace(c, '')

    file_words = file.lower().split()
    words_set = set.union(words_set, set(file_words))

  return words_set

def getWordsFreqDict():
  words_freq_dict = { a: 0 for a in words_set }

  excepted_chars_list = [c for c in chars_set if not c.isalpha()]
  excepted_chars_list.remove(' ')
  
  for b in books_list:
    file = open(b, encoding='utf-8').read()

    for c in excepted_chars_list:
      while c in file:
        file = file.replace(c, '')
        
    file_words = file.lower().split()

    for w in file_words:
      words_freq_dict[w] +=1
  
  return words_freq_dict

def tryInsert(word):
  word_list = list(word)

  for c in alphabet:
    for i in range(len(word_list) + 1):
      word_list.insert(i, c)
      fixed_word = ''.join(word_list)

      if fixed_word in russian_words_set:
        fixed_words_set.add(fixed_word)

      word_list.pop(i)

def tryDelete(word):
  word_list = list(word)

  for i in range(len(word_list)):
    deleted_char = word_list.pop(i)
    fixed_word = ''.join(word_list)

    if fixed_word in russian_words_set:
      fixed_words_set.add(fixed_word)

    word_list.insert(i, deleted_char)

def trySwap(word):
  word_list = list(word)
    
  for i in range(len(word) - 1):
    word_list[i], word_list[i + 1] = word_list[i + 1], word_list[i]
    fixed_word = ''.join(word_list)

    if fixed_word in russian_words_set:
        fixed_words_set.add(fixed_word)

    word_list[i], word_list[i + 1] = word_list[i + 1], word_list[i]

def tryReplace(word):
  word_list = list(word)

  for c in alphabet:
    for i in range(len(word_list)):
      word_list[i], replaced_char = c, word_list[i]
      fixed_word = ''.join(word_list)

      if fixed_word in russian_words_set:
        fixed_words_set.add(fixed_word)

      word_list[i] = replaced_char

chars_set = getCharsSet()
words_set = getWordsSet()

os.system('clear')

print('**********')
print(*[
  '1. Сформировать словарь символов по всем текстам.',
  '2. Сколько различных символов встречается в текстах?',
  '3. Какие небуквенные символы присутствуют в текстах?',
  '4. Какие буквы чаще всего встречаются в словах?',
  '5. Сколько различных слов встречается в текстах?',
  '6. Корректор правописания.'
], sep = '\n')

while True:
  print('**********')
  user_choice = input('=> ')
  print('**********')

  if user_choice == '1':
    print(sorted(chars_set))
  elif user_choice == '2':
    print(len(chars_set))
  elif user_choice == '3':
    not_alpha_chars_list = [c for c in chars_set if not c.isalpha()]
    print(sorted(not_alpha_chars_list))
  elif user_choice == '4':
    chars_freq_dict = getCharsFreqDict()
    writeDictToFile('chars_freq_dict.txt', sorted(chars_freq_dict.items(), key = lambda x: x[1], reverse = True))
  elif user_choice == '5':
    words_freq_dict = getWordsFreqDict()
    writeDictToFile('words_freq_dict.txt', sorted(words_freq_dict.items(), key = lambda x: x[1], reverse = True))
  elif user_choice == '6':
    word = input('Введите слово для проверки: ')

    tryInsert(word)
    tryDelete(word)
    trySwap(word)
    tryReplace(word)

    print('Возможные варианты исправления:', fixed_words_set)
    fixed_words_set.clear()
  else:
    print('???')
  