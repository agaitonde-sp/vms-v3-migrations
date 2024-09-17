import pandas as pd
import numpy as np
import os
import pytz
import datetime

from common import isBool, isNameValid, isNum, isValidResourceState, isValidDoorState, isString

kiosksDf = pd.read_csv("VMS/qr_codes.csv")

orgSitesDf = pd.read_csv("OM/organisation_sites.csv")

joinedDf = pd.merge(kiosksDf, orgSitesDf, on="organisationId").drop_duplicates(subset=["id_x"])


def validate(inputDf):
    if not inputDf["id_x"].apply(isNum).all():
        return False
    if not inputDf["siteId_y"].apply(isNum).all():
        return False
    if not inputDf["organisationId"].apply(isNum).all():
        return False
    if not inputDf["authCode"].apply(isString).all():
        return False
    if not inputDf["qrCode"].apply(isString).all():
        return False

    return True

def process(inputDf):
    kiosks=pd.DataFrame()
    kiosks["id"] = inputDf["id_x"]
    kiosks["organisationId"] = inputDf["organisationId"]
    kiosks["authCode"] = inputDf["authCode"]
    kiosks["kioskName"] = inputDf["kioskName"]
    kiosks["siteId"] = inputDf["siteId_y"]
    kiosks["qrCode"] = inputDf["qrCode"]
    kiosks["createdAt"] = inputDf["createdAt_x"]
    kiosks["updatedAt"] = inputDf["updatedAt_x"]

    kiosks.to_csv("VMSV3/kiosks.csv", index=False)

isOk = validate(joinedDf)
if isOk:
    process(joinedDf)
