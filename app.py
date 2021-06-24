from flask import Flask, Blueprint
from flask import render_template, abort, request, make_response, redirect
from data import db_session
from data.employee import Employee
from data.category import Category
from data.employee_form import EmployeeForm
from api import employee_api


app = Flask(__name__)
app.config['SECRET_KEY'] = 'EWvebEMHMJsUKxgfNUSZmAnuyqcecd'
app.config['JSON_AS_ASCII'] = False
core_bp = Blueprint("core", __name__, template_folder="templates")


def init_defaults():
    session = db_session.create_session()
    if session.query(Category).first() is None:
        titles = ["Trainee", "Junior", "Middle", "Senior"]
        for title in titles:
            ctg = Category(title=title)
            session.add(ctg)
        session.commit()


@core_bp.route("/", methods=["GET"])
def index():
    session = db_session.create_session()
    employees = session.query(Employee).all()
    return make_response(render_template('employee_list.html', title='Список працівників', employees=employees))


@core_bp.route("/employee", methods=["GET", "POST"])
def add_employee():
    form = EmployeeForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        employee = Employee()
        employee.name = form.name.data
        employee.surname = form.surname.data
        employee.middle_name = form.middle_name.data
        employee.address = form.address.data
        employee.email = form.email.data
        employee.phone = form.phone.data
        employee.salary = form.salary.data
        employee.category_id = form.category.data

        session.add(employee)
        session.commit()
        return redirect("/")
    return make_response(render_template('employee.html', title='Добавити працівника', form=form))


@core_bp.route("/employee/<int:id>", methods=["GET", "POST"])
def edit_employee(id):
    form = EmployeeForm()
    if request.method == "GET":
        session = db_session.create_session()
        employee = session.query(Employee).filter(Employee.id == id).first()
        if employee:
            form.name.data = employee.name
            form.surname.data = employee.surname
            form.middle_name.data = employee.middle_name
            form.address.data = employee.address
            form.email.data = employee.email
            form.phone.data = employee.phone
            form.salary.data = employee.salary
            form.category.data = employee.category_id
            form.category.default = employee.category_id
        else:
            abort(404)
    if form.validate_on_submit():
        session = db_session.create_session()
        employee = session.query(Employee).filter(Employee.id == id).first()
        if employee:
            employee.name = form.name.data
            employee.surname = form.surname.data
            employee.middle_name = form.middle_name.data
            employee.address = form.address.data
            employee.email = form.email.data
            employee.phone = form.phone.data
            employee.salary = form.salary.data
            employee.category_id = form.category.data
            session.commit()
            return redirect("/")
        else:
            abort(404)
    return make_response(render_template('employee.html', title='Редагування працівника', form=form))


db_session.global_init("db.sqlite")
app.register_blueprint(core_bp)
app.register_blueprint(employee_api.api_bp, url_prefix='/api')
init_defaults()
