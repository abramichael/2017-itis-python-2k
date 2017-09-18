#coding: utf-8

import random

#сгенерировать 50 файлов,
for i in range(50):
	#сначала генерируется длина имени от 1 до 5, 
	length = random.randrange(1, 6)

	#затем посимвольно генерируется имя файла
	filename = ""
	for j in range(length):
		#сгенерировать символ
		num_sym = random.randrange(ord('a'), ord('z') + 1)
		ch = chr(num_sym)
		filename += ch
	filename += ".txt"

	f = open(filename, "w")
	f.write(str(random.random()))
	f.close()

