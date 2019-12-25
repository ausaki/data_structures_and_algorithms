# title: rank-scores
# detail: https://leetcode.com/submissions/detail/284273267/
# datetime: Sat Dec  7 14:42:29 2019
# runtime: 854 ms
# memory: 0B

# Write your MySQL query statement below
select 
    Score, 
    (
        select count(distinct(Score)) + 1 from Scores where Score > s1.Score
    ) as Rank
from Scores s1
order by Score desc

