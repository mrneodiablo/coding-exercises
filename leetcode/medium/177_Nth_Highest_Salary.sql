CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
declare m INT;
set m=N-1;
  RETURN (
     SELECT
        CASE 
            WHEN COUNT(distinct salary)<N THEN null
            ELSE (select distinct salary from Employee order by salary desc limit 1 offset m)
        END
      from Employee
      
  );
END
