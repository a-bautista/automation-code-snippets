/*
Author: Alejandro Bautista Ramos
Creation date: 2018/11/19

Purpose of the query: The following query has 2 variants to answer the following questions: 
					1) Who opened some specific forms (attached in the txt file that is shown below) and when were these forms opened.
					2) Who opened some specific forms (attached in the txt file that is shown below), when were these forms opened and in which sites were these forms opened?
In order to use this query, insert into the txt file who_opened_these_forms.txt the forms that you want to look for and then execute this query with either of the variants.

In order to use the second variant, comment the lines of code that say -- this line detects who and when the specific forms were opened and uncomment the lines of code that say
-- select user_making_change, date_of_change, LogDesc, sitename, --this line detect who, when and in which site the specific forms were opened. By default, the first 
variant is activated.

*/

declare @StartDate DATETIME, @EndDate DATETIME

set @StartDate = '2018-01-01 00:00:00'
set @EndDate = GETDATE();

--Create dummy tables to dump results

if OBJECT_ID('tempdb..#Modified_Form') is not NULL drop table #Modified_Form
create table #Modified_Form ([user_making_change] varchar(30), [date_of_change] varchar(50), [LogDesc] varchar(100), [sitename] varchar(25))

if OBJECT_ID('tempdb..#Forms_To_Review') is not NULL drop table #Forms_To_Review
create table #Forms_To_Review ([form_to_be_reviewed] varchar(50))

--Start inserting the data in these dummy tables

-- Insert the data that will be searched from the .txt file

bulk insert #Forms_To_Review from 'C:\Temp\userX\who_opened_these_forms.txt' with (rowterminator = '\n')


 insert into #Modified_Form(user_making_change, date_of_change, LogDesc, sitename) select [Username] as User_Making_Change, [RecordDate] 
 as Date_of_Change, LogDesc, 'Another Site' as [SiteName] FROM [SL_XXX_App].[dbo].[AuditLog] WHERE [MessageType] = 2 
 AND [RecordDate] BETWEEN @StartDate and @EndDate


 insert into #Modified_Form(user_making_change, date_of_change, LogDesc, sitename) select [Username] as User_Making_Change, [RecordDate] 
 as Date_of_Change, LogDesc, 'Another Site' as [SiteName] FROM [SL_XXX_App].[dbo].[AuditLog] WHERE [MessageType] = 2  
 AND [RecordDate] BETWEEN @StartDate and @EndDate


 insert into #Modified_Form(user_making_change, date_of_change, LogDesc, sitename) select [Username] as User_Making_Change, [RecordDate] 
 as Date_of_Change, LogDesc, 'Another Site' as [SiteName] FROM [SL_XXX_App].[dbo].[AuditLog] WHERE [MessageType] = 2  
 AND [RecordDate] BETWEEN @StartDate and @EndDate
 

insert into #Modified_Form(user_making_change, date_of_change, LogDesc, sitename) SELECT [Username] as User_Making_Change, [RecordDate] 
as Date_of_Change, LogDesc, 'Another Site' as [SiteName] FROM [SL_XXX_App].[dbo].[AuditLog] WHERE [MessageType] = 2  
AND [RecordDate] BETWEEN @StartDate and @EndDate
    

insert into #Modified_Form(user_making_change, date_of_change, LogDesc, sitename) SELECT [Username] as User_Making_Change, [RecordDate] 
as Date_of_Change, LogDesc, 'Another Site' as [SiteName] FROM [SL_XXX_App].[dbo].[AuditLog] WHERE [MessageType] = 2  
AND [RecordDate] BETWEEN @StartDate and @EndDate


insert into #Modified_Form(user_making_change, date_of_change, LogDesc, sitename) SELECT [Username] as User_Making_Change, [RecordDate] 
as Date_of_Change, LogDesc, 'Another Site' as [SiteName] FROM [SL_XXX_App].[dbo].[AuditLog] WHERE [MessageType] = 2  
AND [RecordDate] BETWEEN @StartDate and @EndDate


insert into #Modified_Form(user_making_change, date_of_change, LogDesc, sitename) SELECT [Username] as User_Making_Change, [RecordDate] 
as Date_of_Change, LogDesc, 'Another Site' as [SiteName] FROM [SL_XXX_App].[dbo].[AuditLog] WHERE [MessageType] = 2  
AND [RecordDate] BETWEEN @StartDate and @EndDate


insert into #Modified_Form(user_making_change, date_of_change, LogDesc, sitename) SELECT [Username] as User_Making_Change, [RecordDate] 
as Date_of_Change, LogDesc, 'Another Site' as [SiteName] FROM [SL_XXX_App].[dbo].[AuditLog] WHERE [MessageType] = 2  
AND [RecordDate] BETWEEN @StartDate and @EndDate


insert into #Modified_Form(user_making_change, date_of_change, LogDesc, sitename) SELECT [Username] as User_Making_Change, [RecordDate] 
as Date_of_Change, LogDesc, 'Another Site' as [SiteName] FROM [SL_XXX_App].[dbo].[AuditLog] WHERE [MessageType] = 2  
AND [RecordDate] BETWEEN @StartDate and @EndDate


insert into #Modified_Form(user_making_change, date_of_change, LogDesc, sitename) SELECT [Username] as User_Making_Change, [RecordDate] 
as Date_of_Change, LogDesc, 'Another Site' as [SiteName] FROM [SL_XXX_App].[dbo].[AuditLog] WHERE [MessageType] = 2  
AND [RecordDate] BETWEEN @StartDate and @EndDate


insert into #Modified_Form(user_making_change, date_of_change, LogDesc, sitename) SELECT [Username] as User_Making_Change, [RecordDate] 
as Date_of_Change, LogDesc, 'Another Site' as [SiteName] FROM [SL_XXX_App].[dbo].[AuditLog] WHERE [MessageType] = 2  
AND [RecordDate] BETWEEN @StartDate and @EndDate


insert into #Modified_Form(user_making_change, date_of_change, LogDesc, sitename) SELECT [Username] as User_Making_Change, [RecordDate] 
as Date_of_Change, LogDesc, 'Another Site' as [SiteName] FROM [SL_XXX_App].[dbo].[AuditLog] WHERE [MessageType] = 2  
AND [RecordDate] BETWEEN @StartDate and @EndDate


--select substring(LogDesc, 6, CHARINDEX('(', LogDesc)-7) as Form from #Modified_Form, #Forms_To_Review where LogDesc like 'Form%' and #Forms_To_Review.form_to_be_reviewed = substring(LogDesc, 6, CHARINDEX('(', LogDesc)-7)
--substring(column to be analyzed, starting position, ending position but notice that I am indicating to locate the ( and then subtract certain amount of spaces until I get the complete name of the form

-- Compare the forms from the txt file with the forms that were found in the SQL query
With Forms as (
	select user_making_change, date_of_change, LogDesc, -- this line detects who and when the specific forms were opened
	-- select user_making_change, date_of_change, LogDesc, sitename, --this line detect who, when and in which site the specific forms were opened
	-- ROW_NUMBER() over (partition by user_making_change, LogDesc, sitename order by date_of_change) as RowNumber --this line detect who, when and in which site the specific forms were opened
	ROW_NUMBER() over (partition by LogDesc order by LogDesc) as RowNumber -- this line detects who and when the specific forms were opened
	from #Modified_Form, #Forms_To_Review 
	where #Forms_To_Review.form_to_be_reviewed = #Modified_Form.LogDesc
	) 
	-- select user_making_change, date_of_change, LogDesc, sitename from Forms where RowNumber < 2 order by convert(datetime, date_of_change) desc --this line detect who, when and in which site the specific forms were opened
	select user_making_change, date_of_change, LogDesc from Forms where RowNumber < 2 order by convert(datetime, date_of_change) desc -- this line detects who and when the specific forms were opened

--drop the dummy tables
drop table #Modified_Form
drop table #Forms_To_Review