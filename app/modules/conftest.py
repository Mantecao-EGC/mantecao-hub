import pytest

from app import create_app, db
from app.modules.auth.models import User
from app.modules.dataset.models import (Author, DataSet, DSDownloadRecord, DSMetaData, DSMetrics, PublicationType)



@pytest.fixture(scope='session')
def test_app():
    """ Create and configure a new app instance for each test session. """
    test_app = create_app('testing')

    with test_app.app_context():
        # Imprimir los blueprints registrados
        print("TESTING SUITE (1): Blueprints registrados:", test_app.blueprints)
        yield test_app


@pytest.fixture(scope='module')
def test_client(test_app):

    with test_app.test_client() as testing_client:
        with test_app.app_context():
            print("TESTING SUITE (2): Blueprints registrados:", test_app.blueprints)

            db.drop_all()
            db.create_all()
            """
            The test suite always includes the following user in order to avoid repetition
            of its creation
            """
            user_test = User(email='test@example.com', password='test1234', is_developer=True)
            db.session.add(user_test)
            db.session.commit()        
            user1 = User(email="user1@testing.com", password="1234", is_developer=False)
        user2 = User(email="user2@testing.com", password="1234", is_developer=False)
        user3 = User(email="user3@testing.com", password="1234", is_developer=False)
        user4 = User(email="user4@testing.com", password="1234", is_developer=False)
        user5 = User(email="user5@testing.com", password="1234", is_developer=False)
        db.session.add_all([user1, user2, user3, user4, user5])
        db.session.commit()

        ds_metrics1 = DSMetrics(number_of_models="5", number_of_features="100")
        ds_metrics2 = DSMetrics(number_of_models="8", number_of_features="400")
        ds_metrics3 = DSMetrics(number_of_models="20", number_of_features="200")
        ds_metrics4 = DSMetrics(number_of_models="10", number_of_features="150")
        ds_metrics5 = DSMetrics(number_of_models="1", number_of_features="10")
        db.session.add_all(
            [ds_metrics1, ds_metrics2, ds_metrics3, ds_metrics4, ds_metrics5]
        )
        db.session.commit()

        ds_meta1 = DSMetaData(
            title="Dataset 1",
            dataset_doi="doi1",
            ds_metrics_id=ds_metrics1.id,
            description="Number1",
            publication_type=PublicationType.BOOK,
        )
        ds_meta2 = DSMetaData(
            title="Dataset 2",
            dataset_doi="doi2",
            ds_metrics_id=ds_metrics2.id,
            description="Number2",
            publication_type=PublicationType.BOOK,
        )
        ds_meta3 = DSMetaData(
            title="Dataset 3",
            dataset_doi="doi3",
            ds_metrics_id=ds_metrics3.id,
            description="Number3",
            publication_type=PublicationType.REPORT,
        )
        ds_meta4 = DSMetaData(
            title="Dataset 4",
            dataset_doi="doi4",
            ds_metrics_id=ds_metrics4.id,
            description="Number4",
            publication_type=PublicationType.BOOK,
        )
        ds_meta5 = DSMetaData(
            title="Dataset 5",
            dataset_doi="doi5",
            ds_metrics_id=ds_metrics5.id,
            description="Number5",
            publication_type=PublicationType.BOOK,
        )
        db.session.add_all([ds_meta1, ds_meta2, ds_meta3, ds_meta4, ds_meta5])
        db.session.commit()

        author1 = Author(name="Author1", ds_meta_data_id=ds_meta1.id)
        author2 = Author(name="Author2", ds_meta_data_id=ds_meta2.id)
        author3 = Author(name="Author3", ds_meta_data_id=ds_meta3.id)
        author4 = Author(name="Author4", ds_meta_data_id=ds_meta4.id)
        author5 = Author(name="Author5", ds_meta_data_id=ds_meta5.id)
        db.session.add_all([author1, author2, author3, author4, author5])
        db.session.commit()

        dataset1 = DataSet(user_id=user1.id, ds_meta_data_id=ds_meta1.id)
        dataset2 = DataSet(user_id=user2.id, ds_meta_data_id=ds_meta2.id)
        dataset3 = DataSet(user_id=user3.id, ds_meta_data_id=ds_meta3.id)
        dataset4 = DataSet(user_id=user4.id, ds_meta_data_id=ds_meta4.id)
        dataset5 = DataSet(user_id=user5.id, ds_meta_data_id=ds_meta5.id)
        db.session.add_all([dataset1, dataset2, dataset3, dataset4, dataset5])
        db.session.commit()

        download_record1 = DSDownloadRecord(
            dataset_id=dataset1.id, download_cookie="cookie1"
        )
        download_record2 = DSDownloadRecord(
            dataset_id=dataset2.id, download_cookie="cookie2"
        )
        download_record3 = DSDownloadRecord(
            dataset_id=dataset3.id, download_cookie="cookie3"
        )
        download_record4 = DSDownloadRecord(
            dataset_id=dataset4.id, download_cookie="cookie4"
        )
        download_record5 = DSDownloadRecord(
            dataset_id=dataset5.id, download_cookie="cookie5"
        )
        download_record6 = DSDownloadRecord(
            dataset_id=dataset1.id, download_cookie="cookie6"
        )
        download_record7 = DSDownloadRecord(
            dataset_id=dataset1.id, download_cookie="cookie7"
        )
        download_record8 = DSDownloadRecord(
            dataset_id=dataset2.id, download_cookie="cookie8"
        )
        download_record9 = DSDownloadRecord(
            dataset_id=dataset3.id, download_cookie="cookie9"
        )
        download_record10 = DSDownloadRecord(
            dataset_id=dataset4.id, download_cookie="cookie10"
        )
        db.session.add_all(
            [
                download_record1,
                download_record2,
                download_record3,
                download_record4,
                download_record5,
                download_record6,
                download_record7,
                download_record8,
                download_record9,
                download_record10,
            ]
        )
        db.session.commit()

        print("Rutas registradas:")
        for rule in test_app.url_map.iter_rules():
            print(rule)
        yield testing_client

        db.session.remove()
        db.drop_all()


@pytest.fixture(scope='function')
def clean_database():
    db.session.remove()
    db.drop_all()
    db.create_all()
    yield
    db.session.remove()
    db.drop_all()
    db.create_all()


def login(test_client, email, password):
    """
    Authenticates the user with the credentials provided.

    Args:
        test_client: Flask test client.
        email (str): User's email address.
        password (str): User's password.

    Returns:
        response: POST login request response.
    """
    response = test_client.post('/login', data=dict(
        email=email,
        password=password
    ), follow_redirects=True)
    return response


def logout(test_client):
    """
    Logs out the user.

    Args:
        test_client: Flask test client.

    Returns:
        response: Response to GET request to log out.
    """
    return test_client.get('/logout', follow_redirects=True)
