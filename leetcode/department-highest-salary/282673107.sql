# title: department-highest-salary
# detail: https://leetcode.com/submissions/detail/282673107/
# datetime: Sat Nov 30 20:38:34 2019
# runtime: 2306 ms
# memory: 0B

# Write your MySQL query statement below
SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Salary
FROM
    Employee
        JOIN
    Department ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
	)