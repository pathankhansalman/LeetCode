# Write your MySQL query statement below
select t1.id from weather as t1
left join weather as t2
on datediff(t1.recordDate, t2.recordDate) = 1
where t1.temperature > t2.temperature