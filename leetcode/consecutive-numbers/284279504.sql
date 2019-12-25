# title: consecutive-numbers
# detail: https://leetcode.com/submissions/detail/284279504/
# datetime: Sat Dec  7 15:24:55 2019
# runtime: 1822 ms
# memory: 0B

# Write your MySQL query statement below
select 
    distinct l1.Num as ConsecutiveNums
from Logs l1
where 
(select count(*) from Logs l2 where l2.Id in (l1.Id - 2, l1.Id - 1) and l2.Num = l1.Num) = 2