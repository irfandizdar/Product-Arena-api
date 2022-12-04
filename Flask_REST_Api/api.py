from flask import Flask, make_response, jsonify, request
import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///api.db')


table = db['doctors']


def fetch_db(doctor_id):  
    return table.find_one(doctor_id=doctor_id)


def fetch_db_all():
    doctors = []
    for doctor in table:
        doctors.append(doctor)
    return doctors


@app.route('/api/db_populate', methods=['GET'])
def db_populate():
    table.insert({
        "doctor_id": "1",
        "firstname": "Doctor Name1",
        "lastname": "Doctor Name1",
        "username": "username1",
        "password": "123456"
    })

    table.insert({
        "doctor_id": "2",
        "firstname": "Doctor Name2",
        "lastname": "Doctor Name2",
        "username": "username2",
        "password": "12345689"

    })
    return make_response(jsonify(fetch_db_all()),
                         200)


table = db['appointments']


def fetch_db(appointment_id):  
    return table.find_one(appointment_id=appointment_id)


def fetch_db_all():
    appointments = []
    for patient in table:
        appointments.append(patient)
    return appointments


@app.route('/api/db_populate_appointments', methods=['GET'])
def db_populate_appointments():
    table.insert({
        "appointment_id": "1",
        "date": "2022-12-06",
        "time": "10:30",
        "patient_id": 1,
        "doctor_id": 2
    })

    table.insert({
        "appointment_id": "2",
        "date": "2022-12-10",
        "time": "12:50",
        "patient_id": 2,
        "doctor_id": 1

    })
    return make_response(jsonify(fetch_db_all()),
                         200)

table = db['patients']


def fetch_db(patient_id):  
    return table.find_one(patient_id=patient_id)


def fetch_db_all():
    patients = []
    for patient in table:
        patients.append(patient)
    return patients


@app.route('/api/db_populate_patients', methods=['GET'])
def db_populate_patients():
    table.insert({
        "patient_id": "1",
        "firstname": "Patient Name1",
        "lastname": "PatientLast Name1",
        "username": "username1",
        "password": "123456"
    })

    table.insert({
        "patient_id": "2",
        "firstname": "Patient Name2",
        "lastname": "PatientLast Name2",
        "username": "username2",
        "password": "12345689"

    })
    return make_response(jsonify(fetch_db_all()),
                         200)




#**************ROUTES FOR DOCTORS**************


@app.route('/api/doctors', methods=['GET', 'POST'])
def api_doctors():
    if request.method == "GET":
        return make_response(jsonify(fetch_db_all()), 200)
    elif request.method == 'POST':
        content = request.json
        doctor_id = content['doctor_id']
        table.insert(content)
        return make_response(jsonify(fetch_db(doctor_id)), 201) 


@app.route('/api/doctors/<doctor_id>', methods=['GET', 'PUT', 'DELETE'])
def api_each_doctor(doctor_id):
    if request.method == "GET":
        doctor_obj = fetch_db(doctor_id)
        if doctor_obj:
            return make_response(jsonify(doctor_obj), 200)
        else:
            return make_response(jsonify(doctor_obj), 404)
    elif request.method == "PUT":  
        content = request.json
        table.update(content, ['doctor_id'])

        book_obj = fetch_db(doctor_id)
        return make_response(jsonify(doctor_obj), 200)
    elif request.method == "DELETE":
        table.delete(id=doctor_id)

        return make_response(jsonify({}), 204)


        #**************ROUTES FOR PATIENTS**************


@app.route('/api/patients', methods=['GET', 'POST'])
def api_patients():
    if request.method == "GET":
        return make_response(jsonify(fetch_db_all()), 200)
    elif request.method == 'POST':
        content = request.json
        patient_id = content['patient_id']
        table.insert(content)
        return make_response(jsonify(fetch_db(patient_id)), 201) 


@app.route('/api/patients/<patient_id>', methods=['GET', 'PUT', 'DELETE'])
def api_each_patient(patient_id):
    if request.method == "GET":
        patient_obj = fetch_db(patient_id)
        if patient_obj:
            return make_response(jsonify(patient_obj), 200)
        else:
            return make_response(jsonify(patient_obj), 404)
    elif request.method == "PUT":  
        content = request.json
        table.update(content, ['doctor_id'])

        patient_obj = fetch_db(patient_id)
        return make_response(jsonify(patient_obj), 200)
    elif request.method == "DELETE":
        table.delete(id=patient_id)

        return make_response(jsonify({}), 204)



         #**************ROUTES FOR APPOINTMENTS**************


@app.route('/api/appointments', methods=['GET', 'POST'])
def api_appointments():
    if request.method == "GET":
        return make_response(jsonify(fetch_db_all()), 200)
    elif request.method == 'POST':
        content = request.json
        appointment_id = content['appointment_id']
        table.insert(content)
        return make_response(jsonify(fetch_db(appointment_id)), 201) 


@app.route('/api/appointments/<appointment_id>', methods=['GET', 'PUT', 'DELETE'])
def api_each_appointment(appointment_id):
    if request.method == "GET":
        appointment_obj = fetch_db(appointment_id)
        if appointment_obj:
            return make_response(jsonify(appointment_obj), 200)
        else:
            return make_response(jsonify(appointment_obj), 404)
    elif request.method == "PUT":  
        content = request.json
        table.update(content, ['appointment_id'])

        appointment_obj = fetch_db(appointment_id)
        return make_response(jsonify(appointment_obj), 200)
    elif request.method == "DELETE":
        table.delete(id=appointment_id)

        return make_response(jsonify({}), 204)


if __name__ == '__main__':
    app.run(debug=True)