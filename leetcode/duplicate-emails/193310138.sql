# title: duplicate-emails
# detail: https://leetcode.com/submissions/detail/193310138/
# datetime: Tue Dec  4 17:54:33 2018
# runtime: 216 ms
# memory: N/A

# Write your MySQL query statement below
SELECT DISTINCT t1.Email
FROM Person t1
JOIN Person t2
ON t1.email = t2.email and t1.id <> t2.id