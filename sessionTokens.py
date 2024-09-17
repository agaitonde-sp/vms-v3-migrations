import pandas as pd
import numpy as np
import os

from common import isBool, isNameValid, isNum, isValidResourceState, isValidDoorState, isString

sessionTokensDf = pd.read_csv("VMS/session_tokens.csv")

def validate(inputDf):
    if not inputDf["id"].apply(isNum).all():
        print("all ids are not null")
        return False
    elif not inputDf["visitorId"].apply(isNum).all():
        print("all visitorId are not numbers")
        return False
    elif not inputDf["organisationId"].apply(isNum).all():
        print("all tokens are not valid")
        return False
    elif not inputDf["token"].apply(isString).all():
        print("all tokens are not valid")
        return False
    return True

def process(inputDf):
    sessionTokens = pd.DataFrame()
    sessionTokens["id"] = inputDf["id"]
    sessionTokens["visitorId"] = inputDf["visitorId"]
    sessionTokens["organisationId"] = inputDf["organisationId"]
    sessionTokens["token"] = inputDf["token"]
    sessionTokens["createdAt"] = inputDf["createdAt"]
    sessionTokens["updatedAt"] = inputDf["updatedAt"]

    sessionTokens.to_csv("VMSV3/session_tokens.csv", index=False)

isOk = validate(sessionTokensDf)
if isOk:
    process(sessionTokensDf)
