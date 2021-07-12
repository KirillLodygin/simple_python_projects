#! python3
# -*- coding: utf8 -*-

# backupToZip.py - Копирует папку со всем ее содержимым в ZIP-файл
# с инкременируемым номером копии в имени файла

import os, shutil, zipfile


def backupToZip(folder):
	folder = os.path.abspath(folder)
	os.chdir('C:\\')
	newfolder = 'C:\\Users\\Kirilll\\Educational_projects_archive\\' + os.path.basename(folder) + '_backup'
	
	for foldername, subfolders, filenames in os.walk(folder):
		if foldername != folder:
			break
		for subfolder in subfolders:
			if subfolder != '.git' and subfolder != '.idea' and subfolder != 'venv':
				shutil.copytree(folder + '\\' + subfolder, newfolder + '\\' + subfolder)
	
	# shutil.copytree(folder, newfolder)
	os.chdir('C:\\Users\\Kirilll\\Educational_projects_archive')
	newfolder = os.path.basename(newfolder)
	
	number = 1
	while True:
		zipFilename = newfolder + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename):
			break
		number = number + 1
	
	print('Создается %s...' % (os.path.basename(zipFilename)))
	backupZip = zipfile.ZipFile(zipFilename, 'w')
	
	for foldername, subfolders, filenames in os.walk(newfolder):
		print('Добавление файлов из папки %s...' % (foldername))
		backupZip.write(foldername)
		
		for filename in filenames:
			backupZip.write(os.path.join(foldername, filename))
	
	backupZip.close()
	shutil.rmtree(newfolder)
	print('Готово!!!')


backupToZip(r'C:\Users\Kirilll\PycharmProjects\simple_python_projects')
