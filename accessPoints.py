# source OM/access_points 
import pandas as pd
import numpy as np
import os

from common import isNameValid, isNum, isValidResourceState, isValidDoorState

def transformResourceState(resourceState):
    if resourceState == "alive":
        return "alive"
    elif resourceState == "configure_pending":
        return "pending"
    else:
        return "pending"

processData  = True

apDevicesDf = pd.read_csv("OM/access_point_devices.csv")
devicesDf = pd.read_csv("OM/devices.csv")

apDevicesDfJoined = pd.merge(apDevicesDf, devicesDf, on="serialNo" )

agg_df = apDevicesDfJoined.groupby('accessPointId_x')['supportedCredentials'].agg(
    unique_values=pd.Series.nunique,
    credentials=lambda x: x.iloc[0]  # Get the first credential (assuming consistency)
).reset_index()
#
# Dropping inconsistencies
apSupportedCred = agg_df[agg_df['unique_values'] == 1]
#
# Removing the auxiliary column
apSupportedCred = apSupportedCred[['accessPointId_x', 'credentials']].rename(columns={'credentials': 'supportedCredentials', 'accessPointId_x': 'accessPointId'})


accessPointsOMDf = pd.read_csv("./OM/access_points.csv").drop_duplicates(subset=['accessPointId'])
accessPointDrDataDf = pd.read_csv("./OM/organisation_visitor_access_qr_data.csv")
#
joinedDf = pd.merge(accessPointsOMDf, accessPointDrDataDf, on=["accessPointId", "organisationId"], how="left", suffixes=('_x', '_y'))

joinedDf = pd.merge(joinedDf, apSupportedCred, on="accessPointId", how="left")
#
#
#
def validate(inputDf):
    if not inputDf["accessPointId"].apply(isNum).any():
        print("all accessPointIds are not numbers")
        return False
    elif not inputDf["name"].apply(isNameValid).all():
        print(inputDf["name"].apply(isNameValid).values)
        print("all names are not proper")
        return False
    elif not inputDf["supportedCredentials"].isnull().any():
        print("all supportedCredentials are not proper")
        return False
    elif not inputDf["resourceState"].apply(transformResourceState).apply(isValidResourceState).all():
        print("all resourceStates are not valid")
        return False
    return  True

def process(inputDf):
        accessPoints = pd.DataFrame()
        accessPoints["id"] = range(1, len(inputDf) + 1)
        accessPoints["accessPointId"] = inputDf["accessPointId"]
        accessPoints["name"] = inputDf["name"]
        accessPoints["resourceState"] = inputDf["resourceState"].apply(transformResourceState)
        accessPoints["createdAt"] = inputDf["createdAt_x"]
        accessPoints["updatedAt"] = inputDf["updatedAt_x"]
        accessPoints["sharingType"] = inputDf["sharingType"]
        accessPoints["supportedCredentials"] = inputDf["supportedCredentials"].astype('Int64').astype('str').replace('<NA>','\\N')
        
        accessPoints["qrCodeData"] = inputDf["qrCode"].apply(lambda x : x if isinstance(x, str) else '\\N')
#
        accessPoints.drop_duplicates(subset=['accessPointId']).to_csv("VMSV3/access_points.csv", index=False)
#     
isOk = validate(joinedDf)
#
if not isOk:
    exit(1)

if isOk:
    process(joinedDf)
# #
# #
