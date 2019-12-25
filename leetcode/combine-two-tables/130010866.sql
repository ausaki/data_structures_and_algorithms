# title: combine-two-tables
# detail: https://leetcode.com/submissions/detail/130010866/
# datetime: Tue Nov 28 17:28:09 2017
# runtime: 1105 ms
# memory: N/A

# Write your MySQL query statement below
select FirstName, LastName, City, State from Person p left join Address a on p.PersonId = a.PersonId;