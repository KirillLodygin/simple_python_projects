import pyperclip
import re

phoneRegex = re.compile(r'(\+7|8)?(\(\d{3}\))?(\d{3})(\s|-|\.)((\d{4})|((\d{2})(\s|-|\.)(\d{2})))')
emailRegex = re.compile(r'([a-zA-Z0-9._%+-]+)(@)([a-zA-Z0-9.-]+)(\.[a-zA-Z]{2,4})')

text = str(pyperclip.paste())

catalog = {'phones': [],'emailes': []}

for groups in phoneRegex.findall(text):
	if ''.join([groups[0], groups[1], groups[2], '-', groups[4], groups[7], groups[9]]) in catalog['phones']:
		continue
	else:
		catalog['phones'].append(''.join([groups[0], groups[1], groups[2], '-', groups[4], groups[7], groups[9]]))

for groups in emailRegex.findall(text):
	if ''.join(groups) in catalog['emailes']:
		continue
	else:
		catalog['emailes'].append(''.join(groups))

with open('usingRegExp/catalog.txt', 'w') as ouf:
	ouf.write('PHONES:')
	if len(catalog['phones']) == 0:
		ouf.write('\nNo phone numbers found.')
	else:
		for cell in catalog['phones']:
			ouf.write('\n' + cell)
	
	ouf.write('\n\nEMAIL ADDRESSES:')
	if len(catalog['emailes']) == 0:
		ouf.write('\nNo email addresses found.')
	else:
		for cell in catalog['emailes']:
			ouf.write('\n' + cell)
		