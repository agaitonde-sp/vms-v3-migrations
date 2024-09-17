import pandas as pd
import numpy as np
import os
import pytz
import datetime

from common import isBool, isNameValid, isNum, isValidResourceState, isValidDoorState, isString

emailTokensDf = pd.read_csv("VMS/email_tokens.csv")

def validate(inputDf):
    if not inputDf["id"].apply(isNum).all():
        return False
    if not inputDf["token"].apply(isString).all():
        return False
    return True


def process(inputDf):
    emailTokens=pd.DataFrame()
    emailTokens["id"] = inputDf["id"]
    emailTokens["meetingId"] = inputDf["meetingId"]
    emailTokens["token"] = inputDf["token"]
    emailTokens["expiredAt"] = inputDf["expiresAt"].apply(lambda x: x if pd.notna(x) else "\\N")
    emailTokens["createdAt"] = inputDf["createdAt"]
    emailTokens["updatedAt"] = inputDf["updatedAt"]

    emailTokens.to_csv("VMSV3/email_tokens.csv", index=False)

isOk = validate(emailTokensDf)
if isOk:
    process(emailTokensDf)
