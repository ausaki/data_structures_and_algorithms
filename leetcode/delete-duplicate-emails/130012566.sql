# title: delete-duplicate-emails
# detail: https://leetcode.com/submissions/detail/130012566/
# datetime: Tue Nov 28 17:52:20 2017
# runtime: 1134 ms
# memory: N/A

# Write your MySQL query statement below
delete p1 from Person p1, Person p2 where p1.Email = p2.Email and p1.Id > p2.Id;