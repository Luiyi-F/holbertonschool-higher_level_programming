-- Creates the table unique_id
-- Set default value in id
-- Set unique vale in id
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
)