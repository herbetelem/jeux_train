import re

def checkIsInt(value):
    if re.match("^[A-Za-z]*$", value):
        return False
    else:
        return True