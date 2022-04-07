# Write your MySQL query statement below
delete t1 from person t1 inner join
person t2
on t1.id > t2.id and t1.email = t2.email