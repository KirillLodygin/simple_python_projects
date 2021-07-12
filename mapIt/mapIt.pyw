#! python3
# -*- coding: utf8 -*-

# mapIt.pyw - Запускает карту в браузере, извлекая адрес из командной строки
#             или буфера обмена

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	# Получение адреса из командной строки
	address = ' '.join(sys.argv[1:])
else:
	# Получить адрес из буфера обмена
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
