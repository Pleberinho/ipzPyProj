from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource
from data import db_session
from data.employee import Employee


api_bp = Blueprint("api", __name__)
api = Api(api_bp)


class EmployeeListApi(Resource):
    def get(self):
        session = db_session.create_session()
        all_employees = sorted(session.query(Employee).all(), key=lambda x: x.name)
        return jsonify({"employees": [emp.as_dict() for emp in all_employees], "success": "OK"})


class EmployeeAddApi(Resource):
    def post(self):
        session = db_session.create_session()
        try:
            employee = Employee()
            employee.name = request.json['name']
            employee.surname = request.json['surname']
            employee.middle_name = request.json['middle_name']
            employee.address = request.json['address']
            employee.email = request.json['email']
            employee.phone = int(request.json['phone'])
            employee.salary = int(request.json['salary'])
            employee.category_id = int(request.json['category_id'])
            session.add(employee)
            session.commit()
        except BaseException:
            return jsonify({'success': 'Bad request'})
        return jsonify({'success': 'OK'})


class EmployeeApi(Resource):
    def get(self, id):
        session = db_session.create_session()
        employee = session.query(Employee).filter(Employee.id == id).first()
        if not employee:
            return jsonify({'success': 'Employee not found'})
        return jsonify({"employees": employee.as_dict(), "success": "OK"})

    def put(self, id):
        if not request.json:
            return jsonify({'success': 'Empty request'})
        session = db_session.create_session()
        employee = session.query(Employee).filter(Employee.id == id).first()
        if not employee:
            return jsonify({'success': 'Employee not found'})
        try:
            employee.name = request.json['name'] if 'name' in request.json else employee.name
            employee.surname = request.json['surname'] if 'surname' in request.json else employee.surname
            employee.middle_name = \
                request.json['middle_name'] if 'middle_name' in request.json else employee.middle_name
            employee.address = request.json['address'] if 'address' in request.json else employee.address
            employee.email = request.json['email'] if 'email' in request.json else employee.email
            employee.phone = int(request.json['phone']) if 'phone' in request.json else employee.phone
            employee.salary = int(request.json['salary']) if 'salary' in request.json else employee.salary
            employee.category_id =\
                int(request.json['category_id']) if 'category_id' in request.json else employee.category_id
            session.commit()
        except BaseException:
            return jsonify({'success': 'Bad request'})
        return jsonify({'success': 'OK'})

    def delete(self, id):
        session = db_session.create_session()
        employee = session.query(Employee).where(Employee.id == id).first()
        if not employee:
            return jsonify({'success': 'Employee not found'})
        session.delete(employee)
        session.commit()
        return jsonify({'success': 'OK'})


api.add_resource(EmployeeApi, "/employee/<int:id>")
api.add_resource(EmployeeListApi, "/employee")
api.add_resource(EmployeeAddApi, "/employee")
