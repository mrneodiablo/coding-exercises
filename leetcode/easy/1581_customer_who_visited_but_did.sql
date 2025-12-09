SELECT v.customer_id, SUM(IF(t.transaction_id,0,1)) as count_no_trans FROM Visits v
    LEFT JOIN Transactions t ON v.visit_id = t.visit_id
    GROUP BY v.customer_id
    HAVING count_no_trans > 0
