from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

def create_database():
    """
    Creating an SQLite database in memory for this example
    """
    engine = create_engine('sqlite:///:memory:', echo=False)
    return engine

def create_user_table(engine):
    """
    Define a simple User model
    """
    Base = declarative_base()
    class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
        name = Column(String(50))
        date_time = Column(String(50))

    # Create the table in the database
    Base.metadata.create_all(engine)

    return User

def add_user(session, user):
    """
    Add a new user to the database
    """
    session.add(user)
    session.commit()

def query_user(session, User, name):
    """
    Query the database to retrieve the user
    """
    queried_user = session.query(User).filter_by(name=name).first()
    return queried_user
