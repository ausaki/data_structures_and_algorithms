# title: second-highest-salary
# detail: https://leetcode.com/submissions/detail/473748008/
# datetime: Mon Mar 29 13:45:10 2021
# runtime: 181 ms
# memory: 0B

# Write your MySQL query statement below
select max(Salary) as SecondHighestSalary from Employee where Salary not in (select max(Salary) from Employee)