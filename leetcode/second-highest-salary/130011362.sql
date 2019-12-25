# title: second-highest-salary
# detail: https://leetcode.com/submissions/detail/130011362/
# datetime: Tue Nov 28 17:34:23 2017
# runtime: 1008 ms
# memory: N/A

# Write your MySQL query statement below
select ifnull(
(select distinct Salary from Employee order by Salary desc limit 1,1),
NULL
) as SecondHighestSalary;
