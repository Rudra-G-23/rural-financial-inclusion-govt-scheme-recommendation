CREATE SCHEMA IF NOT EXISTS utils;

CREATE TABLE utils.category_mapping (
    item_code INTEGER,
    category TEXT,

    ingest_timestamp TIMESTAMPTZ
        DEFAULT (now() AT TIME ZONE 'Asia/Kolkata'),

    ingest_date DATE
        DEFAULT (CURRENT_DATE AT TIME ZONE 'Asia/Kolkata')
);