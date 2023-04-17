SELECT 
    MAX(salary) as SecondHighestSalary
FROM
    employee e 
WHERE
    salary != (
        SELECT
            MAX(salary)
        FROM
            employee
    );
    
SELECT (
    SELECT 
        DISTINCT salary
    FROM
        employee
    ORDER BY
        salary DESC 
    LIMIT 1 OFFSET 1
) as SecondHighestSalary