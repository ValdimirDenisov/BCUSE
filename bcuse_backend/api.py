from flask import request, jsonify
from flask_api import FlaskAPI, status, exceptions
import os
from secret import project_id, url

app = FlaskAPI(__name__)

from web3 import Web3, HTTPProvider

os.environ['WEB3_INFURA_PROJECT_ID'] = project_id
w3 = Web3(HTTPProvider(url))

university_cont = '0xcC30D20DfA1EBe92Ac947312572e505c7C270cE2'
university_abi = [{"inputs":[{"internalType":"string[]","name":"en_spec","type":"string[]"},{"internalType":"uint16[]","name":"en_amount","type":"uint16[]"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"en_student","type":"address"},{"internalType":"string","name":"en_spec","type":"string"}],"name":"add_student","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"en_spec","type":"string"}],"name":"get_all_students_for_speciality","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"}]

BCUSE_university = w3.eth.contract(
    address=university_cont,
    abi=university_abi
)

students_ = [
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

students = {
	"cat": ["tac", "0xC313F4f3efD6124941f95F32843651AB9753801C"],
	"dog": ["god", "0x8e0542831e8fce4E9850ccE41e0C4AE85A4B4"],
	"fish": ["hsif", "0x4Db0151F28D33669c4fD45261D267F282a26d851"]
}

@app.route("/student/<string:login>", methods=['POST'])
def student_get(login):
	if request.method == 'POST':
		#login must be specified
		if login == None:
			return jsonify("Specify login"), 400

		university = request.form.get('university')
		if university is None:
			return jsonify("Specify university"), 400

		#реализовать коннект к sol, использовать функцию get_all_information_for_university
		#передать ей university, вывод записать в ret
		student_cont = students[login][1]
		student_abi = [{"inputs":[{"internalType":"string[]","name":"en_personal_data","type":"string[]"},{"internalType":"uint16[]","name":"en_score","type":"uint16[]"},{"internalType":"string[]","name":"en_subjects","type":"string[]"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"string","name":"en_uni","type":"string"}],"name":"get_all_information_for_university","outputs":[{"internalType":"string[3]","name":"","type":"string[3]"},{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"uint16[]","name":"","type":"uint16[]"},{"internalType":"string[]","name":"","type":"string[]"},{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string[]","name":"en_uni","type":"string[]"},{"internalType":"string[][]","name":"en_spec","type":"string[][]"},{"internalType":"string","name":"en_login","type":"string"},{"internalType":"string","name":"en_password","type":"string"}],"name":"set_data","outputs":[],"stateMutability":"nonpayable","type":"function"}]

		BCUSE_student = w3.eth.contract(
    		address=student_cont,
    		abi=student_abi
		)

		ret = BCUSE_student.functions.get_all_information_for_university(university).call()
		
		return jsonify(ret)

@app.route("/student/", methods=['POST'])
def student_post():
	if request.method == 'POST':
		#POST request example
		#{"universities": ["MGU", "MIPT"], "specialities": [["polit", "info"], ["info"]], "login": "Asd", "password": "Asd"}
		
		login = request.form.get('login')
		if login is None:
			return jsonify("Specify login"), 400

		password = request.form.get('password')
		if password is None:
			return jsonify("Specify password"), 400

		universities = request.form.get('universities')
		if universities is None:
			return jsonify("Specify universities"), 400

		spec = request.form.get('spec')
		if spec is None:
			return jsonify("Specify specialities"), 400
		
		#реализовать коннект к sol, использовать функцию set_data
		#передать ей universities, specialities, login, password, вывод записать в ret
		student_cont = students[login][1]
		student_abi = [{"inputs":[{"internalType":"string[]","name":"en_personal_data","type":"string[]"},{"internalType":"uint16[]","name":"en_score","type":"uint16[]"},{"internalType":"string[]","name":"en_subjects","type":"string[]"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"string","name":"en_uni","type":"string"}],"name":"get_all_information_for_university","outputs":[{"internalType":"string[3]","name":"","type":"string[3]"},{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"uint16[]","name":"","type":"uint16[]"},{"internalType":"string[]","name":"","type":"string[]"},{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string[]","name":"en_uni","type":"string[]"},{"internalType":"string[][]","name":"en_spec","type":"string[][]"},{"internalType":"string","name":"en_login","type":"string"},{"internalType":"string","name":"en_password","type":"string"}],"name":"set_data","outputs":[],"stateMutability":"nonpayable","type":"function"}]

		BCUSE_student = w3.eth.contract(
    		address=student_cont,
    		abi=student_abi
		)

		ret = BCUSE_student.functions.set_data(universities, specialities, login, password).call()

		return jsonify("Universities created"), 201

@app.route("/university/<string:spec>", methods=['GET'])
def university_get(spec):
	if request.method == 'GET':
		#spec must be specified
		if spec == None:
			return jsonify("Specify speciality (spec)"), 400

		#реализовать коннект к sol, использовать функцию get_all_students_for_speciality
		#передать ей spec, вывод записать в ret
		ret = BCUSE_university.functions.get_all_students_for_speciality(spec).call()
		
		return jsonify(ret), 200

@app.route("/university/", methods=['POST'])
def university_post():
	if request.method == 'POST':
		#POST request example
		#{"login": "Asd", "spec": "polit"}
		
		login = request.form.get('login')
		if login is None:
			return jsonify("Specify login"), 400
		address = students[login][1]
		
		spec = request.form.get('spec')
		if spec is None:
			return jsonify("Specify speciality (spec)"), 400

		#реализовать коннект к sol, использовать функцию add_student
		#передать ей address и spec
		BCUSE_university.functions.add_student(address, spec).call()
		
		return jsonify("Student created"), 201

if __name__ == "__main__":
    app.run(debug=True)