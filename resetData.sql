SELECT SETVAL('"cards_id_seq"', (SELECT MAX("id") FROM cards));
SELECT SETVAL('"kiosks_id_seq"', (SELECT MAX("id") FROM kiosks));
SELECT SETVAL('"meeting_access_modes_id_seq"', (SELECT MAX("id") FROM meeting_access_modes));
SELECT SETVAL('"meeting_cards_history_id_seq"', (SELECT MAX("id") FROM meeting_cards_history));
SELECT SETVAL('"meeting_permissions_id_seq"', (SELECT MAX("id") FROM meeting_permissions));
