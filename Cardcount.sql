-- Step 1: Create the database called 'CardCount'
CREATE DATABASE IF NOT EXISTS CardCount;

-- Step 2: Use the 'CardCount' database
USE CardCount;

-- Step 3: View the current card frequency data
SELECT * FROM cardfrequency;

-- Step 4: Delete specific cards (e.g., 'Swamp', 'Mountain', etc.)
SET SQL_SAFE_UPDATES = 0;  -- Disable safe updates temporarily

DELETE FROM cardfrequency WHERE card_name = 'Swamp';
DELETE FROM cardfrequency WHERE card_name = 'Mountain';
DELETE FROM cardfrequency WHERE card_name = 'Plains';
DELETE FROM cardfrequency WHERE card_name = 'Wastes';
DELETE FROM cardfrequency WHERE card_name = 'Island';
DELETE FROM cardfrequency WHERE card_name = 'Forest';

SET SQL_SAFE_UPDATES = 1;  -- Re-enable safe updates

-- Step 5: Verify if the deletion was successful
SELECT * FROM cardfrequency;

-- Step 6: View the top 10 most played cards by total frequency
SELECT card_name, SUM(frequency) AS total_frequency
FROM cardfrequency
GROUP BY card_name
ORDER BY total_frequency DESC
LIMIT 10;

-- Step 7: Create a new table for the top 10 most played cards
CREATE TABLE top_10_most_played_cards AS
SELECT card_name, SUM(frequency) AS total_frequency
FROM cardfrequency
GROUP BY card_name
ORDER BY total_frequency DESC
LIMIT 10;

-- Step 8: Verify the newly created table
SELECT * FROM top_10_most_played_cards;
