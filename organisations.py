import pandas as pd
import numpy as np
import os

from common import isBool, isNameValid, isNum, isString, isValidResourceState, isValidDoorState

def isValidOrgType(orgType):
    return orgType in ["office", "residential", "hospitality", "home"]

organisationsDf = pd.read_csv("OM/organisations.csv")

def validate(inputDf):
    if not inputDf["id"].apply(isNum).all():
        print("all ids are not valid")
        return False
    if not inputDf["name"].apply(isNameValid).all():
        print("all names are not valid")
        return False
    if not inputDf["resourceState"].apply(isValidResourceState).all():
        print("all resourceStates are not valid")
        return False
    if not inputDf["integratorId"].apply(isNum).all():
        print("all ids are not valid")
        return False
    # if not inputDf["defaulter"].apply(isBool).all():
    #     print("all defaulters are not valid")
    #     return False
    if not inputDf["type"].apply(isValidOrgType).all():
        print(inputDf["type"].apply(isValidOrgType))
        print("all organisation types are not valid")
        return False
    # if not inputDf["picUrl"].apply(isString).all():
    #     print("all picUrls are not valid")
    #     return False
    return True


def process(inputDf):
    organisations = pd.DataFrame()
    organisations["id"] = inputDf["id"]
    organisations["name"] = inputDf["name"]
    organisations["resourceState"] = inputDf["resourceState"]
    organisations["integratorId"] = inputDf["integratorId"]
    organisations["defaulter"] = inputDf["defaulter"].apply(lambda x: x if isinstance(x, bool)  else False)
    organisations["createdAt"] = inputDf["createdAt"]
    organisations["updatedAt"] = inputDf["updatedAt"]
    organisations["type"] = inputDf["type"].apply(lambda x: x if x =='residential' else 'office')
    organisations["orgLogo"] = inputDf["picUrl"].apply(lambda x: x if isinstance(x, str) else "\\N")
    organisations.to_csv("VMSV3/organisations.csv", index=False)

isOk = validate(organisationsDf)
if isOk:
    process(organisationsDf)






