from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)

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

class Student(Resource):
	def get(self, login=None):
		if login == None:
			return "Specify login", 400

		#connect to sol
		
		for student in students:
			if(student["login"] == login):
				return student, 200

		return "Student not found", 404

	def post(self, login):
		parser = reqparse.RequestParser()
		parser.add_argument("surname")
		parser.add_argument("name")
		parser.add_argument("middle_name")
		parser.add_argument("password")
		parser.add_argument("universities")
		parser.add_argument("specialities")
		parser.add_argument("sum_score")
		parser.add_argument("score")
		parser.add_argument("subjects")
		params = parser.parse_args()
		
		for student in students:
			if(student["login"] == login):
				return f"Student with login {login} already exists", 400
		
		new_student = {
			"surname": params["surname"],
			"name": params["name"],
			"middle_name": params["middle_name"],
			"login": params["login"],
			"password": params["password"],
			"universities": params["universities"],
			"specialities": params["specialities"],
			"sum_score": params["sum_score"],
			"score": params["score"],
			"subjects": params["subjects"]
		}

		#connect to sol
		
		students.append(new_student)
		return "Student created", 201

api.add_resource(Student, "/students", "/students/", "/students/<string:login>")
if __name__ == '__main__':
    app.run(debug=True)