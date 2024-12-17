from sqlalchemy.exc import DataError  # type: ignore
import pytest  # type: ignore
from flask import url_for  # type: ignore

from app.modules.auth.services import AuthenticationService
from app.modules.auth.repositories import UserRepository
from app.modules.profile.repositories import UserProfileRepository


@pytest.fixture(scope="module")
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    """
    with test_client.application.app_context():

        # Add HERE new elements to the database that you want to exist in the test context.
        # DO NOT FORGET to use db.session.add(<element>) and db.session.commit() to save the data.
        pass
    yield test_client


def test_login_success(test_client):
    response = test_client.post(
        "/login", data=dict(email="test@example.com", password="test1234"), follow_redirects=True
    )

    assert response.request.path != url_for("auth.login"), "Login was unsuccessful"

    test_client.get("/logout", follow_redirects=True)


def test_login_unsuccessful_bad_email(test_client):
    response = test_client.post(
        "/login", data=dict(email="bademail@example.com", password="test1234"), follow_redirects=True
    )

    assert response.request.path == url_for("auth.login"), "Login was unsuccessful"

    test_client.get("/logout", follow_redirects=True)


def test_login_unsuccessful_bad_password(test_client):
    response = test_client.post(
        "/login", data=dict(email="test@example.com", password="basspassword"), follow_redirects=True
    )

    assert response.request.path == url_for("auth.login"), "Login was unsuccessful"

    test_client.get("/logout", follow_redirects=True)


def test_signup_unsuccessful_user_no_name(test_client):
    response = test_client.post(
        "/signup", data=dict(surname="Foo", email="test@example.com", password="test1234",
                             is_developer=False), follow_redirects=True
    )
    assert response.request.path == url_for("auth.show_signup_form"), "Signup was unsuccessful"
    assert b"This field is required" in response.data, response.data


def test_signup_unsuccessful_user_no_surname(test_client):
    response = test_client.post(
        "/signup", data=dict(name="Foo", email="test@example.com", password="test1234",
                             is_developer=False), follow_redirects=True
    )
    assert response.request.path == url_for("auth.show_signup_form"), "Signup was unsuccessful"
    assert b"This field is required" in response.data, response.data


def test_signup_unsuccessful_user_no_email(test_client):
    response = test_client.post(
        "/signup", data=dict(name="Foo", surname="Faa", email="test@example.com",
                             is_developer=False), follow_redirects=True
    )
    assert response.request.path == url_for("auth.show_signup_form"), "Signup was unsuccessful"
    assert b"This field is required" in response.data, response.data


def test_signup_unsuccessful_user_no_password(test_client):
    response = test_client.post(
        "/signup", data=dict(name="Foo", surname="Faa", password="test1234",
                             is_developer=False), follow_redirects=True
    )
    assert response.request.path == url_for("auth.show_signup_form"), "Signup was unsuccessful"
    assert b"This field is required" in response.data, response.data


def test_signup_user_unsuccessful(test_client):
    email = "test@example.com"
    response = test_client.post(
        "/signup", data=dict(name="Test", surname="Foo", email=email, password="test1234",
                             is_developer=False), follow_redirects=True
    )
    assert response.request.path == url_for("auth.show_signup_form"), "Signup was unsuccessful"
    assert f"Email {email} in use".encode("utf-8") in response.data


def test_signup_user_successful(test_client):
    response = test_client.post(
        "/signup",
        data=dict(name="Foo", surname="Example", email="foo@example.com", password="foo1234",
                  is_developer=False),
        follow_redirects=True,
    )
    assert response.request.path == url_for("public.index"), "Signup was unsuccessful"


def test_signup_succesful_no_developer_user(test_client):
    response = test_client.post(
        "/signup",
        data={
            "name": "Test",
            "surname": "Foo",
            "email": "service_test@example.com",
            "password": "test1234"
        },
        follow_redirects=True,
    )
    assert response.request.path == url_for("public.index"), "Signup was successful"


def test_signup_successful_developer_user(test_client):
    response = test_client.post(
        "/signup",
        data={
            "name": "Test",
            "surname": "Foo",
            "email": "service_test@example.com",
            "is_developer": False,
            "password": "test1234"
        },
        follow_redirects=True,
    )
    assert response.request.path == url_for("public.index"), "Signup was successful"


def test_service_create_with_profile_success(clean_database):
    data = {
        "name": "Test",
        "surname": "Foo",
        "email": "service_test@example.com",
        "is_developer": True,
        "password": "test1234"
    }

    AuthenticationService().create_with_profile(**data)

    assert UserRepository().count() == 1
    assert UserProfileRepository().count() == 1


def test_service_create_with_profile_fail_no_name(clean_database):
    data = {
        "name": "",
        "surname": "Foo",
        "email": "test@example.com",
        "password": "1234"
    }

    with pytest.raises(ValueError, match="Name is required."):
        AuthenticationService().create_with_profile(**data)

    assert UserRepository().count() == 0
    assert UserProfileRepository().count() == 0


def test_service_create_with_profile_fail_name_too_long(clean_database):
    wrong_value = "4z8K5uX2pD1rM9tQ3sVfL6oYwIhE7gCkUqJbTz0aWvOxlPjNnF"  # A 50-character_string
    wrong_value = wrong_value + wrong_value + "a"
    data = {
        "name": wrong_value,
        "surname": "Foo",
        "email": "test@example.com",
        "password": "1234"
    }

    with pytest.raises(DataError, match="Data too long for column 'name' at row 1"):
        AuthenticationService().create_with_profile(**data)

    assert UserRepository().count() == 0
    assert UserProfileRepository().count() == 0


def test_service_create_with_profile_fail_no_surname(clean_database):
    data = {
        "name": "Test",
        "surname": "",
        "email": "test@example.com",
        "password": "1234"
    }

    with pytest.raises(ValueError, match="Surname is required."):
        AuthenticationService().create_with_profile(**data)

    assert UserRepository().count() == 0
    assert UserProfileRepository().count() == 0


def test_service_create_with_profile_fail_surname_too_long(clean_database):
    wrong_value = "4z8K5uX2pD1rM9tQ3sVfL6oYwIhE7gCkUqJbTz0aWvOxlPjNnF"  # A 50-character_string
    wrong_value = wrong_value + wrong_value + "a"
    data = {
        "name": "Test",
        "surname": wrong_value,
        "email": "test@example.com",
        "password": "1234"
    }

    with pytest.raises(DataError, match="Data too long for column 'surname' at row 1"):
        AuthenticationService().create_with_profile(**data)

    assert UserRepository().count() == 0
    assert UserProfileRepository().count() == 0


def test_service_create_with_profile_fail_no_email(clean_database):
    data = {
        "name": "Test",
        "surname": "Foo",
        "email": "",
        "password": "1234"
    }

    with pytest.raises(ValueError, match="Email is required."):
        AuthenticationService().create_with_profile(**data)

    assert UserRepository().count() == 0
    assert UserProfileRepository().count() == 0


def test_service_create_with_profile_fail_email_too_long(clean_database):
    wrong_value = "4z8K5uX2pD1rM9tQ3sVfL6oYwIhE7gCkUqJbTz0aWvOxlPjNnF0yHcZpYdR8m2sK"  # A 64-character_string
    wrong_end = "4z8K5uX2pD1rM9tQ3sVfL6oYwIhE7gCkUqJbTz0aWvOxlPjNnF0ya@example.com"  # A 65-character_string
    wrong_value = wrong_value + wrong_value + wrong_value + wrong_end
    data = {
        "name": "Test",
        "surname": "Foo",
        "email": wrong_value,
        "password": "1234"
    }

    with pytest.raises(DataError, match="Data too long for column 'email' at row 1"):
        AuthenticationService().create_with_profile(**data)

    assert UserRepository().count() == 0
    assert UserProfileRepository().count() == 0


def test_service_create_with_profile_fail_no_password(clean_database):
    data = {
        "name": "Test",
        "surname": "Foo",
        "email": "test@example.com",
        "password": ""
    }

    with pytest.raises(ValueError, match="Password is required."):
        AuthenticationService().create_with_profile(**data)

    assert UserRepository().count() == 0
    assert UserProfileRepository().count() == 0
