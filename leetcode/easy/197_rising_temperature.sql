SELECT p1.id FROM Weather p1
JOIN Weather p2
WHERE DATEDIFF(p1.recordDate,p2.recordDate) = 1
AND p1.temperature > p2.temperature
