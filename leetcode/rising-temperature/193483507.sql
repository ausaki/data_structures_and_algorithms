# title: rising-temperature
# detail: https://leetcode.com/submissions/detail/193483507/
# datetime: Wed Dec  5 16:04:03 2018
# runtime: 328 ms
# memory: N/A

# Write your MySQL query statement below
SELECT w1.Id AS Id
FROM Weather w1 INNER JOIN Weather w2 
ON DATEDIFF(w1.RecordDate, w2.RecordDate) = 1 AND w1.Temperature > w2.Temperature;