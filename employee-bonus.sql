# Write your MySQL query statement below
select t1.name, t2.bonus
from Employee t1
left outer join
Bonus t2
on t1.empId = t2.empId
where ifnull(t2.bonus, 500) < 1000