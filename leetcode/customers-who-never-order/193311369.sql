# title: customers-who-never-order
# detail: https://leetcode.com/submissions/detail/193311369/
# datetime: Tue Dec  4 18:09:30 2018
# runtime: 240 ms
# memory: N/A

# Write your MySQL query statement below
# SELECT c.Name as 'Customers'
# FROM `Customers` as c LEFT JOIN `Orders` as o
# ON c.Id = o.CustomerId 
# WHERE o.Id IS NULL;

Select c.Name as Customers from Customers c
where c.Id not in(
select Distinct(CustomerId) from Orders)