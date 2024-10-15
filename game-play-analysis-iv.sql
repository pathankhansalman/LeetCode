# Write your MySQL query statement below
select round(t2.uniq_signed/count(distinct t1.player_id), 2) fraction
from Activity t1,
(select count(distinct t1.player_id) uniq_signed
from
Activity t1
inner join
(select player_id, min(event_date) as first_date
from Activity
group by player_id) t2
on t1.player_id = t2.player_id and t1.event_date = date_add(t2.first_date, interval 1 day)) t2