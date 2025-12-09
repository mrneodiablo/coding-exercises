SELECT E1.name as Employee 
    FROM Employee as E1
    INNER JOIN Employee as E2
    ON E2.id = E1.managerId
    WHERE E1.salary > E2.salary
