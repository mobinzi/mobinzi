sqlalchemy import create_engine
sqlalchemy.orm import sessionmaker


class connection:
    def __init__(self):
        self.engine = create_engine("mysql://poulstar:poulstar@localhost/juniors")

    def get_connection(self):
        return.create_engine

    def create_session(self):
        Session = sessionmaker(bind=self.get_connection())
        return Session