import pytest
from odpidentity.lib.users import check_password_complexity, check_consecutive_letters

@pytest.mark.parametrize("email, password, expected", [
    ('lance@saeon.ac.za', 'abcABC12!@*09', True),
    ('lance@saeon.ac.za', '--P--8x-----------', True),
    ('lance@saeon.ac.za', 'asdQweTest123#', True),
    ('lance@saeon.ac.za', '9135YOFJH#$xcva', True),
    ('lance@saeon.ac.za', 'E0$yu8M&4JDbC', True),
    ('lance@saeon.ac.za', '$TCd_M5A7Z@i$', True),
    ('lance@saeon.ac.za', 'RZm32COf2!L6P', True),
    ('lance@saeon.ac.za', 'a@!8Qm%=UVJ|m', True),
    ('lance@saeon.ac.za', 'Cjly_47j%2uWy', True),
    ('lance@saeon.ac.za', 'c4Qdutfn6&f-?', True),
    
    ('lance@saeon.ac.za', 'lanceasdTest123', False),
    ('lance@saeon.ac.za', 'asdaasdTest123', False),
    ('lance@saeon.ac.za', '15687asddewq**', False),
    ('lance@saeon.ac.za', 'saeonQweRtw&87', False),
    ('lance@saeon.ac.za', '159qweQwe!', False),
    ('lance@saeon.ac.za', 'ASD!@1593QWEEE', False),
    ('lance@saeon.ac.za', '1234567891234', False),
    ('lance@saeon.ac.za', 'asdTEST"$asdQWE', False),
    ('lance@saeon.ac.za', '123qwe', False),
    ('lance@saeon.ac.za', 'zxcewer@15', False)
])
def test_valid_password(email, password, expected):
    assert check_password_complexity(email, password) == expected

@pytest.mark.parametrize("email, password, expected", [
    ('lance@saeon.ac.za', 'laWncsdTest123', True),
    ('lance@saeon.ac.za', 'anfDsa&eo!n09', True),
    ('lance@saeon.ac.za', '!@*9nc(ce)sa.eo', True),
    ('lance@saeon.ac.za', 'aczaTestla.a@ce', True),
    ('lance@saeon.ac.za', '@sR3Clamnc!@*09', True),
    ('lance@saeon.ac.za', 'ceMN@cSa.a(', True),
    ('lance@saeon.ac.za', 'Gq".z1a(hYncbe@~bz9a', True),
    ('lance@saeon.ac.za', '5;tvY`_.asa:eo]n.v2#{', True),
    ('lance@saeon.ac.za', 'Cg%e@D#Ty,3?[M:', True),
    ('lance@saeon.ac.za', 'FK=J"%k<#2m+"', True), 

    ('lance@saeon.ac.za', 'lanceasdTEst123', False),
    ('lance@saeon.ac.za', 'saeon!@*09', False),
    ('lance@saeon.ac.za', 'laAncsdTest123', False),
    ('lance@saeon.ac.za', '958$#FDce@sa.Qewt', False),
    ('lance@saeon.ac.za', '!@*09ac.za', False),
    ('lance@saeon.ac.za', '&sK%bJe@sqX}R68`', False),
    ('lance@saeon.ac.za', 'cnE;k"-!n.aS7!h', False),
    ('lance@saeon.ac.za', 'M3}-n*c.z=U-E', False),
    ('lance@saeon.ac.za', '_9<wSD#S`+.zaQnx', False),
    ('lance@saeon.ac.za', 's)=H:*3&SV>U.acy', False),
])
def test_consecutive_letters(email, password, expected):
    assert check_consecutive_letters(email, password) == expected
