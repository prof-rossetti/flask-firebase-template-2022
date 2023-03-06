
import pytest

from app.firebase_service import FirebaseService
from web_app import create_app

# see: https://flask.palletsprojects.com/en/2.1.x/testing/

@pytest.fixture(scope="module")
def test_firebase_service():
    # fixture scope module level to only initialize it once
    # to fix: "The default Firebase app already exists. This means you called 'initialize_app() more than once without providing an app name ..."
    return FirebaseService()

@pytest.fixture()
def test_client(test_firebase_service):
    # always passing the same firebase service will avoid initializing more than one, and avoid error
    app = create_app(firebase_service=test_firebase_service)
    app.config.update({"TESTING": True})
    return app.test_client()
