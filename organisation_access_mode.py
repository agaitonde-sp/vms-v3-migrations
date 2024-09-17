import pandas as pd
import numpy as np
import os

from common import isBool, isNameValid, isNum, isValidResourceState, isValidDoorState

organisationAccessModeDf = pd.read_csv("OM/organisation_visitor_access_modes.csv")

def validate(inputDf):
    if not inputDf["id"].apply(isNum).all():
        print("all ids are not numbers")
        return False
    elif not inputDf["organisationId"].apply(isNum).all():
        print("all organisationIds are not numbers")
        return False
    elif not inputDf["qr"].apply(isBool).all():
        print("all qr scanner vals are not bool")
        return False
    elif not inputDf["card"].apply(isBool).all():
        print("all card vals are not bool")
        return False
    return True

def process(inputDf):
    organisationAccessModes = pd.DataFrame()
    organisationAccessModes["id"] = inputDf["id"]
    organisationAccessModes["organisationId"] = inputDf["organisationId"]
    organisationAccessModes["qrReader"] = False
    organisationAccessModes["card"] = inputDf["card"]
    organisationAccessModes["qrScanner"] = inputDf["qr"]
    organisationAccessModes["autoApprovalAccessMode"] = 'qrScanner'
    organisationAccessModes["createdAt"] = inputDf["createdAt"]
    organisationAccessModes["updatedAt"] = inputDf["updatedAt"]

    organisationAccessModes.to_csv("VMSV3/organisation_access_modes.csv", index=False)


isOk = validate(organisationAccessModeDf)
if isOk:
    process(organisationAccessModeDf)
