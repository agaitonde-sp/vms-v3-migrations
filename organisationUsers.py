import pandas as pd
import numpy as np
import os

from common import isNameValid, isNum, isValidResourceState, isValidDoorState

organisationUsersDf = pd.read_csv("OM/organisation_users.csv")
organisationModulesDf = pd.read_csv("OM/organisation_modules.csv")

joinedDf = pd.merge(organisationUsersDf, organisationModulesDf, on="organisationId", how="inner")

joinDf = joinedDf[joinedDf["visitor"] == True]

def validate(inputDf):
    if not inputDf["id_x"].apply(isNum).all():
        print("all Ids are not numbers")
        return False
    elif not inputDf["organisationId"].apply(isNum).all():
        print("all orgIds are not numbers")
        return False
    elif not inputDf["userId"].apply(isNum).all():
        print("all userIds are not numbers")
        return False
    elif not inputDf["name"].apply(isNameValid).all():
        print("all names are not valid")
        return False
    return True


def process(inputDf):
    organisationUsers = pd.DataFrame()
    organisationUsers["id"] = inputDf["id_x"]
    organisationUsers["organisationId"] = inputDf["organisationId"]
    organisationUsers["userId"] = inputDf["userId"].astype('Int64').astype('str').replace('<NA>','\\N')
    organisationUsers["name"] = inputDf["name"]
    organisationUsers["createdAt"] = inputDf["createdAt_x"]
    organisationUsers["updatedAt"] = inputDf["updatedAt_x"]

    organisationUsers.to_csv("VMSV3/organisation_users.csv", index=False)

isOk = validate(joinedDf)
if isOk:
    process(joinedDf)
