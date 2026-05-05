import re
def is_strong_passowrd(pwd: str)-> bool:
    if " " in pwd:
        return False
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%]).{8,}$'

    return bool(re.match(pattern,pwd))