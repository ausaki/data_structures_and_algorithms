# title: consecutive-numbers
# detail: https://leetcode.com/submissions/detail/284278876/
# datetime: Sat Dec  7 15:20:17 2019
# runtime: 1030 ms
# memory: 0B

# Write your MySQL query statement below
select distinct l1.Num as ConsecutiveNums
from 
    Logs l1 inner join Logs l2
on (l2.Id between l1.Id - 2 and l1.Id - 1) and l2.Num = l1.Num
group by l1.Id
having count(*) = 2