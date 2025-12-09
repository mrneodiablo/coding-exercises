SELECT Product.product_id, Product.product_name FROM Product
    JOIN Sales ON Product.product_id =  Sales.product_id 
    WHERE Product.product_id NOT IN (
            SELECT DISTINCT product_id FROM Sales
                WHERE sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31'
    )
    GROUP BY Product.product_id
