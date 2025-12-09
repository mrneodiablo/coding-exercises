SELECT user_id, MAX(IF(YEAR(time_stamp)='2020',time_stamp,0)) as last_stamp
    FROM Logins
    GROUP BY user_id
    HAVING YEAR(last_stamp)='2020'
