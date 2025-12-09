SELECT id, CASE 
                WHEN p_id IS NULL THEN 'Root'
                WHEN id IS NOT NULL AND id IN (select DISTINCT p_id as parent 
                                FROM Tree
                                GROUP BY p_id) THEN 'Inner'
                ELSE 'Leaf'
            END as type
    FROM Tree
