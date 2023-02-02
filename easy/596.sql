SELECT class 
FROM courses
GROUP BY class
WHERE COUNT(class) >= 5;