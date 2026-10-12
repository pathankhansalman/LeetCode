# Write your MySQL query statement below
select t.activity_date day, count(t.user_id) active_users
from (select distinct user_id, activity_date
from Activity) t
where t.activity_date >= date("2019-06-28") and t.activity_date <= date("2019-07-27")
group by t.activity_date