-- Raw layer: landing table for source data, unmodified.

CREATE SCHEMA IF NOT EXISTS raw;

CREATE TABLE IF NOT EXISTS raw.transactions (
    step            INTEGER,
    type            VARCHAR(50),
    amount          NUMERIC(18, 2),
    nameorig        VARCHAR(50),
    oldbalanceorg   NUMERIC(18, 2),
    newbalanceorig  NUMERIC(18, 2),
    namedest        VARCHAR(50),
    oldbalancedest  NUMERIC(18, 2),
    newbalancedest  NUMERIC(18, 2),
    isfraud         INTEGER,
    isflaggedfraud  INTEGER
);
