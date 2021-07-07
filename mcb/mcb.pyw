#! python3
# -*- coding: utf8 -*-
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import pyperclip
import shelve
import sys

mcbShelve = shelve.open('mcb')

# Сохранить содержимое в буфер обмена
if len(sys.argv) == 3:
	if sys.argv[1].lower() == 'save':
		mcbShelve[sys.argv[2]] = pyperclip.paste()
	if sys.argv[1].lower() == 'delete' and sys.argv[2] in mcbShelve:
		del mcbShelve[sys.argv[2]]
elif len(sys.argv) == 2:
	# Сформировать список ключевых слов и загрузить содержимое
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelve.keys())))
	elif sys.argv[1].lower() == 'delete':
		mcbShelve.clear()
	elif sys.argv[1] in mcbShelve:
		pyperclip.copy(mcbShelve[sys.argv[1]])

mcbShelve.close()
