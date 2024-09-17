import pandas as pd
import numpy as np
import os

from common import isBool, isNameValid, isNum, isValidResourceState, isValidDoorState

organisationVisitorSettingsDf = pd.read_csv("OM/organisation_level_visitor_settings.csv")


def validate(inputDf):
    if not inputDf["id"].apply(isNum).all():
        print("all ids are not null")
        return False
    elif not inputDf["organisationId"].apply(isNum).all():
        print("all organisationIds are not numbers")
        return False
    elif not inputDf["visitorNameEnabled"].apply(isBool).all():
        print("all visitorNameEnabled are not bool")
        return False
    elif not inputDf["personToMeetEnabled"].apply(isBool).all():
        print("all visitorMobileEnabled are not bool")
        return False
    elif not inputDf["visitorPhotoEnabled"].apply(isBool).all():
        print("all visitorMobileEnabled are not bool")
        return False
    elif not inputDf["additionalInfoEnabled"].apply(isBool).all():
        print("all visitorMobileEnabled are not bool")
        return False
    elif not inputDf["printVisitorDetailsEnabled"].apply(isBool).all():
        print("all visitorMobileEnabled are not bool")
        return False
    elif not inputDf["visitorPhoneEnabled"].apply(isBool).all():
        print("all visitorMobileEnabled are not bool")
        return False
    elif not inputDf["visitorEmailEnabled"].apply(isBool).all():
        print("all visitorMobileEnabled are not bool")
        return False
    elif not inputDf["autoApproveVisit"].apply(isBool).all():
        print("all visitorMobileEnabled are not bool")
        return False
    elif not inputDf["visitorAdditionalInfo"].apply(isBool).all():
        print("all visitorMobileEnabled are not bool")
        return False
    return True

def process(inputDf):
    organisationVisitorSettings = pd.DataFrame() 
    organisationVisitorSettings["id"] = inputDf["id"]
    organisationVisitorSettings["organisationId"] = inputDf["organisationId"]
    organisationVisitorSettings["visitorNameEnabled"] = inputDf["visitorNameEnabled"]
    organisationVisitorSettings["personToMeetEnabled"] = inputDf["personToMeetEnabled"]
    organisationVisitorSettings["visitStartTimeEnabled"] = True
    organisationVisitorSettings["visitEndTimeEnabled"] = True
    organisationVisitorSettings["visitorPhotoEnabled"] = inputDf["visitorPhotoEnabled"]
    organisationVisitorSettings["commentsEnabled"] = inputDf["additionalInfoEnabled"]
    organisationVisitorSettings["printVisitorDetailsEnabled"] = inputDf["printVisitorDetailsEnabled"]
    organisationVisitorSettings["otpVerificationEnabled"] = False
    organisationVisitorSettings["phoneEnabled"] = inputDf["visitorPhoneEnabled"]
    organisationVisitorSettings["emailEnabled"] = inputDf["visitorEmailEnabled"]
    organisationVisitorSettings["unscheduledVisitsEnabled"]=True
    organisationVisitorSettings["autoApprovalEnabled"] = inputDf["autoApproveVisit"]
    organisationVisitorSettings["allowAllAdminEnabled"] = inputDf["allowAllUsers"]
    organisationVisitorSettings["visitorComments"] = inputDf["visitorAdditionalInfo"]
    organisationVisitorSettings["createdAt"] = inputDf["createdAt"]
    organisationVisitorSettings["updatedAt"] = inputDf["updatedAt"]

    organisationVisitorSettings.to_csv("VMSV3/organisation_visitor_settings.csv", index=False)

isOk = validate(organisationVisitorSettingsDf)

if isOk:
    process(organisationVisitorSettingsDf)
