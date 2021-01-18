class student(Base):
    __tablename__="student"
    studentId= Column(Integer(),primary_key=True,autooincrement=True)
    name= column(String(50))
    family= Column(String(50))
    grade=

    def __init__(self,name=None,family=None,grade=None):
    self.name = name
    self.family = family
    self.grade = grade

engine= Connection().get_connection()
if not engine.dailect.has_table(engine,"student"):
    Base.metadata.create_all(engine,checkfirst)=True)
    print("Database Created")

else:
    print("Database{} exist!".format("student"))    