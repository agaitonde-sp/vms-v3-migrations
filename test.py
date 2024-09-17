
import pandas as pd
import pytz
import datetime

# Function to convert epoch to timezone-aware datetime string
def convert_to_timezone_aware_datetime(epoch, timezone):
    # Convert epoch to datetime
    dt = datetime.datetime.fromtimestamp(epoch)
    # Convert to timezone-aware datetime
    tz = pytz.timezone(timezone)
    tz_aware_dt = tz.localize(dt)
    # Format the datetime as required, returning a string
    return tz_aware_dt.strftime('%Y-%m-%d %H:%M:%S.%f %z')

def process(inputDf):
    visitorHistores = pd.DataFrame()
    visitorHistores["id_x"] = inputDf["id"]
    visitorHistores["eventTimeEpoch"] = inputDf["accessedAt"]
    visitorHistores["orgId"] = inputDf["organisationId"]
    visitorHistores["accessType"] = inputDf["accessMode"].apply(lambda x: "qr_scanner" if x == "qr" else "card")
    visitorHistores["eventType"] = "authorized_access"
    visitorHistores["eventCause"] = ""
    visitorHistores["direction"] = inputDf["direction"]
    visitorHistores["accessPointId"] = inputDf["accessPointId"]
    visitorHistores["meetingId"] = inputDf["meetingId"]
    visitorHistores["siteId"] = inputDf["siteId"]
    
    # This line should not produce a ValueError as it's returning a string
    visitorHistores["timezonedEventTime"] = inputDf.apply(
        lambda x: convert_to_timezone_aware_datetime(x["accessedAt"], x["timeZone"]), axis=1
    )
    
    visitorHistores["date"] = inputDf.apply(
        lambda x: convert_to_timezone_aware_datetime(x["accessedAt"], x["timeZone"]).split(' ')[0], axis=1
    )
    visitorHistores["time"] = inputDf.apply(
        lambda x: convert_to_timezone_aware_datetime(x["accessedAt"], x["timeZone"]).split(' ')[1], axis=1
    )
    visitorHistores["tzAbbr"] = inputDf["timeZone"].apply(get_tzAbbr)
    
    visitorHistores["createdAt"] = inputDf["createdAt_x_x"]
    visitorHistores["updatedAt"] = inputDf["updatedAt_x_x"]
    
    visitorHistores.to_csv("VMSV3/visitor_histories.csv", index=False)

# Ensure get_tzAbbr is defined:
def get_tzAbbr(timezone):
    tz = pytz.timezone(timezone)
    now = datetime.datetime.now(tz)
    return now.strftime('%Z')

# Test with dummy data
data = {
    'id': [1, 2],
    'accessedAt': [1691853984, 1691857584],
    'organisationId': [101, 102],
    'accessMode': ['qr', 'card'],
    'direction': ['in', 'out'],
    'accessPointId': [1001, 1002],
    'meetingId': [2001, 2002],
    'siteId': [3001, 3002],
    'timeZone': ['Asia/Kolkata', 'America/New_York'],
    'createdAt_x_x': ['2024-08-12 21:46:24', '2024-08-12 22:46:24'],
    'updatedAt_x_x': ['2024-08-12 22:46:24', '2024-08-12 23:46:24']
}

inputDf = pd.DataFrame(data)
process(inputDf)
