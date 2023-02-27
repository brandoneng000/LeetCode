SELECT
    employee_id,
    IF(
        MOD(employee_id, 2) = 1 
        AND LEFT(name, 1) != 'm', 
        salary, 
        0
    ) as bonus
FROM 
    employees
ORDER BY
    employee_id;