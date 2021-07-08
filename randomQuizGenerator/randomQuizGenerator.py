#! python3

import random, os

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

os.chdir(r'C:\Users\Kirilll\PycharmProjects\simple_python_projects\randomQuizGenerator\exam_tickets')

# Generate 35 quiz files.
for quizNum in range(35):
	# Создать файлы билетов и файлы ключей ответов
	quizFile = open(r'.\questions\capitalsquiz%s.txt' % (quizNum + 1), 'w')
	answerKeyFile = open(r'.\answerKeys\capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

	# Записать заголовок билета
	quizFile.write('Имя:\n\nДата:\n\nКурс:\n\n')
	quizFile.write((' ' * 15) + 'Проверка знания столиц штатов (Билет %s)' % (quizNum + 1))
	quizFile.write('\n\n')

	# Перемешать порядок следования штатов
	states = list(capitals.keys())
	random.shuffle(states)

	# Организовать цикл по всем 50 штатам, создавая вопрос для каждого из них
	for questionNum in range(50):
		# Получение правильных и неправильных ответов
		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)
		
		# Записать варианты вопросов и ответов в файл билета
		quizFile.write('%s Выберите столицу штата %s\n' % (questionNum + 1, states[questionNum]))
		for i in range(4):
			quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
			quizFile.write('\n')
		
		# Записать ключ ответа в файл
		answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
	quizFile.close()
	answerKeyFile.close()
	