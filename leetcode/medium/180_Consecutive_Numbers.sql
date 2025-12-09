SELECT distinct l1.num ConsecutiveNums 
FROM logs l1 
JOIN logs l2 on l1.id = l2.id+1 and l1.num = l2.num
JOIN logs l3 on l1.id = l3.id+2 and l1.num = l3.num 
