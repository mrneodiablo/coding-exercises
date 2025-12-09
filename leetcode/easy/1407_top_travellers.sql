SELECT Users.name, IFNULL(SUM(distance),0) as travelled_distance FROM Rides
    RIGHT JOIN Users ON Users.id = Rides.user_id 
    GROUP BY Rides.user_id 
    ORDER BY travelled_distance DESC, Users.name ASC
