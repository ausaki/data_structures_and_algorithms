# title: exchange-seats
# detail: https://leetcode.com/submissions/detail/287752808/
# datetime: Sun Dec 22 22:00:57 2019
# runtime: 975 ms
# memory: 0B

# Write your MySQL query statement below
select 
    case
        when mod(id, 2) = 1 and id != total then id + 1
        when mod(id, 2) = 1 then id
        else id - 1
    end as id,
    student
from 
    seat, (select count(*) as total from seat) as tmp
order by id