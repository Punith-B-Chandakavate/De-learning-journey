// Use admin role to grant access
USE ROLE ACCOUNTADMIN;

// ----------- Data analysts ----------------  //

// The role needs compute power to run queries.
GRANT USAGE ON WAREHOUSE BI_PROD_WH TO ROLE DATA_ANALYST;

// The role must be able to “see” and “use” these objects before it can query them.
GRANT USAGE ON DATABASE SALES_DB TO ROLE DATA_ANALYST;
GRANT USAGE ON SCHEMA SALES_DB.RAW_SCHEMA TO ROLE DATA_ANALYST;

// Now give data-level access such as SELECT, INSERT, UPDATE, etc.
GRANT SELECT ON ALL TABLES IN SCHEMA SALES_DB.RAW_SCHEMA TO ROLE DATA_ANALYST;

// Verify grants
SHOW GRANTS TO ROLE DATA_ANALYST;

// revoke access
REVOKE SELECT ON ALL TABLES IN SCHEMA SALES_DB.RAW_SCHEMA FROM ROLE DATA_ANALYST;


// ----------- Data Engineers ----------------  //

// The role needs compute power to run queries.
GRANT USAGE ON WAREHOUSE ETL_DEV_WH TO ROLE DATA_ENGINEERS;

// The role must be able to “see” and “use” these objects before it can query them.
GRANT USAGE ON DATABASE SALES_DB TO ROLE DATA_ENGINEERS;
GRANT USAGE ON SCHEMA SALES_DB.RAW_SCHEMA TO ROLE DATA_ENGINEERS;

// Now give data-level access such as SELECT, INSERT, UPDATE, etc.
GRANT SELECT, UPDATE, INSERT ON ALL TABLES IN SCHEMA SALES_DB.RAW_SCHEMA TO ROLE DATA_ENGINEERS;

// If you also want the role to access future tables (those that will be created later), use:
GRANT SELECT, UPDATE, INSERT ON FUTURE TABLES IN SCHEMA SALES_DB.RAW_SCHEMA TO ROLE DATA_ENGINEERS;

// If the role should be allowed to create objects (e.g., tables or views):
GRANT CREATE TABLE ON SCHEMA SALES_DB.RAW_SCHEMA TO ROLE DATA_ENGINEERS;
GRANT CREATE VIEW ON SCHEMA SALES_DB.RAW_SCHEMA TO ROLE DATA_ENGINEERS;

// Verify grants
SHOW GRANTS TO ROLE DATA_ENGINEERS;




