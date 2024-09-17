# source OM/access_points 
import pandas as pd
import numpy as np
import os

from common import isBool, isNameValid, isNum, isString, isValidResourceState, isValidDoorState

organisationModulesDf = pd.read_csv("OM/organisation_modules.csv")

def validate(inputDf):
    if not inputDf["id"].apply(isNum).all():
        print("all Ids are not numbers")
        return False
    elif not inputDf["organisationId"].apply(isNum).all():
        print("all orgIds are not numbers")
        return False
    elif not inputDf["visitor"].apply(isBool).all():
        print("all module are not proper")
        return False
    return True

def process(inputDf):
    organisationModules = pd.DataFrame()
    organisationModules["id"] = inputDf["id"]
    organisationModules["organisationId"] = inputDf["organisationId"]
    organisationModules["visitor"] = inputDf["visitor"]
    organisationModules["createdAt"] = inputDf["createdAt"]
    organisationModules["updatedAt"] = inputDf["updatedAt"]

    organisationModules.to_csv("VMSV3/organisation_modules.csv", index=False)

isOk = validate(organisationModulesDf)
if isOk:
    process(organisationModulesDf)
