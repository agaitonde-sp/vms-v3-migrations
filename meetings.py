import pandas as pd
import numpy as np
import os
import pytz
import datetime

from common import isBool, isNameValid, isNum, isValidResourceState, isValidDoorState

def validMeetingStatus(value):
    return True

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
    if pd.isna(timezone):
        timezone = 'Asia/Kolkata'
    return pytz.timezone(timezone).localize(datetime.datetime.now()).strftime('%Z')


meetings = pd.read_csv("VMS/meetings.csv")

orgUsers = pd.read_csv("OM/organisation_users.csv")
sites = pd.read_csv("OM/organisation_sites.csv")
orgUserWithSite =  pd.merge(orgUsers, sites, left_on='homeSiteId', right_on='siteId')
orgUserWithTz = orgUserWithSite[['id_x', 'timeZone', 'siteId']].rename(columns={'id_x': 'orgUserId'})

meetingsDf = pd.read_csv("VMS/meetings.csv")

joinedDf = pd.merge(meetingsDf, orgUserWithTz, left_on='orgUserId', right_on='orgUserId', how='left')

def validate(inputDf):
    if not inputDf["id"].apply(isNum).all():
        print("all ids are not numbers")
        return False
    elif not inputDf["organisationId"].apply(isNum).all():
        print("all organisationIds are not numbers")
        return False
    elif not inputDf["visitorId"].apply(isNum).all():
        print("all visitorIds are not numbers")
        return False
    elif not inputDf["status"].apply(validMeetingStatus).all():
        print("all statuses are not numbers")
        return False

    return True

def process(inputDf):
    meetings = pd.DataFrame()
    meetings["id"] = inputDf["id"]
    meetings["organisationId"] = inputDf["organisationId"]
    meetings["visitorId"] = inputDf["visitorId"]
    meetings["startTimeEpoch"] = inputDf["visitDateTime"].apply(lambda x: int(pd.to_datetime(x).timestamp()) if pd.notnull(x) else 0)
    meetings["endTimeEpoch"] = inputDf["checkOutTime"].apply(lambda x: int(pd.to_datetime(x).timestamp()) if pd.notnull(x) else 0)
    meetings["timeZone"] = inputDf["timeZone"]
    meetings["startDate"] = meetings.apply(lambda x: convert_to_date(x["startTimeEpoch"], x["timeZone"]), axis=1)
    meetings["startTime"] = meetings.apply(lambda x: convert_to_time(x["startTimeEpoch"], x["timeZone"]), axis=1)
    meetings["endDate"] = meetings.apply(lambda x: convert_to_date(x["endTimeEpoch"], x["timeZone"]), axis=1)
    meetings["endTime"] = meetings.apply(lambda x: convert_to_time(x["endTimeEpoch"], x["timeZone"]), axis=1)
    meetings["tzAbbr"] = meetings["timeZone"].apply(lambda x: get_tzAbbr(x))
    meetings["siteId"] = inputDf["siteId"].astype('Int64').astype('str').replace('<NA>','\\N')
    meetings["status"] = inputDf["status"]
    meetings["meetingPurpose"] = inputDf["meetingPurpose"]
    meetings["signature"] = inputDf["signature"]
    meetings["visitorComments"] = inputDf["visitorAdditionalInfo"]
    meetings["hostComments"] = inputDf["additionalInfo"]
    meetings["comments"] = ""
    meetings["fdComments"] = ""
    meetings["covidStatus"] = inputDf["covidStatus"]
    meetings["covidData"] = inputDf["covidData"]
    meetings["hostId"] = inputDf["orgUserId"].astype('Int64').astype('str').replace('<NA>','\\N')
    meetings["kioskId"] = inputDf["kioskId"].astype('Int64').astype('str').replace('<NA>','\\N')
    meetings["approvedBy"] = inputDf.apply(lambda x : x["requestProcessedById"] if x["status"] == "approved" else "\\N", axis=1)
    meetings["checkInTimeEpoch"] = inputDf["checkInTime"].apply(lambda x: int(pd.to_datetime(x).timestamp()) if pd.notnull(x) else 0)
    meetings["checkOutTimeEpoch"] = inputDf["checkOutTime"].apply(lambda x: int(pd.to_datetime(x).timestamp()) if pd.notnull(x) else 0)
    meetings["checkinDate"] = meetings.apply(lambda x: convert_to_date(x["checkInTimeEpoch"], x["timeZone"]), axis=1)
    meetings["checkinTime"] = meetings.apply(lambda x: convert_to_time(x["checkInTimeEpoch"], x["timeZone"]), axis=1)
    meetings["checkoutDate"] = meetings.apply(lambda x: convert_to_date(x["checkOutTimeEpoch"], x["timeZone"]), axis=1)
    meetings["checkoutTime"] = meetings.apply(lambda x: convert_to_time(x["checkOutTimeEpoch"], x["timeZone"]), axis=1)
    meetings["checkedInById"] = inputDf["requestProcessedById"].astype('Int64').astype('str').replace('<NA>','\\N')
    meetings["checkedOutById"] = inputDf["checkedOutById"].astype('Int64').astype('str').replace('<NA>','\\N')
    meetings["checkedInByFd"] = inputDf["requestProcessedByFd"]
    meetings["checkedOutByFd"] = inputDf["checkedOutByFd"]
    meetings["rejectedById"] = inputDf.apply(lambda x : int(x["requestProcessedById"]) if (x["status"] == "rejected" and pd.notna(x["requestProcessedById"])) else "\\N", axis=1)
    meetings["requestProcessedByFd"] = inputDf["requestProcessedByFd"]
    meetings["createdAt"] = inputDf["createdAt"]
    meetings["updatedAt"] = inputDf["updatedAt"]

    meetings.drop(columns=["timeZone"], inplace=True)
    meetings.to_csv("VMSV3/meetings.csv", index=False)
isOk = validate(joinedDf)

if isOk:
    process(joinedDf)
