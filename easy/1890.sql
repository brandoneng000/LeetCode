SELECT
    DISTINCT user_id,
    MAX(time_stamp) as last_stamp
FROM
    logins
WHERE
    YEAR(time_stamp) = '2020'
GROUP BY 
    user_id;