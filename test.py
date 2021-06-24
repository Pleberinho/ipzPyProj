from requests import post, get, put, delete
from pprint import pprint

print(1, post('http://localhost:5000/api/employee',
              json={'name': 'Ігор',
                    'surname': "111",
                    'middle_name': "222",
                    'address': 'Ukraine',
                    'email': 'example@gmail.com',
                    'phone': 380900000,
                    'salary': 150,
                    'category_id': 1,
                    }).json())
print(2, put('http://localhost:5000/api/employee/1',
             json={'name': 'Ігор',
                   'surname': "111",
                   'middle_name': "222",
                   'address': 'Ukraine',
                   'email': 'example@gmail.com',
                   'phone': 380900000,
                   'salary': 5000,
                   'category_id': 4,
                   }).json())
pprint((3, get('http://localhost:5000/api/employee/1').json()))
print(4, delete('http://localhost:5000/api/employee/1').json())
pprint((5, get('http://localhost:5000/api/employee').json()))
print(6, post('http://localhost:5000/api/employee',
              json={'name': 'Олег',
                    'surname': "111",
                    'middle_name': "222",
                    'address': 'Ukraine',
                    'email': 'example@gmail.com',
                    'phone': 380900000,
                    'salary': 150,
                    'category_id': 1,
                    }).json())
print(7, post('http://localhost:5000/api/employee',
              json={'name': 'Петро',
                    'surname': "321",
                    'middle_name': "123",
                    'address': 'Russia',
                    'email': 'example2@gmail.com',
                    'phone': 380900001,
                    'salary': 150,
                    'category_id': 1,
                    }).json())
pprint((8, get('http://localhost:5000/api/employee').json()))
