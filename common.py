from numbers import Number
from datetime import datetime
import psycopg2


def isNameValid(name):
    if not isinstance(name, str):
        print("name " + str(name) + " is not valid")
        return False
    if len(name) > 255:
        print("name " + name + " is not valid")
        return False
    else:
        return True


def isNum(val):
    if not isinstance(val, Number):
        print("val", val, " is not a number")
        return False
    else:
        return True


def isString(val):
    if not isinstance(val, str):
        print("val", val, " is not a string")
        return False
    else:
        return True

def check_date_format(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f %z")
        return True
    except ValueError:
        return False


def isBool(value):
    if value not in ['t', 'f']:
        print("isBool", value, " not valid value")
        return False
    else:
        return True



def isValidResourceState(value):
    if value not in ["alive", "pending"]:
        print("isValidResourceState", value, "not valid value")
        return False
    else:
        return True



def isValidDoorState(value):
    if value not in ["unlocked", "locked", "access_control"]:
        print("isValidDoorState", value, "not valid door state")
        return False
    else:
        return True


def isValidStatus(value):
    if not value in ['online', 'offline']:
        print("isValidStatus", value," is not correct type")
        return False
    else:
        return True

def isValidCardType(value):
    if not value in ['0' ,'spintly', 'mifare_csn', 'H10301']:
        print("isValidCardType", value, " is not a correct card type")
        return False
    else:
        return True
