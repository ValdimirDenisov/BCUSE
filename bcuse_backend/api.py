from flask import request, jsonify
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

students = [
	{
		"surname": "Asd",
		"name": "Asd",
		"middle_name": "Asd",
		"login": "Asd",
		"password": "asd",
		"universities": "asd",
		"specialities": "asd",
		"sum_score": 270,
		"score": [100, 100, 70],
		"subjects": ['rus', 'math', 'inf']
	},
	{
		"surname": "Qwe",
		"name": "Qwe",
		"middle_name": "Qwe",
		"login": "Qwe",
		"password": "qwe",
		"universities": "qwe",
		"specialities": "qwe",
		"sum_score": 170,
		"score": [60, 40, 70],
		"subjects": ['rus', 'math', 'phis']
	},
	{
		"surname": "Zxc",
		"name": "Zxc",
		"middle_name": "Zxc",
		"login": "Zxc",
		"password": "zxc",
		"universities": "zxc",
		"specialities": "zxc",
		"sum_score": 300,
		"score": [100, 100, 100],
		"subjects": ['rus', 'math', 'hist']
	},
]

@app.route("/students/<string:login>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def students(login):
	if request.method == 'GET':
		#login must be specified
		if login == None:
			return jsonify("Specify login"), 400

		#connect to sol
		
		#find and return student with uniq login
		for student in students:
			if student["login"] == login:
				return jsonify(student), 200

		return jsonify("Student not found"), 404
	elif request.method == 'POST':
		#POST request example
		#{"surname": "Sad", "name": "Sad", "middle_name": "Sad", "login": "Sad", "password": "sad", "universities": "sad", "specialities": "sad", "sum_score": 270, "score": [100, 100, 70], "subjects": ["rus", "math", "inf"]}
		surname = request.form.get('surname')
		if surname is None:
			return jsonify("Specify surname"), 400
		
		name = request.form.get('name')
		if name is None:
			return jsonify("Specify name"), 400

		middle_name = request.form.get('middle_name')
		if middle_name is None:
			return jsonify("Specify middle_name"), 400

		password = request.form.get('password')
		if password is None:
			return jsonify("Specify password"), 400

		universities = request.form.get('universities')
		if universities is None:
			return jsonify("Specify universities"), 400

		specialities = request.form.get('specialities')
		if specialities is None:
			return jsonify("Specify specialities"), 400

		sum_score = request.form.get('sum_score')
		if sum_score is None:
			return jsonify("Specify sum_score"), 400

		score = request.form.get('score')
		if score is None:
			return jsonify("Specify score"), 400

		subjects = request.form.get('subjects')
		if subjects is None:
			return jsonify("Specify subjects"), 400
		
		#check this login in db
		for student in students:
			if student["login"] == login:
				return jsonify(f"Student with login {login} already exists"), 400
		
		#create new student
		new_student = {
			"surname": surname,
			"name": name,
			"middle_name": middle_name,
			"login": login,
			"password": password,
			"universities": universities,
			"specialities": specialities,
			"sum_score": sum_score,
			"score": score,
			"subjects": subjects
		}

		#connect to sol
		
		students.append(new_student)
		return jsonify("Student created"), 201
	elif request.method == 'PUT':
		surname = request.form.get('surname')
		if surname is None:
			surname = [student for student in students if student["login"] == login][0]["surname"]
		
		name = request.form.get('name')
		if name is None:
			name = [student for student in students if student["login"] == login][0]["name"]

		middle_name = request.form.get('middle_name')
		if middle_name is None:
			middle_name = [student for student in students if student["login"] == login][0]["middle_name"]

		password = request.form.get('password')
		if password is None:
			pass = [student for student in students if student["login"] == login][0]["password"]

		universities = request.form.get('universities')
		if universities is None:
			universities = [student for student in students if student["login"] == login][0]["universities"]

		specialities = request.form.get('specialities')
		if specialities is None:
			specialities = [student for student in students if student["login"] == login][0]["specialities"]

		sum_score = request.form.get('sum_score')
		if sum_score is None:
			sum_score = [student for student in students if student["login"] == login][0]["sum_score"]

		score = request.form.get('score')
		if score is None:
			score = [student for student in students if student["login"] == login][0]["score"]

		subjects = request.form.get('subjects')
		if subjects is None:
			subjects = [student for student in students if student["login"] == login][0]["subjects"]

		students = [student for student in students if student["login"] != login]

		new_student = {
			"surname": surname,
			"name": name,
			"middle_name": middle_name,
			"login": login,
			"password": password,
			"universities": universities,
			"specialities": specialities,
			"sum_score": sum_score,
			"score": score,
			"subjects": subjects
		}

		#connect to sol

		students.append(new_student)
		return jsonify("Student created"), 201
	elif request.method == 'DELETE':
		#find and delete student by login
		students = [student for student in students if student["login"] != login]
		return jsonify(f"Student with login {login} is deleted"), 200

if __name__ == "__main__":
    app.run(debug=True)