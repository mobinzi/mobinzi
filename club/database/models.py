from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Date,DateTime,TIMESTAMP
from connection import Connection
from sqlalchemy.sql.functions import func

Base = declarative_base()

class Student(Base):
    __tablename__ = "student"
    memberId =Column(Integer,primary_key=True,autoincrement=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    birth_date = Column(Date) 
    image = Column(String(255))
    updated_at = Column(TIMESTAMP,server_default=func.now(),onupdate=func.current_timestamp())

    def __init__(self, first, last, birth, image,club_id):
        self.first_name = first
        self.last_name = last
        self.birth_date = birth
        self.image =image
        self.club_id = club_id
################################################################
    def __str__(self):
        return self.first_name+" "+self.last_name        





engine = Connection().get_connection()
Base.metadata.create_all(engine,checkfirst=True)

