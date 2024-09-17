import pandas as pd
import numpy as np
import os

from common import isBool, isNameValid, isNum, isValidResourceState, isValidDoorState,isString

organisationDeclarationSettingsDf = pd.read_csv("OM/organisation_level_visitor_settings.csv")
print(organisationDeclarationSettingsDf.columns)

def validate(inputDf):
    if not inputDf["id"].apply(isNum).all():
        print("all Ids are not numbers")
        return False
    elif not inputDf["organisationId"].apply(isNum).all():
        print("all orgIds are not numbers")
        return False
    elif not inputDf["tAndCFormEnabled"].apply(isBool).all():
        print("all tAndCFormEnabled vals are not bool")
        return False
    elif not inputDf["defaultTAndCEnabled"].apply(isBool).all():
        print("all defaultTandCEnabled vals are not bool")
        return False
    # elif not inputDf["uploadedTAndCFile"].apply(isString).all():
    #     print("all values of uploadTAndCFile are not string")
    #     return False
    elif not inputDf["covidEnabled"].apply(isBool).all():
        print("all covidEnable vals are not bool")
        return False
    return True

def process(inputDf):
    organisationDeclarationSettings = pd.DataFrame()
    organisationDeclarationSettings["id"] = inputDf["id"]
    organisationDeclarationSettings["organisationId"] = inputDf["organisationId"]
    organisationDeclarationSettings["tAndCEnabled"] = inputDf["tAndCFormEnabled"]
    organisationDeclarationSettings["defaultOrUploadedTAndCType"] = inputDf["defaultTAndCEnabled"].apply(lambda x: 'default' if x else 'uploaded')
    organisationDeclarationSettings["uploadedTAndCFile"] = inputDf["uploadedTAndCFile"].apply(lambda x : x if isinstance(x, str) else '\\N')
    organisationDeclarationSettings["covidEnabled"] = inputDf["covidEnabled"]
    organisationDeclarationSettings["createdAt"] = inputDf["createdAt"]
    organisationDeclarationSettings["updatedAt"] = inputDf["updatedAt"]

    organisationDeclarationSettings.to_csv("VMSV3/organisation_declaration_settings.csv", index=False)

isOk = validate(organisationDeclarationSettingsDf)

if isOk:
    process(organisationDeclarationSettingsDf)
