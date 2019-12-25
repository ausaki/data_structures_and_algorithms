# title: consecutive-numbers
# detail: https://leetcode.com/submissions/detail/284281770/
# datetime: Sat Dec  7 15:40:27 2019
# runtime: 1042 ms
# memory: 0B

# Write your MySQL query statement below
select distinct l1.Num as ConsecutiveNums
from 
    Logs l1
    inner join Logs l2 on (l2.Id = l1.Id + 1 and l2.Num = l1.Num)
    inner join Logs l3 on (l3.Id = l1.Id + 2 and l3.Num = l1.Num)
