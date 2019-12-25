# title: rank-scores
# detail: https://leetcode.com/submissions/detail/284273971/
# datetime: Sat Dec  7 14:47:10 2019
# runtime: 773 ms
# memory: 0B

# Write your MySQL query statement below
select 
    Score, 
    (
        select count(Score) + 1 from (select Score from Scores group by Score) s2 where Score > s1.Score
    ) as Rank
from Scores s1
order by Score desc

