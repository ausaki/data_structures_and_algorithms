# title: employees-earning-more-than-their-managers
# detail: https://leetcode.com/submissions/detail/85636162/
# datetime: Wed Dec 14 16:54:00 2016
# runtime: 1042 ms
# memory: N/A

# Write your MySQL query statement below
SELECT employee.Name AS Employee 
FROM Employee AS employee, Employee AS manager 
WHERE employee.ManagerId = manager.Id AND employee.Salary > manager.Salary;