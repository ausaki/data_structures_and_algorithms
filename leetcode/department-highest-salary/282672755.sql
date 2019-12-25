# title: department-highest-salary
# detail: https://leetcode.com/submissions/detail/282672755/
# datetime: Sat Nov 30 20:34:31 2019
# runtime: 828 ms
# memory: 0B

# Write your MySQL query statement below
select e1.Deparment as Department, e2.Name as Employee, e2.Salary 
from
(select d.Id, d.Name as Deparment, MAX(e.Salary) as MaxSalary 
from Department as d join Employee as e on d.Id = e.DepartmentId
group by d.Id) as e1
join Employee as e2
on e1.id = e2.DepartmentId and e1.MaxSalary = e2.Salary
