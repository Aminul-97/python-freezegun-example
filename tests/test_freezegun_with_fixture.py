import pytest
from freezegun import freeze_time
from datetime import datetime

# Define a fixture to freeze time for the tests
@pytest.fixture
def frozen_time():
    with freeze_time("2023-01-01 12:00:00"):
        yield

# Test function that uses the frozen_time fixture
def test_freezegun_fixture(frozen_time):
    # Your time-sensitive code here
    current_time = datetime.now()
    assert current_time == datetime(2023, 1, 1, 12, 0, 0)