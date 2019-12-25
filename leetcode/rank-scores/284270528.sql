# title: rank-scores
# detail: https://leetcode.com/submissions/detail/284270528/
# datetime: Sat Dec  7 14:24:58 2019
# runtime: 1115 ms
# memory: 0B

# Write your MySQL query statement below
select 
    Scores.Score, tt.row_number as Rank
from Scores
join
    (select  
        t1.Score,(@row_number:=@row_number + 1) as row_number
     from
        (select Score from Scores group by Score desc) t1,
        (select @row_number:=0) as t2
    ) tt
on Scores.Score = tt.Score
order by Score desc

