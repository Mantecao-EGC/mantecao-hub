import pytest

from app import db
from app.modules.auth.models import User
from app.modules.conftest import login, logout
from app.modules.profile.models import UserProfile


@pytest.fixture(scope="module")
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    for module testing (por example, new users)
    """
    with test_client.application.app_context():
        user_test = User(email='user@example.com', password='test1234', is_developer=False)
        db.session.add(user_test)
        db.session.commit()

        profile = UserProfile(user_id=user_test.id, name="Name", surname="Surname")
        db.session.add(profile)
        db.session.commit()

    yield test_client


def test_edit_profile_page_get(test_client):
    """
    Tests access to the profile editing page via a GET request.
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.get("/profile/edit")
    assert response.status_code == 200, "The profile editing page could not be accessed."
    assert b"Edit profile" in response.data, "The expected content is not present on the page"

    logout(test_client)


def test_edit_profile_unauthorized(test_client):
    """
    Tests that unauthorized users cannot access the profile editing page.
    """
    response = test_client.get("/profile/edit")
    assert response.status_code == 302, "Unauthorized access should redirect"


def test_update_profile_success(test_client):
    """
    Tests successful profile update with valid data.
    """
    login(test_client, "user@example.com", "test1234")

    response = test_client.post("/profile/edit", data={
        'name': 'John',
        'surname': 'Doe',
        'orcid': '0000-0002-1825-0097',
        'affiliation': 'Test University'
    })
    assert response.status_code == 302, "Profile update should redirect on success"

    # Verify database update
    user = User.query.filter_by(email='user@example.com').first()
    assert user.profile.name == 'John'
    assert user.profile.surname == 'Doe'

    logout(test_client)


def test_invalid_orcid_format(test_client):
    """
    Tests profile update with invalid ORCID format.
    """
    login(test_client, "user@example.com", "test1234")

    response = test_client.post("/profile/edit", data={
        'name': 'John',
        'surname': 'Doe',
        'orcid': '1234-5678-invalid',
        'affiliation': 'Test University'
    })
    assert response.status_code == 200, "Should return to form with errors"
    assert b'Invalid ORCID format' in response.data

    logout(test_client)


def test_missing_required_fields(test_client):
    """
    Tests profile update with missing required fields.
    """
    login(test_client, "user@example.com", "test1234")

    response = test_client.post("/profile/edit", data={
        'name': '',
        'surname': '',
        'orcid': '',
        'affiliation': 'Test University'
    })
    assert response.status_code == 200, "Should return to form with errors"
    assert b'This field is required' in response.data

    logout(test_client)


def test_profile_summary_page_access(test_client):
    """
    Tests access to profile summary page.
    """
    login(test_client, "user@example.com", "test1234")

    response = test_client.get("/profile/summary")
    assert response.status_code == 200
    assert b'User profile' in response.data

    logout(test_client)


def test_profile_summary_unauthorized(test_client):
    """
    Tests that unauthorized users cannot access the profile summary page.
    """
    response = test_client.get("/profile/summary")
    assert response.status_code == 302, "Unauthorized access should redirect"


def test_affiliation_length_validation(test_client):
    """
    Tests affiliation field length validation.
    """
    login(test_client, "user@example.com", "test1234")

    response = test_client.post("/profile/edit", data={
        'name': 'John',
        'surname': 'Doe',
        'orcid': '0000-0002-1825-0097',
        'affiliation': 'A' * 101  # Exceeds max length of 100
    })
    assert response.status_code == 200
    assert b'Field must be between 5 and 100 characters long' in response.data

    logout(test_client)


def test_short_affiliation(test_client):
    """
    Tests profile update with too short affiliation.
    """
    login(test_client, "user@example.com", "test1234")

    response = test_client.post("/profile/edit", data={
        'name': 'John',
        'surname': 'Doe',
        'orcid': '0000-0002-1825-0097',
        'affiliation': 'ABC'  # Less than minimum length of 5
    })
    assert response.status_code == 200
    assert b'Field must be between 5 and 100 characters long' in response.data

    logout(test_client)


def test_valid_orcid_format(test_client):
    """
    Tests profile update with valid ORCID format.
    """
    login(test_client, "user@example.com", "test1234")

    response = test_client.post("/profile/edit", data={
        'name': 'John',
        'surname': 'Doe',
        'orcid': '0000-0002-1825-0097',
        'affiliation': 'Test University'
    })
    assert response.status_code == 302

    user = User.query.filter_by(email='user@example.com').first()
    assert user.profile.orcid == '0000-0002-1825-0097'

    logout(test_client)


def test_empty_optional_fields(test_client):
    """
    Tests profile update with empty optional fields.
    """
    login(test_client, "user@example.com", "test1234")

    response = test_client.post("/profile/edit", data={
        'name': 'John',
        'surname': 'Doe',
        'orcid': '',
        'affiliation': ''
    })
    assert response.status_code == 302

    user = User.query.filter_by(email='user@example.com').first()
    assert user.profile.orcid is None or user.profile.orcid == ''
    assert user.profile.affiliation is None or user.profile.affiliation == ''

    logout(test_client)


def test_profile_data_persistence(test_client):
    """
    Tests if profile data persists correctly after updates.
    """
    login(test_client, "user@example.com", "test1234")

    # First update
    response = test_client.post("/profile/edit", data={
        'name': 'John',
        'surname': 'Doe',
        'orcid': '0000-0002-1825-0097',
        'affiliation': 'Test University'
    })
    assert response.status_code == 302, "First update should redirect on success"

    # Verify first update
    user = User.query.filter_by(email='user@example.com').first()
    assert user.profile.name == 'John'
    assert user.profile.affiliation == 'Test University'

    # Second update with partial data
    response = test_client.post("/profile/edit", data={
        'name': 'Johnny',
        'surname': 'Doe',
        'orcid': '0000-0002-1825-0097',
        'affiliation': 'Test University Updated'
    })
    assert response.status_code == 302, "Second update should redirect on success"

    # Verify second update
    user = User.query.filter_by(email='user@example.com').first()
    assert user.profile.name == 'Johnny'
    assert user.profile.affiliation == 'Test University Updated'
    assert user.profile.orcid == '0000-0002-1825-0097'

    logout(test_client)


def test_name_max_length_validation(test_client):
    """
    Tests name field maximum length validation (100 characters).
    """
    login(test_client, "user@example.com", "test1234")

    response = test_client.post("/profile/edit", data={
        'name': 'A' * 101,  # Exceeds max length of 100
        'surname': 'Doe',
        'orcid': '0000-0002-1825-0097',
        'affiliation': 'Test University'
    })
    assert response.status_code == 200
    assert b'Field cannot be longer than 100 characters' in response.data

    logout(test_client)


def test_surname_max_length_validation(test_client):
    """
    Tests surname field maximum length validation (100 characters).
    """
    login(test_client, "user@example.com", "test1234")

    response = test_client.post("/profile/edit", data={
        'name': 'John',
        'surname': 'D' * 101,  # Exceeds max length of 100
        'orcid': '0000-0002-1825-0097',
        'affiliation': 'Test University'
    })
    assert response.status_code == 200
    assert b'Field cannot be longer than 100 characters' in response.data

    logout(test_client)
