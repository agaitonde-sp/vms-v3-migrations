import pandas as pd
import numpy as np
import os
import pytz
import datetime

from common import isBool, isNameValid, isNum, isValidResourceState, isValidDoorState

def convert_to_timezone_aware_datetime(epoch, timezone):

    if pd.isna(timezone):
        timezone = 'Asia/Kolkata'
    # Convert epoch to datetime
    dt = datetime.datetime.fromtimestamp(epoch)
    # Convert to timezone-aware datetime
    tz = pytz.timezone(timezone)
    tz_aware_dt = tz.localize(dt)
    # Format the datetime as required, returning a string
    return tz_aware_dt.strftime('%Y-%m-%d %H:%M:%S.%f %z')

def convert_to_date(epoch, timezone):
        # Convert epoch to datetime
    dt = datetime.datetime.fromtimestamp(epoch)
    if pd.isna(timezone):
        timezone = 'Asia/Kolkata'
    # Convert to timezone-aware datetime
    tz = pytz.timezone(timezone)
    tz_aware_dt = tz.localize(dt)
    # Format the datetime as required
    return tz_aware_dt.strftime('%Y-%m-%d')

def convert_to_time(epoch, timezone):
        # Convert epoch to datetime
    dt = datetime.datetime.fromtimestamp(epoch)
    if pd.isna(timezone):
        timezone = 'Asia/Kolkata'
    # Convert to timezone-aware datetime
    tz = pytz.timezone(timezone)
    tz_aware_dt = tz.localize(dt)
    # Format the datetime as required
    return tz_aware_dt.strftime('%H:%M:%S')

def get_tzAbbr(timezone):
    return pytz.timezone(timezone).localize(datetime.datetime.now()).strftime('%Z')


visitorHistoriesDf = pd.read_csv("VMS/visitor_histories.csv")
meetingsDf = pd.read_csv("VMS/meetings.csv")
accessPointDf = pd.read_csv("OM/access_points.csv")
siteDf = pd.read_csv("OM/sites.csv")

apWithSiteDf = pd.merge(accessPointDf, siteDf, on=["siteId", "organisationId"])
meetingJoinDf = pd.merge(visitorHistoriesDf, meetingsDf, left_on="meetingId", right_on="id")

joinedDf = pd.merge(meetingJoinDf, apWithSiteDf, on=["accessPointId", "organisationId"], how="left")

def validate(inputDf):
    return True


def process(inputDf):
    visitorHistores = pd.DataFrame()
    visitorHistores["id"] = inputDf["id_x"]
    visitorHistores["eventTimeEpoch"] = inputDf["accessedAt"]
    visitorHistores["orgId"] = inputDf["organisationId"]
    visitorHistores["accessType"] = inputDf["accessMode"].apply(lambda x: "qr" if x == "qr" else "card")
    visitorHistores["eventType"] = "authorised_access"
    visitorHistores["eventCause"] = ""
    visitorHistores["direction"] = inputDf["direction"].apply(lambda x: x if pd.notna(x) else "\\N")
    visitorHistores["accessPointId"] = inputDf["accessPointId"].astype('Int64').astype('str').replace('<NA>','\\N')
    visitorHistores["meetingId"] = inputDf["meetingId"]
    visitorHistores["visitorId"] = inputDf["visitorId"]
    visitorHistores["siteId"] = inputDf["siteId"].astype('Int64').astype('str').replace('<NA>','\\N')
    visitorHistores["timezonedEventTime"] = inputDf.apply(lambda x: convert_to_timezone_aware_datetime(x["accessedAt"], x["timeZone"]), axis=1)
    visitorHistores["date"] = inputDf.apply(lambda x: convert_to_date(x["accessedAt"], x["timeZone"]), axis=1)
    visitorHistores["time"] = inputDf.apply(lambda x: convert_to_time(x["accessedAt"], x["timeZone"]), axis=1)
    visitorHistores["tzAbbr"] = inputDf["timeZone"].apply(lambda x : 'Asia/Kolkata' if pd.isna(x) else x ).apply(get_tzAbbr)
    visitorHistores["createdAt"] = inputDf["createdAt_x_x"]
    visitorHistores["updatedAt"] = inputDf["updatedAt_x_x"]
    visitorHistores.to_csv("VMSV3/visitor_histories.csv", index=False)


process(joinedDf)
