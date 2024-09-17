import pandas as pd
import numpy as np
import os

from common import isBool, isNameValid, isNum, isValidResourceState, isValidDoorState

organisationVisitorSettingsDf = pd.read_csv("OM/organisation_level_visitor_settings.csv")


def validate(inputDf):
    if not inputDf["id"].apply(isNum).all():
        print("all ids are not null")
        return False
    elif not inputDf["organisationId"].apply(isNum).all():
        print("all organisationIds are not numbers")
        return False
    elif not inputDf["accessAssignmentEnabled"].apply(isBool).all():
        print("all accessAssignmentEnabled are not bool")
        return False
    return True


def process(inputDf):
    organisationVisitorSetupEnabled = pd.DataFrame()
    organisationVisitorSetupEnabled["id"] = inputDf["id"]
    organisationVisitorSetupEnabled["organisationId"] = inputDf["organisationId"]
    organisationVisitorSetupEnabled["settingsEnabled"] = True
    organisationVisitorSetupEnabled["accessSetup"] = inputDf["accessAssignmentEnabled"]
    organisationVisitorSetupEnabled["autoSettings"] = False
    organisationVisitorSetupEnabled["createdAt"] = inputDf["createdAt"]
    organisationVisitorSetupEnabled["updatedAt"] = inputDf["updatedAt"]

    organisationVisitorSetupEnabled.to_csv("VMSV3/organisation_visitor_setup_enable.csv", index=False)


isOk = validate(organisationVisitorSettingsDf)
if isOk:
    process(organisationVisitorSettingsDf)
