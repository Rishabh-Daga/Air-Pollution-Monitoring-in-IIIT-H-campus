create table comtemp(timestamp string);
delete from tp;
insert into tp select sensor, strftime('%Y-%m-%d %H:00:00', datetime) as timestamp, avg(temp) as temp from pollution_readings where sensor = 31 group by strftime('%Y-%m-%d %H', datetime);
insert into comtemp select timstamp from tp;
alter table comtemp add column n31 int;
alter table comtemp add column n32 int;
alter table comtemp add column n33 int;
alter table comtemp add column n24 int;
alter table comtemp add column n11 int;
alter table comtemp add column n12 int;
alter table comtemp add column n14 int;
update comtemp set n31 = (select temp from tp where comtemp.timestamp = tp.timestamp);
delete from tp;
insert into tp select sensor, strftime('%Y-%m-%d %H:00:00', datetime) as timestamp, avg(temp) as temp from pollution_readings where sensor = 32 group by strftime('%Y-%m-%d %H', datetime);
update comtemp set n32 = (select temp from tp where comtemp.timestamp = tp.timestamp);
delete from tp;
insert into tp select sensor, strftime('%Y-%m-%d %H:00:00', datetime) as timestamp, avg(temp) as temp from pollution_readings where sensor = 33 group by strftime('%Y-%m-%d %H', datetime);
update comtemp set n33 = (select temp from tp where comtemp.timestamp = tp.timestamp);
delete from tp;
insert into tp select sensor, strftime('%Y-%m-%d %H:00:00', datetime) as timestamp, avg(temp) as temp from pollution_readings where sensor = 24 group by strftime('%Y-%m-%d %H', datetime);
update comtemp set n24 = (select temp from tp where comtemp.timestamp = tp.timestamp);
delete from tp;
insert into tp select sensor, strftime('%Y-%m-%d %H:00:00', datetime) as timestamp, avg(temp) as temp from pollution_readings where sensor = 11 group by strftime('%Y-%m-%d %H', datetime);
update comtemp set n11 = (select temp from tp where comtemp.timestamp = tp.timestamp);
delete from tp;
insert into tp select sensor, strftime('%Y-%m-%d %H:00:00', datetime) as timestamp, avg(temp) as temp from pollution_readings where sensor = 12 group by strftime('%Y-%m-%d %H', datetime);
update comtemp set n12 = (select temp from tp where comtemp.timestamp = tp.timestamp);
delete from tp;
insert into tp select sensor, strftime('%Y-%m-%d %H:00:00', datetime) as timestamp, avg(temp) as temp from pollution_readings where sensor = 14 group by strftime('%Y-%m-%d %H', datetime);
update comtemp set n14 = (select temp from tp where comtemp.timestamp = tp.timestamp);
