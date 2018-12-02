/*
Author: Alejandro Bautista Ramos
Creation date: 2018/11/30

Purpose of the query: The following query extracts the all the unique vendors from all our sites that were added in a given timeframe.
Version 1: Fully working query.
Notes: 
      1. A new vendors should be always added directly through the parent site and then the vendors are replicated through our other sites.

*/

declare @start_date varchar(15), @end_date varchar(15)
set @start_date = '2018-01-01'
set @end_date   = '2018-09-30'


if OBJECT_ID('tempdb..#Vendor_population') is not NULL 
drop table #Vendor_population

create table #Vendor_population 
	(
	 [SiteName]   varchar(30),
	 [vend_num]   varchar(30),
	 [name]       varchar(60),
	 [CreatedBy]  varchar(15), 
	 [CreateDate] datetime, 
	 [updatedby]  varchar(15), 
	 [recorddate] datetime
	 ) 

insert into #Vendor_population (
			[SiteName],
			[vend_num],
			[name],
			[CreatedBy],
			[CreateDate],
			[updatedby], 
			[recorddate] )
				SELECT 'SL_XXX_APP' as [SiteName], vend_num,name, CreatedBy, CreateDate, updatedby, recorddate
				from [SL_XXX_App].[dbo].[vendaddr] 
				where [createdate] between @start_date and @end_date
			
			
insert into #Vendor_population (
			[SiteName],
			[vend_num],
			[name],
			[CreatedBy], 
			[CreateDate], 
			[updatedby], 
			[recorddate])
				SELECT 'SL_XXX_App' as [SiteName], vend_num,name, CreatedBy, CreateDate, updatedby, recorddate
				from [SL_XXX_App].[dbo].[vendaddr] 
				where [createdate] between @start_date and @end_date
				
insert into #Vendor_population (
			[SiteName],
			[vend_num],
			[name],
			[CreatedBy], 
			[CreateDate], 
			[updatedby], 
			[recorddate])
				SELECT 'SL_XXX_App' as [SiteName], vend_num,name, CreatedBy, CreateDate, updatedby, recorddate
				from [SL_XXX_App].[dbo].[vendaddr] 
				where [createdate] between @start_date and @end_date

;


WITH UniqueVendor As(
				  select [SiteName],[vend_num],[name],[CreatedBy],[CreateDate],[updatedby],[recorddate], 
				  ROW_NUMBER() over (PARTITION by vend_num order by vend_num) as RowNumber
				  from #Vendor_population
)


select * from UniqueVendor where RowNumber < 2 order by createdate asc

drop table #Vendor_population





