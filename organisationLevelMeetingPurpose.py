# source OM/access_points 
import pandas as pd
import numpy as np
import os

from common import isBool, isNameValid, isNum, isString, isValidResourceState, isValidDoorState

organisationLevelMeetingPurposeDf = pd.read_csv("OM/organisation_level_meeting_purposes.csv")

def validate(inputDf):
    if not inputDf["id"].apply(isNum).all():
        print("all Ids are not numbers")
        return False
    elif not inputDf["organisationId"].apply(isNum).all():
        print("all orgIds are not numbers")
        return False
    elif not inputDf["meetingPurpose"].apply(isString).all():
        print("all meetingPurpose are not proper")
        return False
    elif not inputDf["checked"].apply(isBool).all():
        print("all checked are not proper")
        return False
    return True

def process(inputDf):
    organisationLevelMeetingPurpose = pd.DataFrame()
    organisationLevelMeetingPurpose["id"] = inputDf["id"]
    organisationLevelMeetingPurpose["organisationId"] = inputDf["organisationId"]
    organisationLevelMeetingPurpose["meetingPurpose"] = inputDf["meetingPurpose"]
    organisationLevelMeetingPurpose["checked"] = inputDf["checked"]
    organisationLevelMeetingPurpose["createdAt"] = inputDf["createdAt"]
    organisationLevelMeetingPurpose["updatedAt"] = inputDf["updatedAt"]

    organisationLevelMeetingPurpose.to_csv("VMSV3/organisation_meeting_purposes.csv", index=False)

isOk = validate(organisationLevelMeetingPurposeDf)
if isOk:
    process(organisationLevelMeetingPurposeDf)



