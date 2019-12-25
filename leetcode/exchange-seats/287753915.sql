# title: exchange-seats
# detail: https://leetcode.com/submissions/detail/287753915/
# datetime: Sun Dec 22 22:10:50 2019
# runtime: 526 ms
# memory: 0B

# Write your MySQL query statement below
select 
    s1.id as id, coalesce(s2.student, s1.student) as student
from 
    seat s1 left join 
    seat s2 on (s1.id + 1) ^ 1 - 1 = s2.id
order by s1.id