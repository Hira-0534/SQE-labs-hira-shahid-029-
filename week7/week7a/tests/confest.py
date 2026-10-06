import auth
import pytest
pytest.fixture(autouse=True)
def fresh_store():
    """give every test a clean in memory store to work with."""
    auth.initialize_store()