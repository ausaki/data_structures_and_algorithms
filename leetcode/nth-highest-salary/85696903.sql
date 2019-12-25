# title: nth-highest-salary
# detail: https://leetcode.com/submissions/detail/85696903/
# datetime: Thu Dec 15 10:09:44 2016
# runtime: 650 ms
# memory: N/A

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE s_count INT;
    DECLARE result INT;
    select count(*) into s_count From (select  distinct Salary from Employee order by Salary desc) AS tmp;
    IF (s_count < N) THEN
        SET result=null;
    ELSE
            SELECT tmp.Salary INTO result
            FROM (
                SELECT Salary FROM Employee GROUP BY Salary DESC LIMIT N
            ) AS tmp 
            ORDER BY tmp.Salary LIMIT 1;
    END IF;
    RETURN (result);
END