import pytest
from utilits import valid_email, log

@pytest.mark.parametrize('email', ['test@test.ru', 'w@w.com', "123QWE@mmm.mmm", ])
def test_correct_check_email(email, log_file):
    check_email = valid_email(email)
    if check_email:
        log(log_file, email + 'valid\n')
    else:
        log(log_file, email + 'not valid\n')
    

@pytest.mark.parametrize('email', ['test@test.', 'w@', "@tt"])
def test_incorrect_check_email(email, log_file):
    check_email = valid_email(email)
    if check_email:
        log(log_file, email + 'valid\n')
    else:
        log(log_file, email + 'not valid\n')
