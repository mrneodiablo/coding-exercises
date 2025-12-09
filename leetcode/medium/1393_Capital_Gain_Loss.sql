SELECT stock_name, SUM(CASE 
                        WHEN operation = 'Buy' THEN 0-price
                        WHEN operation = 'Sell' THEN price
                    END) as capital_gain_loss
    FROM Stocks
    GROUP BY stock_name
