#! python3
# -*- coding: utf8 -*-

import re

# Составить словарь, в котором ключи - слова на замену, а значения - предложение пользователю ввести новое слово
wordsForReplacement = {
	'ADJECTIVE': 'Введите прилагательное\n',
	'NOUN': 'Введите существительное\n',
	'ADVERB': 'Введите наречие\n',
	'VERB': 'Введите глагол\n'
}

# Открыть файл, считать текст в строку и вывести его в терминал
with open(r'.\texts\originalText.txt') as inf:
	text = inf.read()
print(text)

# Преобразовать строку в список
text = text.split(' ')

# Список для заполнения словами обработанного текста
newText = []

# Перебрать словарь, проверяя, содержит ли список ключи-слова из словаря
for word in text:
	newWord = ''
	for key in wordsForReplacement.keys():
		nRegex = re.compile(key)
		mo = nRegex.search(word)
		# Если ключ в тексте есть, предложить пользователю ввести слово на замену
		if mo is not None:
			newWord = input(wordsForReplacement[key])
			newText.append(nRegex.sub(newWord, word))
			break
	if newWord == '':
		newText.append(word)

# Преобразовать список в строку
text = ' '.join(newText)
print('\n' + text)

# Открыть файл для записи и записать в него текст
with open(r'.\texts\processedText.txt', 'w') as out:
	out.write(text)
	
print('\nОбработанный текст записан в файл processedText.txt')
