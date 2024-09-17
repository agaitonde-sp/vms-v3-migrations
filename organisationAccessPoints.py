import pandas as pd
import numpy as np
import os

from common import isBool, isNameValid, isNum, isValidResourceState, isValidDoorState

organisationAPDf = pd.read_csv("OM/access_points.csv")

def validate(inputDf):
    if not inputDf["accessPointId"].apply(isNum).all():
        print("all accessPointIds are not numbers")
        return False
    elif not inputDf["organisationId"].apply(isNum).all():
        print("all organisationIds are not numbers")
        return False
    elif not inputDf["siteId"].apply(isNum).all():
        print("all sites are not numbers")
        return False
    elif not inputDf["forVisitorAccess"].apply(isBool).all():
        print("all sites are not numbers")
        return False
    return True

def process(inputDf):
    organisationAp = pd.DataFrame()
    organisationAp["accessPointId"] = inputDf["accessPointId"]
    organisationAp["organisationId"] = inputDf["organisationId"]
    organisationAp["siteId"] = inputDf["siteId"]
    organisationAp["createdAt"] = inputDf["createdAt"]
    organisationAp["updatedAt"] = inputDf["updatedAt"]
    organisationAp["vmsEnabled"] = inputDf["forVisitorAccess"]
    organisationAp["autoApprovalEnabled"] =  False
    organisationAp.to_csv("VMSV3/organisation_access_points.csv", index=False)

isOk = validate(organisationAPDf)
if isOk:
    process(organisationAPDf)


