# title: employees-earning-more-than-their-managers
# detail: https://leetcode.com/submissions/detail/85636245/
# datetime: Wed Dec 14 16:55:10 2016
# runtime: 1122 ms
# memory: N/A

# Write your MySQL query statement below
SELECT employee.Name AS Employee 
FROM Employee AS employee, Employee AS manager 
WHERE employee.ManagerId = manager.Id AND employee.Salary > manager.Salary;