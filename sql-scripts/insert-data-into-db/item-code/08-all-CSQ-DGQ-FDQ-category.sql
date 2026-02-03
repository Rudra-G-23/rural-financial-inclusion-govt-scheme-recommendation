CREATE TABLE utils.category_mapping_csq (
    item_code INTEGER,
    category TEXT,

    ingest_timestamp TIMESTAMPTZ
        DEFAULT (now() AT TIME ZONE 'Asia/Kolkata'),

    ingest_date DATE
        DEFAULT (CURRENT_DATE AT TIME ZONE 'Asia/Kolkata')
);

CREATE TABLE utils.category_mapping_dgq (
    item_code INTEGER,
    category TEXT,

    ingest_timestamp TIMESTAMPTZ
        DEFAULT (now() AT TIME ZONE 'Asia/Kolkata'),

    ingest_date DATE
        DEFAULT (CURRENT_DATE AT TIME ZONE 'Asia/Kolkata')
);

CREATE TABLE utils.category_mapping_fdq (
    item_code INTEGER,
    category TEXT,

    ingest_timestamp TIMESTAMPTZ
        DEFAULT (now() AT TIME ZONE 'Asia/Kolkata'),

    ingest_date DATE
        DEFAULT (CURRENT_DATE AT TIME ZONE 'Asia/Kolkata')
);