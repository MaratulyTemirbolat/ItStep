create database aero
go
USE aero
GO
PRINT N'Recreating the objects for the database'
--Drop all FKs in the database
declare @table_name sysname, @constraint_name sysname
declare i cursor static for 
select c.table_name, a.constraint_name
from INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS a join INFORMATION_SCHEMA.KEY_COLUMN_USAGE b
on a.unique_constraint_name=b.constraint_name join INFORMATION_SCHEMA.KEY_COLUMN_USAGE c
on a.constraint_name=c.constraint_name
WHERE upper(c.table_name) in (upper('company'),upper('pass_in_trip'),upper('passenger'),upper('trip'))
open i
fetch next from i into @table_name,@constraint_name
while @@fetch_status=0
begin
	exec('ALTER TABLE '+@table_name+' DROP CONSTRAINT '+@constraint_name)
	fetch next from i into @table_name,@constraint_name
end
close i
deallocate i
GO
--Drop all tables
declare @object_name sysname, @sql varchar(8000)
declare i cursor static for 
SELECT table_name from INFORMATION_SCHEMA.TABLES
where upper(table_name) in (upper('company'),upper('pass_in_trip'),upper('passenger'),upper('trip'))

open i
fetch next from i into @object_name
while @@fetch_status=0
begin
	set @sql='DROP TABLE [dbo].['+@object_name+']'
	exec(@sql)
	fetch next from i into @object_name
end
close i
deallocate i
GO

CREATE TABLE [dbo].[company] (
	[id_comp] [int] NOT NULL ,
	[name] [char] (10) NOT NULL 
)
GO

CREATE TABLE [dbo].[pass_in_trip] (
	[trip_no] [int] NOT NULL ,
	[date] [datetime] NOT NULL ,
	[id_psg] [int] NOT NULL ,
	[place] [char] (10) NOT NULL 
)
GO

CREATE TABLE [dbo].[passenger] (
	[id_psg] [int] NOT NULL ,
	[name] [char] (20) NOT NULL 
)
GO

CREATE TABLE [dbo].[trip] (
	[trip_no] [int] NOT NULL ,
	[id_comp] [int] NOT NULL ,
	[plane] [char] (10) NOT NULL ,
	[town_from] [char] (25) NOT NULL ,
	[town_to] [char] (25) NOT NULL ,
	[time_out] [datetime] NOT NULL ,
	[time_in] [datetime] NOT NULL 
)
GO

ALTER TABLE [dbo].[company] WITH NOCHECK ADD 
	CONSTRAINT [PK2] PRIMARY KEY  CLUSTERED 
	(
		[id_comp]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[pass_in_trip] WITH NOCHECK ADD 
	CONSTRAINT [PK_pt] PRIMARY KEY  CLUSTERED 
	(
		[trip_no],
		[date],
		[id_psg]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[passenger] WITH NOCHECK ADD 
	CONSTRAINT [PK_psg] PRIMARY KEY  CLUSTERED 
	(
		[id_psg]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[trip] WITH NOCHECK ADD 
	CONSTRAINT [PK_t] PRIMARY KEY  CLUSTERED 
	(
		[trip_no]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[pass_in_trip] ADD 
	CONSTRAINT [FK_pass_in_trip_passenger] FOREIGN KEY 
	(
		[id_psg]
	) REFERENCES [dbo].[passenger] (
		[id_psg]
	),
	CONSTRAINT [FK_pass_in_trip_trip] FOREIGN KEY 
	(
		[trip_no]
	) REFERENCES [dbo].[trip] (
		[trip_no]
	)
GO

ALTER TABLE [dbo].[trip] ADD 
	CONSTRAINT [FK_trip_company] FOREIGN KEY 
	(
		[id_comp]
	) REFERENCES [dbo].[company] (
		[id_comp]
	)
GO
                                                                                                                                                                                                                                                                 
----company------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
insert into company values(1,'Don_avia  ')
insert into company values(2,'Aeroflot  ')
insert into company values(3,'Dale_avia ')
insert into company values(4,'air_France')
insert into company values(5,'British_AW')
GO

                                                                                                                                                                                                                                                                 
----passenger------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
insert into passenger values(1,'Bruce Willis        ')
insert into passenger values(2,'George Clooney      ')
insert into passenger values(3,'Kevin Costner       ')
insert into passenger values(4,'Donald Sutherland   ')
insert into passenger values(5,'Jennifer Lopez      ')
insert into passenger values(6,'Ray Liotta          ')
insert into passenger values(7,'Samuel L. Jackson   ')
insert into passenger values(8,'Nikole Kidman       ')
insert into passenger values(9,'Alan Rickman        ')
insert into passenger values(10,'Kurt Russell        ')
insert into passenger values(11,'Harrison Ford       ')
insert into passenger values(12,'Russell Crowe       ')
insert into passenger values(13,'Steve Martin        ')
insert into passenger values(14,'Michael Caine       ')
insert into passenger values(15,'Angelina Jolie      ')
insert into passenger values(16,'Mel Gibson          ')
insert into passenger values(17,'Michael Douglas     ')
insert into passenger values(18,'John Travolta       ')
insert into passenger values(19,'Sylvester Stallone  ')
insert into passenger values(20,'Tommy Lee Jones     ')
insert into passenger values(21,'Catherine Zeta-Jones')
insert into passenger values(22,'Antonio Banderas    ')
insert into passenger values(23,'Kim Basinger        ')
insert into passenger values(24,'Sam Neill           ')
insert into passenger values(25,'Gary Oldman         ')
insert into passenger values(26,'Clint Eastwood      ')
insert into passenger values(27,'Brad Pitt           ')
insert into passenger values(28,'Johnny Depp         ')
insert into passenger values(29,'Pierce Brosnan      ')
insert into passenger values(30,'Sean Connery        ')
insert into passenger values(31,'Bruce Willis        ')
insert into passenger values(37,'Mullah Omar         ')

GO

                                                                                                                                                                                                                                                                 
----trip------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
insert into trip values(1100,4,'Boeing    ','Rostov                   ','Paris                    ','19000101 14:30:00.000','19000101 17:50:00.000')
insert into trip values(1101,4,'Boeing    ','Paris                    ','Rostov                   ','19000101 08:12:00.000','19000101 11:45:00.000')
insert into trip values(1123,3,'TU-154    ','Rostov                   ','Vladivostok              ','19000101 16:20:00.000','19000101 03:40:00.000')
insert into trip values(1124,3,'TU-154    ','Vladivostok              ','Rostov                   ','19000101 09:00:00.000','19000101 19:50:00.000')
insert into trip values(1145,2,'IL-86     ','Moscow                   ','Rostov                   ','19000101 09:35:00.000','19000101 11:23:00.000')
insert into trip values(1146,2,'IL-86     ','Rostov                   ','Moscow                   ','19000101 17:55:00.000','19000101 20:01:00.000')
insert into trip values(1181,1,'TU-134    ','Rostov                   ','Moscow                   ','19000101 06:12:00.000','19000101 08:01:00.000')
insert into trip values(1182,1,'TU-134    ','Moscow                   ','Rostov                   ','19000101 12:35:00.000','19000101 14:30:00.000')
insert into trip values(1187,1,'TU-134    ','Rostov                   ','Moscow                   ','19000101 15:42:00.000','19000101 17:39:00.000')
insert into trip values(1188,1,'TU-134    ','Moscow                   ','Rostov                   ','19000101 22:50:00.000','19000101 00:48:00.000')
insert into trip values(1195,1,'TU-154    ','Rostov                   ','Moscow                   ','19000101 23:30:00.000','19000101 01:11:00.000')
insert into trip values(1196,1,'TU-154    ','Moscow                   ','Rostov                   ','19000101 04:00:00.000','19000101 05:45:00.000')
insert into trip values(7771,5,'Boeing    ','London                   ','Singapore                ','19000101 01:00:00.000','19000101 11:00:00.000')
insert into trip values(7772,5,'Boeing    ','Singapore                ','London                   ','19000101 12:00:00.000','19000101 02:00:00.000')
insert into trip values(7773,5,'Boeing    ','London                   ','Singapore                ','19000101 03:00:00.000','19000101 13:00:00.000')
insert into trip values(7774,5,'Boeing    ','Singapore                ','London                   ','19000101 14:00:00.000','19000101 06:00:00.000')
insert into trip values(7775,5,'Boeing    ','London                   ','Singapore                ','19000101 09:00:00.000','19000101 20:00:00.000')
insert into trip values(7776,5,'Boeing    ','Singapore                ','London                   ','19000101 18:00:00.000','19000101 08:00:00.000')
insert into trip values(7777,5,'Boeing    ','London                   ','Singapore                ','19000101 18:00:00.000','19000101 06:00:00.000')
insert into trip values(7778,5,'Boeing    ','Singapore                ','London                   ','19000101 22:00:00.000','19000101 12:00:00.000')
insert into trip values(8881,5,'Boeing    ','London                   ','Paris                    ','19000101 03:00:00.000','19000101 04:00:00.000')
insert into trip values(8882,5,'Boeing    ','Paris                    ','London                   ','19000101 22:00:00.000','19000101 23:00:00.000')

GO

                                                                                                                                                                                                                                                                 
----pass_in_trip------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
insert into pass_in_trip values(1100,'20030429 00:00:00.000',1,'1a        ')
insert into pass_in_trip values(1123,'20030405 00:00:00.000',3,'2a        ')
insert into pass_in_trip values(1123,'20030408 00:00:00.000',1,'4c        ')
insert into pass_in_trip values(1123,'20030408 00:00:00.000',6,'4b        ')
insert into pass_in_trip values(1124,'20030402 00:00:00.000',2,'2d        ')
insert into pass_in_trip values(1145,'20030405 00:00:00.000',3,'2c        ')
insert into pass_in_trip values(1181,'20030401 00:00:00.000',1,'1a        ')
insert into pass_in_trip values(1181,'20030401 00:00:00.000',6,'1b        ')
insert into pass_in_trip values(1181,'20030401 00:00:00.000',8,'3c        ')
insert into pass_in_trip values(1181,'20030413 00:00:00.000',5,'1b        ')
insert into pass_in_trip values(1182,'20030413 00:00:00.000',5,'4b        ')
insert into pass_in_trip values(1187,'20030414 00:00:00.000',8,'3a        ')
insert into pass_in_trip values(1188,'20030401 00:00:00.000',8,'3a        ')
insert into pass_in_trip values(1182,'20030413 00:00:00.000',9,'6d        ')
insert into pass_in_trip values(1145,'20030425 00:00:00.000',5,'1d        ')
insert into pass_in_trip values(1187,'20030414 00:00:00.000',10,'3d        ')
insert into pass_in_trip values(8882,'20051106 00:00:00.000',37,'1a        ') 
insert into pass_in_trip values(7771,'20051107 00:00:00.000',37,'1c        ') 
insert into pass_in_trip values(7772,'20051107 00:00:00.000',37,'1a        ') 
insert into pass_in_trip values(8881,'20051108 00:00:00.000',37,'1d        ') 
insert into pass_in_trip values(7778,'20051105 00:00:00.000',10,'2a        ') 
insert into pass_in_trip values(7772,'20051129 00:00:00.000',10,'3a        ')
insert into pass_in_trip values(7771,'20051104 00:00:00.000',11,'4a        ')
insert into pass_in_trip values(7771,'20051107 00:00:00.000',11,'1b        ')
insert into pass_in_trip values(7771,'20051109 00:00:00.000',11,'5a        ')
insert into pass_in_trip values(7772,'20051107 00:00:00.000',12,'1d        ')
insert into pass_in_trip values(7773,'20051107 00:00:00.000',13,'2d        ')
insert into pass_in_trip values(7772,'20051129 00:00:00.000',13,'1b        ')
insert into pass_in_trip values(8882,'20051113 00:00:00.000',14,'3d        ')
insert into pass_in_trip values(7771,'20051114 00:00:00.000',14,'4d        ')
insert into pass_in_trip values(7771,'20051116 00:00:00.000',14,'5d        ')
insert into pass_in_trip values(7772,'20051129 00:00:00.000',14,'1c        ')

GO

