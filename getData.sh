#!/bin/bash

set -euo pipefail

psql -Atx $ORG_MGMT_URL -c "\copy access_point_devices TO 'OM/access_point_devices.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $ORG_MGMT_URL -c "\copy access_points TO 'OM/access_points.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $ORG_MGMT_URL -c "\copy organisation_sites TO 'OM/sites.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $ORG_MGMT_URL -c "\copy organisation_users TO 'OM/organisation_users.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $ORG_MGMT_URL -c "\copy organisations TO 'OM/organisations.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $ORG_MGMT_URL -c "\copy devices TO 'OM/devices.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $ORG_MGMT_URL -c "\copy organisation_visitor_access_qr_data TO 'OM/organisation_visitor_access_qr_data.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $ORG_MGMT_URL -c "\copy organisation_sites TO 'OM/organisation_sites.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $ORG_MGMT_URL -c "\copy organisation_visitor_access_modes TO 'OM/organisation_visitor_access_modes.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $ORG_MGMT_URL -c "\copy organisation_level_visitor_settings TO 'OM/organisation_level_visitor_settings.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $ORG_MGMT_URL -c "\copy organisation_level_meeting_purposes TO 'OM/organisation_level_meeting_purposes.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $ORG_MGMT_URL -c "\copy organisation_modules TO 'OM/organisation_modules.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $VISITOR_MGMT_URL -c "\copy meeting_access_modes TO 'VMS/meeting_access_modes.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $VISITOR_MGMT_URL -c "\copy meeting_permissions TO 'VMS/meeting_permissions.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $VISITOR_MGMT_URL -c "\copy meetings TO 'VMS/meetings.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $VISITOR_MGMT_URL -c "\copy meetings TO 'VMS/meetings.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $VISITOR_MGMT_URL -c "\copy session_tokens TO 'VMS/session_tokens.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $VISITOR_MGMT_URL -c "\copy visitor_histories TO 'VMS/visitor_histories.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $VISITOR_MGMT_URL -c "\copy visitors TO 'VMS/visitors.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $VISITOR_MGMT_URL -c "\copy qr_codes TO 'VMS/qr_codes.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"

psql -Atx $VISITOR_MGMT_URL -c "\copy visitor_accessor_cards TO 'VMS/visitor_accessor_cards.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $VISITOR_MGMT_URL -c "\copy meeting_cards TO 'VMS/meeting_cards.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"
psql -Atx $VISITOR_MGMT_URL -c "\copy email_tokens TO 'VMS/email_tokens.csv' WITH (FORMAT csv, DELIMITER ',', HEADER)"


python accessPoints.py
python cards.py
python kiosks.py
python meetingAccessMode.py
python meetingCardHistory.py
python meetingPermissions.py
python meetings.py
python organisation_access_mode.py
python organisationAccessPoints.py
python organisationDeclarationSettings.py
python organisationLevelMeetingPurpose.py
python organisationModules.py
python organisations.py
python organisationSites.py
python organisationUsers.py
python organisationVisitorSettings.py
python organisationVisitorSetupEnable.py
python sessionTokens.py
python visitorHistories.py
python visitors.py
python emailTokens.py


psql -Atx $VISITOR_MGMT_V3_URL -a -f truncate.sql
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy access_points from 'VMSV3/access_points.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy cards from 'VMSV3/cards.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy kiosks from 'VMSV3/kiosks.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy meeting_access_modes from 'VMSV3/meeting_access_modes.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy meeting_cards_history from 'VMSV3/meeting_card_history.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy meeting_permissions from 'VMSV3/meeting_permissions.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy meetings from 'VMSV3/meetings.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy organisation_access_modes from 'VMSV3/organisation_access_modes.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy organisation_access_points from 'VMSV3/organisation_access_points.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy organisation_declaration_settings from 'VMSV3/organisation_declaration_settings.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy organisation_meeting_purposes from 'VMSV3/organisation_meeting_purposes.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy organisation_modules from 'VMSV3/organisation_modules.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy organisations from 'VMSV3/organisations.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy organisation_sites from 'VMSV3/organisation_sites.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy organisation_users from 'VMSV3/organisation_users.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy organisation_visitor_settings from 'VMSV3/organisation_visitor_settings.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy organisation_visitor_setup_enable from 'VMSV3/organisation_visitor_setup_enable.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy session_tokens from 'VMSV3/session_tokens.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy visitor_histories from 'VMSV3/visitor_histories.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy visitors from 'VMSV3/visitors.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"
psql -Atx $VISITOR_MGMT_V3_URL -c "\copy email_tokens from 'VMSV3/email_tokens.csv' WITH (FORMAT csv, DELIMITER ',', NULL '\N', HEADER)"


psql -Atx $VISITOR_MGMT_V3_URL -a -f resetData.sql
