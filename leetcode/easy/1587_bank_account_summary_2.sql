SELECT Users.name, SUM(Transactions.amount) as balance
    FROM Users
    JOIN Transactions ON Transactions.account = Users.account
    GROUP BY Transactions.account
    HAVING SUM(Transactions.amount) > 10000
