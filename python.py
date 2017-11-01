import os.path
file = "log.txt"
file2 = "pass.txt"
if os.path.isfile(file) == True and os.path.isfile(file) == True:
	print('hello')
	login = input("Enter you login: ")
	password = input("Enter you password: ")
else:
	login = input("(registr)Enter you login: ")
	password = input("(registr)Enter you password: ")
	file = open("log.txt", "w")
	file.write(login)
	file.close()
	file = open("pass.txt", "w")
	file.write(password)
	file.close()
while True:
	file = open("log.txt", "r")
	loger = file.read()
	file = open("pass.txt", "r")
	pass2 = file.read()
	if login == loger and password ==  pass2:
		print("Hello admin")
		input()
		break
	else:
		print("error")
		login = input("Enter you login: ")
		password = input("Enter you password: ")