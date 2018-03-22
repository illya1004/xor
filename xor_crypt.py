import random

key = 24

try:
    fileTEST = open('crypt.txt')
except IOError as e:
	CreatePassword = input("Создайте свой пароль:")
	# Шифрование
	crypt = ""
	for i in CreatePassword:
		try:
			crypt += chr(ord(i)^ord(key))
		except TypeError:
			crypt += chr(ord(i)^key)

	# A = 65 ASCII
	# B = 66
	# C = 67 ...


	with open("crypt.txt","w") as file:
		file.write(crypt)
		
else:
		vxod = input("Введите парль:")
		# Расшифрование
		decrypt = ""
		cryptofile = open("crypt.txt")
		
		
		for j in cryptofile.read():
			try:
				decrypt += chr(ord(j)^ord(key))
			except TypeError:
				decrypt += chr(ord(j)^key)
		loop = True
		if vxod == decrypt:
			while loop:
				print("Что бы выйти напишите (exit) ")
				print("Что бы скачать фото по url напишите (save foto)")
				print("мини игра (mini game)")
				comanda = input()
				if comanda == "mini game":
					say = ['машин','аниме','гладиолус','мир']
					say2 = random.randint(0,3)
					if say2 == 0:
						say3 = say[0]
						print("BMW, Ferrari, Ford, Lamborghini, Mazda, Jaguar. Это все марки", say3[:2])
						otvet = input()
						if otvet == 'машин':
								print("Молодец")
								input()
						if otvet != 'машин':
							print("Ты че тупой?")
							print("BMW, Ferrari, Ford, Lamborghini, Mazda, Jaguar. Это все марки", say3[:3])
							otvet = input()
							if otvet == 'машин':
								print("Молодец")
								input()
							if otvet != 'машин':
								print("Ты че совсем уже с своими играми отупел?")
								print("BMW, Ferrari, Ford, Lamborghini, Mazda, Jaguar. Это все марки", say3[:4])
								otvet = input()
								if otvet == 'машин':
									print("Молодец")
								if otvet != 'машин':
									print("Ты слишком тупой чтобы ответить на этот вопрос. Ты проиграл.")
						
						
					if say2 == 1:
						say4 = say[1]
						print("Эта анимиция пошла из Японии и називаеться она",say4[:2])
						otvet2 = input()
						if otvet2 != 'аниме':
							print("Ты серьезно? Ответ не правильний")
							print("Эта анимиция пошла из Японии и називаеться она",say4[:3])
							otvet2 = input()
							if otvet2 != 'аниме':
								print("Как я понял твой IQ не может ответить на этот вопрос. Ты проиграл")
							if otvet2 == 'аниме':
								print("Мое тебе уважение. Это правильний ответ.")
						if otvet2 == 'аниме':
							print("Мое тебе уважение. Это правильний ответ.")
						
					if say2 == 2:
						print(say[2])
						input()
						
					if say2 == 3:
						print(say[3])
						input()
						
				if comanda == 'exit':
					loop = False



# XOR исключающее ИЛИ

# XOR:
# 1 ^ 1 = 0
# 1 ^ 0 = 1
# 0 ^ 1 = 1
# 0 ^ 0 = 0

x = 10; y = 5

# x = 1010
# y = 0101
x = x ^ y # 1010 ^ 0101 = 1111 
y = x ^ y # 1111 ^ 0101 = 1010 
x = x ^ y # 1111 ^ 1010 = 0101 
# x = 0101
# y = 1010

# Шифр Цезаря с ключом 1: IFMMP XPSME
# XOR Шифрование с ключом 1: IDMMN!VNSME
