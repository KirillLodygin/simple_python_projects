#! python3

import pyperclip
import re

phoneRegex = re.compile(r'(\+7|8)?(\(\d{3}\))?(\d{3})(\s|-|\.)((\d{4})|((\d{2})(\s|-|\.)(\d{2})))')
emailRegex = re.compile(r'([a-zA-Z0-9._%+-]+)(@)([a-zA-Z0-9.-]+)(\.[a-zA-Z]{2,4})')

text = str(pyperclip.paste())

catalog = {'phones': [],'emailes': []}
phones, emailes = 0, 0

with open(r'C:\Users\Kirilll\PycharmProjects\simple_python_projects\usingRegExp\phones_and_emailes\catalog\catalog.txt') as inf:
	for line in inf:
		line = line.strip()
		odj = phoneRegex.search(line)
		if odj != None:
			catalog['phones'].append(odj.group())
			continue
		odj = emailRegex.search(line)
		if odj != None:
			catalog['emailes'].append(odj.group())

for groups in phoneRegex.findall(text):
	if ''.join([groups[0], groups[1], groups[2], '-', groups[4]]) in catalog['phones']:
		continue
	else:
		catalog['phones'].append(''.join([groups[0], groups[1], groups[2], '-', groups[4]]))
		phones += 1

for groups in emailRegex.findall(text):
	if ''.join(groups) in catalog['emailes']:
		continue
	else:
		catalog['emailes'].append(''.join(groups))
		emailes += 1

with open('.\catalog\catalog.txt', 'w') as ouf:
	ouf.write('PHONES:')
	if phones == 0:
		print('\nNo phone numbers found.\n')
	for cell in catalog['phones']:
		ouf.write('\n' + cell)
		
	
	ouf.write('\n\nEMAIL ADDRESSES:')
	if emailes == 0:
		print('No email addresses found.')
	for cell in catalog['emailes']:
		ouf.write('\n' + cell)
		