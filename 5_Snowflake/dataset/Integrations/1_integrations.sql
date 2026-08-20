-- ============================================================
-- Snowflake Storage Integration and External Stage
-- This script demonstrates how to create a Snowflake Storage
-- Integration and an External Stage to securely access data
-- stored in an S3 bucket. It also shows how to load data from
-- the S3 bucket into a Snowflake table.
-- ============================================================


-- ============================================================
-- 1. CREATE STORAGE INTEGRATION
-- ============================================================
-- A Storage Integration is a Snowflake object that securely
-- manages access between Snowflake and external cloud storage.
--
-- Instead of storing AWS access keys/secrets in Snowflake,
-- Snowflake uses an AWS IAM Role to access the S3 bucket.

CREATE OR REPLACE STORAGE INTEGRATION int_s3_sales_db
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = S3
  ENABLED = TRUE

  -- AWS IAM Role that Snowflake is allowed to assume
  STORAGE_AWS_ROLE_ARN =
    'arn:aws:iam::521926169599:role/snowflake-si-role'

  -- Restricts Snowflake access to this specific S3 location
  STORAGE_ALLOWED_LOCATIONS =
    ('s3://sales-punith-demo/');


-- ============================================================
-- 2. DESCRIBE THE STORAGE INTEGRATION
-- ============================================================
-- DESC INTEGRATION displays the integration properties.
--
-- Most importantly, Snowflake provides values such as:
--   STORAGE_AWS_IAM_USER_ARN
--   STORAGE_AWS_EXTERNAL_ID
--
-- These values are required when configuring the AWS IAM
-- Role's trust relationship so that Snowflake can assume
-- the role securely.

DESC INTEGRATION INT_S3_SALES_DB;


-- ============================================================
-- 3. CREATE AN EXTERNAL STAGE
-- ============================================================
-- The Stage creates a Snowflake reference to the S3 location.
--
-- It uses:
--   - The S3 bucket as the external storage location
--   - The Storage Integration for authentication
--   - CSV as the file format
--
-- This means we do not need to specify AWS credentials
-- directly in the Stage definition.

CREATE OR REPLACE STAGE SALES_DB.RAW_SCHEMA.STG_S3_SALES_DB
  URL = 's3://sales-punith-demo/'
  STORAGE_INTEGRATION = INT_S3_SALES_DB
  FILE_FORMAT = (
      TYPE = CSV
      FIELD_DELIMITER = ','
      SKIP_HEADER = 1
  );


-- ============================================================
-- 4. LIST FILES IN THE S3 LOCATION
-- ============================================================
-- LIST checks the files available in the external stage.
--
-- It is useful for verifying that:
--   1. Snowflake can access the S3 bucket
--   2. The Storage Integration is configured correctly
--   3. The expected files are present

LIST @SALES_DB.RAW_SCHEMA.STG_S3_SALES_DB;


-- ============================================================
-- 5. LOAD DATA FROM S3 INTO SNOWFLAKE
-- ============================================================
-- COPY INTO loads the CSV files from the external stage
-- into the Snowflake target table.
--
-- Source:
--   @SALES_DB.RAW_SCHEMA.STG_S3_SALES_DB
--
-- Target:
--   SALES_DB.RAW_SCHEMA.ORDER_RAW
--
-- The CSV file format tells Snowflake:
--   - Files are CSV
--   - Columns are separated by commas
--   - The first row contains column headers and should be skipped

COPY INTO SALES_DB.RAW_SCHEMA.ORDER_RAW
FROM @SALES_DB.RAW_SCHEMA.STG_S3_SALES_DB
FILE_FORMAT = (
    TYPE = CSV
    FIELD_DELIMITER = ','
    SKIP_HEADER = 1
);