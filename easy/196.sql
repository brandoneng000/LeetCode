-- DELETE
--     p1
-- FROM
--     person p1,
--     person p2
-- WHERE 
--     p1.email = p2.email
-- AND
--     p1.id > p2.id

DELETE FROM
    person
WHERE 
    id
NOT IN (
        SELECT
            *
        FROM
            (
                SELECT
                    MIN(id)
                FROM
                    person
                GROUP BY
                    email
            ) as tmp 
    )