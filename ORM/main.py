from connection import Connection
from sqlalchemy.sql.schema import MetaData
from sqlalchemy.sql import table, insert
from models import Student


session= Connection().create_session()

person1 = Student("mobin","ziaei","2004-01-03",98,30)

session.add(person1)
session.commit()

persons = session.query(Student).filter(Student.first_name == "mobin")
for person in persons:
    print(person)

