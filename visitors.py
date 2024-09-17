import pandas as pd
import numpy as np
import os
import pytz
import datetime

from common import isBool, isNameValid, isNum, isValidResourceState, isValidDoorState, isString

visitorsDf = pd.read_csv("VMS/visitors.csv")

def validate(inputDf):
    if not inputDf["id"].apply(isNum).all():
        return False
    # if not inputDf["phone"].apply(isString).all():
    #     return False

    return True

def process(inputDf):
    visitors=pd.DataFrame()
    visitors["id"] = inputDf["id"]
    visitors["organisationId"] = inputDf["organisationId"]
    visitors["name"] = inputDf["name"].apply(lambda x: x if x is not np.nan else "")
    visitors["email"] = inputDf["email"].apply(lambda x: x if x is not np.nan else "")
    visitors["phone"] = inputDf["phone"].apply(lambda x: x if x is not np.nan else "")
    visitors["picUrl"] = inputDf["picUrl"].apply(lambda x: x if x is not np.nan else "")
    visitors["createdAt"] = inputDf["createdAt"]
    visitors["updatedAt"] = inputDf["updatedAt"]

    visitors.to_csv("VMSV3/visitors.csv", index=False)

isOk = validate(visitorsDf)
if isOk:
    process(visitorsDf)
