SELECT
    DISTINCT w1.id
FROM
    weather w1,
    weather w2
WHERE
    w1.recordDate = DATE_SUB(w2.recordDate, INTERVAL -1 DAY)
AND
    w1.temperature > w2.temperature;