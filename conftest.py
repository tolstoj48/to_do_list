import pytest
import datetime


@pytest.fixture
def notebook_mock():
        return {"First": ["textace", datetime.date.today(), datetime.date.today()]}