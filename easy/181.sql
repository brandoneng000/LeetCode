# Write your MySQL query statement below
SELECT 
    name as Employee 
FROM 
     employee e 
WHERE 
    managerID IS NOT NULL 
    AND salary > (
        SELECT 
        salary 
        from 
        employee 
        where 
        e.managerID = id
    );
