# title: customers-who-never-order
# detail: https://leetcode.com/submissions/detail/193311339/
# datetime: Tue Dec  4 18:09:06 2018
# runtime: 233 ms
# memory: N/A

# Write your MySQL query statement below
# SELECT c.Name as 'Customers'
# FROM `Customers` as c LEFT JOIN `Orders` as o
# ON c.Id = o.CustomerId 
# WHERE o.Id IS NULL;

SELECT c.Name as 'Customers'
FROM `Customers` as c 
WHERE c.Id NOT IN (
SELECT DISTINCT(o.CustomerId) FROM `Orders` as o
)