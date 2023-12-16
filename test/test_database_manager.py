import pytest
from freezegun import freeze_time
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from src.database_manager import (
    create_database,
    create_user_table,
    add_user,
    query_user,
)


# Fixture to setup test environment
@pytest.fixture
def setup_environment():
    engine = create_database()
    Session = sessionmaker(bind=engine)
    session = Session()
    yield engine, session


# Fixture to create table
@pytest.fixture
def create_table(setup_environment):
    engine = setup_environment[0]
    User = create_user_table(engine)
    yield User


# Testing adding and quering data
@freeze_time("2023-12-14 23:31:00")
def test_create_user(setup_environment, create_table):
    session = setup_environment[1]
    User = create_table
    # Adding a new user to database
    new_user = User(name="John Doe", date_time=datetime.now())
    if add_user(session, new_user):
        pass
    # Checking if the data added successfully
    queried_user = query_user(session, User, "John Doe").date_time
    assert queried_user == "2023-12-14 23:31:00"
