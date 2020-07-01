import pytest
from odpidentity.lib.users import check_password_complexity, check_consecutive_letters


@pytest.mark.parametrize('email,password', [
    ('lance@saeon.ac.za', 'abcABC12!@*09'),
    ('lance@saeon.ac.za', '--P--8x-----------'),
])
def test_valid_password(email, password):
    assert check_password_complexity(email, password) is True
