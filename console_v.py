from requests import get, post
url = "http://127.0.0.1:5000"

while True:
	c = int(input("[1] Получить информацию об ученике\n[2] Получить список логинов студентов, поступающих на данную специальность\n[3] Добавить студента на специальность\n[4] Добавить ВУЗ студенту\nВыбор: "))
	print("")
	
	if c == 1:
		login = input("Введите логин: ")
		university = input("Введите университет: ")
		print("")
		data = post(url+"/student/"+login, data={"university": university})
		print(data)
	elif c == 2:
		spec = input("Введите специальность: ")
		print("")
		data = get(url+"/university/"+spec)
		print(data)
	elif c == 3:
		login = input("Введите логин: ")
		spec = input("Введите специальность: ")
		print("")
		data = post(url+"/university/", data={"login":login, "spec":spec})
		print(data)
	elif c == 4:
		login = input("Введите логин: ")
		password = input("Введите пароль: ")
		universities = input("Введите университет: ")
		spec = input("Введите специальность: ")
		print("")
		data = post(url+"/student/", data={"login":login, "password": password, "universities": universities, "spec": spec})
		print(data)
	else:
		print("Try again")
		print("")