SELECT tmp.activity_date as day, COUNT(*) as active_users  FROM
   ( SELECT activity_date, COUNT(*) as active_users
            FROM Activity 
            WHERE activity_date BETWEEN DATE_SUB("2019-07-27", INTERVAL 29 DAY) AND '2019-07-27'
            GROUP BY activity_date, user_id
    ) tmp
    GROUP BY tmp.activity_date
    ORDER BY day ASC
