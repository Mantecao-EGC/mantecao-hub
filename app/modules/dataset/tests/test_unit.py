import pytest
from app import db
from app.modules.auth.models import User
from app.modules.dataset.models import (Author, DataSet, DSDownloadRecord, DSMetaData, DSMetrics, PublicationType)
from app.modules.dataset.repositories import AuthorRepository, DataSetRepository

author_repo = AuthorRepository()
dataset_repo = DataSetRepository()


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


def test_latest_synchro(test_client):
    datasets = dataset_repo.latest_synchronized()
    assert len(datasets) == 5
