import os

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
books = ['CrimeAndPunishment.txt', 'EugeneOnegin.txt', 'FathersAndSons.txt', 'MasterAndMargarita.txt', 'WarAndPeace.txt']

def getCharsDict():
  result_set = set()

  for b in books:
    temp_set = set(open(b, encoding="utf-8").read())
    result_set = set.union(result_set, temp_set)

  return result_set

chars_dict = getCharsDict()

os.system('clear')
print('**********')
print(*[
  '1. Сформировать словарь символов по всем текстам.',
  '2. Сколько различных символов встречается в текстах?',
  '3. Какие небуквенные символы присутствуют в текстах?',
  '4. Рассчитать частоту каждого символа, записать в словарь. Отсортировать по убыванию частоты. Какие буквы чаще всего встречаются в словах?',
  '5. Сформировать словарь слов. Сколько всего слов в текстах? Сколько различных слов встречается в текстах? ',
  '6. Написать программу – корректор правописания.'
], sep = '\n')

user_choice = ''
while user_choice != 'exit':
  print('**********')
  user_choice = input('Выбор 1-6: ')
  print('**********')

  if user_choice == '1':
    print(sorted(chars_dict))
  elif user_choice == '2':
    print(len(chars_dict))