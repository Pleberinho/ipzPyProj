import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Employee(SqlAlchemyBase):
    __tablename__ = 'employee'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    middle_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=True)
    phone = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    salary = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    hiring_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    category_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("category.id"), nullable=True)
    category = orm.relation('Category', back_populates="employees")

    def __repr__(self):
        return f'id: {self.id}  name: {self.name}  surname: {self.surname}  middle_name: {self.middle_name}  ' \
               f'email: {self.email}  phone: {self.phone}  salary: {self.salary}  ' \
               f'hiring_date: {self.hiring_date}, category: {self.category.title}'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
