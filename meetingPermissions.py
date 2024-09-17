import pandas as pd
import numpy as np
import os

from common import isBool, isNameValid, isNum, isValidResourceState, isValidDoorState
meetingPermissionsDf = pd.read_csv("VMS/meeting_permissions.csv")

meetingAccessModeDf = pd.read_csv("VMS/meeting_access_modes.csv")


joinedDf = pd.merge(meetingPermissionsDf, meetingAccessModeDf, on="meetingId", how="left" )

def validate(inputDf):
    if not inputDf["id_x"].apply(isNum).all():
        print("all ids are not numbers")
        return False
    elif not inputDf["meetingId"].apply(isNum).all():
        print("all ids are not numbers")
        return False
    elif not inputDf["accessPointId"].apply(isNum).all():
        print("all ids are not numbers")
        return False
    return True


def process(inputDf):
    meetingPermissions = pd.DataFrame()
    meetingPermissions["id"] = inputDf["id_x"]
    meetingPermissions["meetingId"] = inputDf["meetingId"]
    meetingPermissions["accessPointId"] = inputDf["accessPointId"]
    meetingPermissions["status"] = 'in_sync'
    meetingPermissions["requestId"] = ""
    meetingPermissions["accessMode"] = inputDf.apply(lambda x : 'qrScanner' if x["qr"] else 'card', axis=1)
    meetingPermissions["createdAt"] = inputDf["createdAt_x"]
    meetingPermissions["updatedAt"] = inputDf["updatedAt_x"]

    meetingPermissions.to_csv("VMSV3/meeting_permissions.csv", index=False)


isOk = validate(joinedDf)
if isOk:
    process(joinedDf)
