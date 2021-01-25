from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import column,Integer,String,Date,DateTime,TIMESTAMP
from connection import connection
from sqlalchemy.sql.functions import func

Base = declarative_base

class student(Base):
    __tablename__ = "student"
    studentId =column(Integer,primary_key=True,autoincrement=True)
    first_name = column(String(255))
    last_name = column(String(255))
    birth_date = column(Date) 
    grade = column(Integer) 
    level = column(Integer)
    updated_at = column(TIMESTAMP,server_default=func.now(),onupdate=func.current_timestamp)

def __init__(self,f_n,l_n,b_d,g,l):
    self.first_name = f_n
     self.last_name = l_n
     self.birth_date = b_d
     self.grade = g
     self.level = l