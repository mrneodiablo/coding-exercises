SELECT name FROM SalesPerson
    WHERE name NOT IN (
        SELECT SalesPerson.name 
        FROM SalesPerson,Orders,Company
        WHERE Orders.sales_id=SalesPerson.sales_id AND Orders.com_id=Company.com_id
        AND Company.name='RED'
    )
