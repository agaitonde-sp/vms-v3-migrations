import pandas as pd
import numpy as np
import os

from common import isBool, isNameValid, isNum, isValidResourceState, isValidDoorState

meetingAccessModeDf = pd.read_csv("VMS/meeting_access_modes.csv")

def validate(inputDf):
    if not inputDf["meetingId"].apply(isNum).all():
        print("all meetingIds are not numbers")
        return False
    elif not inputDf["qr"].apply(isBool).all():
        print("all qr scanner vals are not bool")
        return False
    elif not inputDf["card"].apply(isBool).all():
        print("all card vals are not bool")
        return False
    # elif inputDf[['qr', 'card']].all(axis=1).any():
    #     inputDf[['qr', 'card']].to_csv("vms_invalid_meetings")
    #     print("meetingId has dual purpose")
        # return False
    return True

def process(inputDf):
    meetingAccessModes = pd.DataFrame()
    meetingAccessModes["id"] = inputDf["id"]
    meetingAccessModes["meetingId"] = inputDf["meetingId"]
    meetingAccessModes["qrReader"] = False
    meetingAccessModes["card"] = inputDf["card"]
    meetingAccessModes["qrScanner"] = inputDf["qr"]
    meetingAccessModes["createdAt"] = inputDf["createdAt"]
    meetingAccessModes["updatedAt"] = inputDf["updatedAt"]

    meetingAccessModes.to_csv("VMSV3/meeting_access_modes.csv", index=False)


isOk = validate(meetingAccessModeDf)
if isOk:
    process(meetingAccessModeDf)
