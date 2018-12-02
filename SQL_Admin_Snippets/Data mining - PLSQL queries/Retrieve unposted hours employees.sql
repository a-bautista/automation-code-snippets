/*
Author: Alejandro Bautista Ramos
Creation date: 2018/11/15

Purpose of the query: The following query extracts the hours from all our shop trak employees that were approved by its managers but these hours weren't posted to the system
					  because the jobs were closed. Feel free to modify the starting and ending datetimes for reviewing purposes.

*/
  declare @beginning_date datetime
  declare @ending_date    datetime
  declare @dt DATE = '1905-01-01' -- dummy date as reference for setting up the starting and ending date  
 
  set @beginning_date = convert(datetime,convert(varchar,DATEADD(WEEK,DATEDIFF(week, @dt, current_timestamp), @dt))+' '+'00:00:00')
  set @ending_date = convert(datetime,convert(varchar,dateadd(dd,6,DATEADD(WEEK,DATEDIFF(week, @dt, current_timestamp), @dt)) )+' '+'23:59:59');
   
  --set @beginning_date = '2018-11-11 00:00:00'
  --set @ending_date    = '2018-12-31 23:59:59';
  --set @ending_date      = GETDATE() ;
    
    
  -- Declare our Table expression because it will help us to remove duplicate values. 
  
  With UnpostedHours As
  (
	  select jt.emp_num, emp.name, trans_num, job, trans_type, trans_date, a_hrs, jt.ind_code,user_code, lct_emp.supervisor_primary, lct_emp.supervisor_alternate, 
	  ROW_Number() over (partition by a_hrs, trans_date, jt.emp_num order by a_hrs ) as RowNumber 
	  -- ROW_Number() over (partition by ... order by ...) indicates to put a row id number over columns a_hrs, trans_date and employee number, so for every row in the
	  -- table, SQL will assign a row id whenever trans_date, a_hrs and employee are different but if it happens that we have repeated values then row id wil assign an 
	  -- increased value for that repeated value.
	  
	  -- For the record: if you partition by the a_hrs column you run in the issue that two employees might have similar worked hours, so rowid will assign increased 
	  -- row numbers which mean that the rows appear several times but it is not the case because hours are similar but the employees with these hours are not similar.
	  -- I had to partition by 3 columns to avoid the problem of similar hours and similar trans_date.  
	  from [SL_CASPER_App].[dbo].[jobtran] jt 
		   inner join [SL_CASPER_App].[dbo].[employee] emp on emp.emp_num = jt.emp_num -- job transaction with employee relationship
		   inner join [SL_CASPER_App].[dbo].[lc_lt_employee_profile] lct_emp on jt.emp_num = lct_emp.emp_num -- job transaction with supervisor relationship
		   inner join [SL_CASPER_App].[dbo].[lc_lt_employee_profile] lct_emp_bound_two on emp.emp_num = lct_emp_bound_two.emp_num --supervisor with employee relationship
	  where posted = 0
	  and trans_date between @beginning_date and @ending_date
	) 
	select emp_num,name, trans_num, job, trans_type, trans_date, a_hrs, ind_code, user_code, supervisor_primary, supervisor_alternate 
	from UnpostedHours where RowNumber < 2 order by trans_date desc
	-- RowNumber < 2 just indicates to disregard the rows that have appeared several times 
	
--print @beginning_date;
--print @ending_date;