import pandas as pd
import numpy as np
import os
import pytz
import datetime

from common import isBool, isNameValid, isNum, isValidResourceState, isValidDoorState, isString


visitorCardsDf = pd.read_csv("VMS/visitor_accessor_cards.csv")
meetingCardsDf = pd.read_csv("VMS/meeting_cards.csv")
meetingsDf = pd.read_csv("VMS/meetings.csv")

meetingsWithCardsDf = pd.merge(meetingsDf, meetingCardsDf, left_on="id", right_on="meetingId", how="right")

joinedDf = pd.merge(visitorCardsDf, meetingsWithCardsDf, on=["accessorId"], how="inner")

cardsDf = joinedDf[joinedDf["assigned"]=='t']


def validate(inputDf):
    return True

def process(inputDf):
    cards=pd.DataFrame()
    cards["id"] = inputDf["id"].astype('Int64')
    cards["credentialId"] = inputDf["credentialId"]
    cards["organisationId"] = inputDf["organisationId_x"]
    cards["meetingId"] = inputDf["meetingId"].astype('Int64').astype('str').replace('<NA>','\\N')
    cards["visitorId"] = inputDf["visitorId"].astype('Int64').astype('str').replace('<NA>','\\N')
    cards["status"] = 'in_sync'
    cards["createdAt"] = inputDf["createdAt"]
    cards["updatedAt"] = inputDf["updatedAt"]

    cards.drop_duplicates(subset=["id"]).to_csv("VMSV3/cards.csv", index=False)


isOk = validate(cardsDf)
if isOk:
    process(cardsDf)
