SELECT name, SUM(IFNULL(distance, 0)) as travelled_distance
FROM users 
LEFT JOIN rides ON users.id = rides.user_id
GROUP BY rides.user_id
ORDER BY travelled_distance DESC, name;