# title: rank-scores
# detail: https://leetcode.com/submissions/detail/284276232/
# datetime: Sat Dec  7 15:02:21 2019
# runtime: 564 ms
# memory: 0B

# Write your MySQL query statement below
select Score, convert(Rank, signed integer) as Rank from
(
    select 
        Score,
        @rank := 
        case
            when Score = @score then @rank
            else @rank + 1
        end as Rank,
        @score := Score
    from 
        Scores,
        (select @rank:=0, @score:=null) t1
    order by Score desc
) t2


