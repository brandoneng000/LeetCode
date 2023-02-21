SELECT user_id, 
CONCAT(LEFT(UPPER(name), 1), SUBSTRING(LOWER(name), 2, LENGTH(name))) as name
FROM users
ORDER BY user_id;