import pandas as pd
import numpy as np
import os

from common import isNameValid, isNum, isValidResourceState, isValidDoorState

organisationSitesDf = pd.read_csv("OM/organisation_sites.csv")

def transformResourceState(resourceState):
    if resourceState == "alive":
        return "alive"
    elif resourceState == "configure_pending":
        return "pending"
    else:
        return "pending"

def validate(inputDf):
    if not inputDf["id"].apply(isNum).all():
        print("all Ids are not numbers")
        return False
    elif not inputDf["organisationId"].apply(isNum).all():
        print("all orgIds are not numbers")
        return False
    elif not inputDf["name"].apply(isNameValid).all():
        print("all siteNames are not proper")
        return False
    elif not inputDf["timeZone"].apply(isNameValid).all():
        print("all siteAddresses are not proper")
        return False
    elif not inputDf["resourceState"].apply(transformResourceState).apply(isValidResourceState).all():
        print("all siteTypes are not proper")
        return False
    return True

def process(inputDf):
    organisationSites = pd.DataFrame()
    organisationSites["siteId"] = inputDf["id"]
    organisationSites["organisationId"] = inputDf["organisationId"]
    organisationSites["name"] = inputDf["name"]
    organisationSites["timeZone"] = inputDf["timeZone"]
    organisationSites["resourceState"] = inputDf["resourceState"].apply(transformResourceState)
    organisationSites["createdAt"] = inputDf["createdAt"]
    organisationSites["updatedAt"] = inputDf["updatedAt"]

    organisationSites.to_csv("VMSV3/organisation_sites.csv", index=False)

isOk = validate(organisationSitesDf)
if isOk:
    process(organisationSitesDf)
