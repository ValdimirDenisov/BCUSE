from flask import request, jsonify
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

students = [
	"Asd": ["Asd", "0xAsd"],
	"Qwe": ["Qwe", "0xQwe"],
	"Zxc": ["Zxc", "0xZxc"]
]

@app.route("/student/<string:university>", methods=['GET'])
def student_get(university):
	if request.method == 'GET':
		#university must be specified
		if university == None:
			return jsonify("Specify university"), 400

		#реализовать коннект к sol, использовать функцию get_all_information_for_university
		#передать ей university, вывод записать в ret
		
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

		specialities = request.form.get('specialities')
		if specialities is None:
			return jsonify("Specify specialities"), 400
		
		#реализовать коннект к sol, использовать функцию set_data
		#передать ей universities, specialities, login, password, вывод записать в ret

		return jsonify("Universities created"), 201

@app.route("/university/<string:spec>", methods=['GET'])
def university_get(spec):
	if request.method == 'GET':
		#spec must be specified
		if spec == None:
			return jsonify("Specify speciality (spec)"), 400

		#реализовать коннект к sol, использовать функцию get_all_students_for_speciality
		#передать ей spec, вывод записать в ret
		
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
		
		return jsonify("Student created"), 201

if __name__ == "__main__":
    app.run(debug=True)