-- ============================================================
-- Snowpipe Auto-Ingest
-- This script demonstrates how to create a Snowpipe
-- with auto-ingest enabled, allowing for continuous
-- data ingestion from an S3 bucket into a Snowflake table.
-- ============================================================

-- ============================================================
-- 1. CREATE SNOWPIPE WITH AUTO-INGEST
-- ============================================================

-- Snowpipe is a continuous data ingestion service in Snowflake.
--
-- Unlike a normal COPY INTO command, Snowpipe can automatically
-- load new files as they arrive in the external S3 location.
--
-- AUTO_INGEST = TRUE tells Snowflake that this pipe will use
-- cloud event notifications to detect new files.
--
-- The overall flow is:
--
--   S3 Bucket
--       ↓
--   S3 Event Notification
--       ↓
--   SQS Queue
--       ↓
--   Snowpipe
--       ↓
--   Snowflake Table
--
-- Snowpipe uses the existing external stage to access S3.


CREATE OR REPLACE PIPE SALES_DB.RAW_SCHEMA.PIPE_ORDER_AUTO

  AUTO_INGEST = TRUE

  AS

  COPY INTO SALES_DB.RAW_SCHEMA.ORDER_RAW

  FROM @SALES_DB.RAW_SCHEMA.STG_S3_SALES_DB

  FILE_FORMAT = (
      TYPE = CSV
      FIELD_DELIMITER = ','
      SKIP_HEADER = 1
  )

  ON_ERROR = 'CONTINUE';


-- ============================================================
-- 2. SHOW SNOWPIPES
-- ============================================================

-- SHOW PIPES displays the pipes available in Snowflake.
--
-- This is useful for verifying that:
--
--   1. The pipe was created successfully
--   2. The pipe name is correct
--   3. AUTO_INGEST is enabled
--   4. The pipe is associated with the expected stage
--
-- The LIKE condition filters the result to our pipe.

SHOW PIPES LIKE 'PIPE_ORDER_AUTO';


-- ============================================================
-- 3. DESCRIBE THE SNOWPIPE
-- ============================================================

-- DESC PIPE displays detailed information about the pipe.
--
-- It helps us verify the pipe configuration, including:
--
--   - Pipe name
--   - Auto-ingest status
--   - Source stage
--   - Target table
--   - COPY INTO definition
--   - Notification channel information
--
-- The notification channel is important for AUTO_INGEST
-- because Snowpipe uses cloud event notifications to know
-- when new files are available.

DESC PIPE SALES_DB.RAW_SCHEMA.PIPE_ORDER_AUTO;


-- ============================================================
-- 4. CHECK SNOWPIPE STATUS
-- ============================================================

-- SYSTEM$PIPE_STATUS returns the current status of the pipe.
--
-- This is one of the most useful commands when troubleshooting
-- Snowpipe.
--
-- It can provide information such as:
--
--   - Execution state
--   - Pending files
--   - Last received notification
--   - Last completed file
--   - Error information
--
-- Use this command to verify whether Snowpipe is actively
-- processing incoming files.

SELECT SYSTEM$PIPE_STATUS(
    'SALES_DB.RAW_SCHEMA.PIPE_ORDER_AUTO'
);


-- ============================================================
-- 5. VIEW SNOWPIPE LOAD HISTORY
-- ============================================================

-- COPY_HISTORY shows files that have been processed by
-- Snowflake's COPY INTO operations, including files loaded
-- through Snowpipe.
--
-- This query filters the history for the ORDERS_RAW table
-- and checks the last one hour.
--
-- Useful information includes:
--
--   - FILE_NAME
--   - STAGE_LOCATION
--   - LAST_LOAD_TIME
--   - ROW_COUNT
--   - ROW_PARSED
--   - FILE_SIZE
--   - ERROR INFORMATION
--
-- This allows us to verify whether Snowpipe successfully
-- loaded the incoming S3 files.

SELECT *
FROM TABLE(
    SALES_DB.INFORMATION_SCHEMA.COPY_HISTORY(
        TABLE_NAME => 'SALES_DB.RAW_SCHEMA.ORDER_RAW',
        START_TIME => DATEADD(
            hours,
            -1,
            CURRENT_TIMESTAMP()
        )
    )
);


-- ============================================================
-- 6. VERIFY DATA IN THE TARGET TABLE
-- ============================================================

-- After Snowpipe processes the files, we can query the
-- target table to verify that the data has been loaded.
--
-- This confirms that the data successfully moved from:
--
--   S3 → Snowpipe → Snowflake Table

SELECT *
FROM SALES_DB.RAW_SCHEMA.ORDER_RAW;


-- ============================================================
-- 7. TEMPORARILY PAUSE SNOWPIPE
-- ============================================================

-- PIPE_EXECUTION_PAUSED = TRUE temporarily stops the pipe
-- from processing new files.
--
-- This does NOT delete the pipe.
--
-- The pipe remains available and can be resumed later.
--
-- This is useful when:
--
--   - Performing maintenance
--   - Troubleshooting
--   - Temporarily stopping ingestion
--   - Testing different configurations

ALTER PIPE SALES_DB.RAW_SCHEMA.PIPE_ORDER_AUTO
SET PIPE_EXECUTION_PAUSED = TRUE;


-- ============================================================
-- 8. RESUME SNOWPIPE
-- ============================================================

-- When the pipe needs to start processing files again,
-- change PIPE_EXECUTION_PAUSED to FALSE.
--
-- This resumes Snowpipe execution.

ALTER PIPE SALES_DB.RAW_SCHEMA.PIPE_ORDER_AUTO
SET PIPE_EXECUTION_PAUSED = FALSE;


-- ============================================================
-- 9. DELETE THE SNOWPIPE
-- ============================================================

-- DROP PIPE permanently removes the Snowpipe object.
--
-- This should only be used when the pipe is no longer required.
--
-- Dropping the pipe does NOT delete:
--
--   - Files from the S3 bucket
--   - The external stage
--   - The target Snowflake table
--
-- It only removes the Snowpipe object.

DROP PIPE SALES_DB.RAW_SCHEMA.PIPE_ORDER_AUTO;