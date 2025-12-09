DELETE FROM Person
    WHERE Person.id IN (
        SELECT id FROM (SELECT P1.id
        FROM Person P1, Person P2
        WHERE P1.id > P2.id AND P1.email = P2.email) as t
    )
