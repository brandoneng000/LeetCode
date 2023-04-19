SELECT
    s.score,
    temp.row_num as 'rank'
FROM 
    scores s,
    (SELECT
        score,
        row_number() OVER (
            ORDER BY score DESC
        ) row_num
    FROM
        scores
    GROUP BY
        score
    ORDER BY
        score DESC) as temp
WHERE
    s.score = temp.score
ORDER BY
    score DESC;


SELECT
    row_number() OVER (
        ORDER BY score DESC
    ) row_num
FROM
    scores
GROUP BY
    score
ORDER BY
    score DESC;