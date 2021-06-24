import re


def strip(string, el=' '):
	if el != ' ':
		stringRegex = re.compile(el)
	else:
		stringRegex = re.compile(r'(^\s)?(\s$)?')
	
	return stringRegex.sub('', string)


text = input()
letter = input()

print(strip(text, letter))
print(strip(text))
