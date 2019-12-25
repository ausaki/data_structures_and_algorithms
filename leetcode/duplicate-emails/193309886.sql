# title: duplicate-emails
# detail: https://leetcode.com/submissions/detail/193309886/
# datetime: Tue Dec  4 17:52:02 2018
# runtime: 176 ms
# memory: N/A

# Write your MySQL query statement below
SELECT `Email` FROM `Person` GROUP BY `Email` HAVING COUNT(`Id`) >= 2;