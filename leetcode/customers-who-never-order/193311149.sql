# title: customers-who-never-order
# detail: https://leetcode.com/submissions/detail/193311149/
# datetime: Tue Dec  4 18:06:51 2018
# runtime: 228 ms
# memory: N/A

# Write your MySQL query statement below
SELECT c.Name as 'Customers'
FROM `Customers` as c LEFT JOIN `Orders` as o
ON c.Id = o.CustomerId 
WHERE o.Id IS NULL;