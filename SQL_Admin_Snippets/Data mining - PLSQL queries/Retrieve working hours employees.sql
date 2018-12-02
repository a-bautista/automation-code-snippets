/*
Author: Alejandro Bautista Ramos
Creation date: 2018/11/15

Purpose of the query: The following query extracts the total hours -posted and unposted hours - that shop trak employees have worked from Sunday to Saturday of a given week. 
Version 4: Fully working query.
Notes: 
      1. Hours that are approved on the same day will not be reflected until the next day.
      
*/

-- Common table expression to determine the unique hours
-- you are going to take unique values of hours based on the bef_start_time column, so in that way I will disregard values with RowNumber that have a value greater than 1


if OBJECT_ID('tempdb..#EmployeeNumber') is not NULL drop table #EmployeeNumber
create table #EmployeeNumber (ID int NOT NULL identity primary key, [employee_number] varchar(30)) --identity primary key does the trick for the id auto increment


if OBJECT_ID('tempdb..#ResultHourEmployee') is not NULL drop table #ResultHourEmployee
create table #ResultHourEmployee ([employee_number] int, [employee_name] varchar(30), [total_worked_hours] varchar(10))

print 'Inserting values into the temp table'
insert into #EmployeeNumber select emp_num from [SL_XXX_App].[dbo].employee where term_date is NULL 

declare @beginning_time datetime
declare @ending_time datetime
  
-- week 44
--set @beginning_time = '2018-10-28 00:00:00'
--set @ending_time    = '2018-11-03 23:59:59' 


-- week 46
set @beginning_time = '2018-11-25 00:00:00'
set @ending_time    = '2018-12-01 23:59:59'

--select * from #EmployeeNumber

declare @LoopCounter int = 1 --initial value of the temp EmployeeNumber table 
declare @MaxRowCounter int = (select count(id) from #EmployeeNumber) --max value of the temp EmployeeNumber table
declare @EmployeeNumber nvarchar(15) --store the employee number in this variable so you can loop with a counter
declare @EmployeeName nvarchar(15) 
declare @TotalWorkedHours decimal

-- print @MaxRowCounter

print 'Retrieving values for employees'

while (@LoopCounter <= @MaxRowCounter)
begin 
	 -- Start by selecting each employee number and id from the temp table that has these values
     select @EmployeeNumber = employee_number
     from #EmployeeNumber where id = @LoopCounter;
	 -- The code from below is more like a function that displays the total hours - posted and unposted - a given employee has worked. I had to use this loop, so for  
	 -- every employee number then display the total hours he/she has worked. 
	 With EmployeeHours As
	 (
		select  translog.emp_num, employee.name, bef_start_time, bef_hrs, 
				ROW_NUMBER() over (PARTITION by bef_start_time, translog.emp_num, bef_hrs order by bef_start_time) as RowNumber
				-- put a row number to every row considering the combo bef_start_time, emp_num and bef_hrs, that is, when a row that contains these 3 columns as unique then 
				-- an id of 1 will appear but if these 3 columns have the same values then an increased row id will appear. 
				from [SL_XXX_App].[dbo].[lc_lt_transactionlog] translog 
				inner join [SL_XXX_App].[dbo].[employee] employee on translog.emp_num = employee.emp_num
				where bef_start_time >= @beginning_time 
				and bef_end_time   <=  @ending_time 
				and translog.emp_num = convert(int,@EmployeeNumber)
				and coalesce(bef_ind_code, '') <> 'LNC' -- Do not count the Lunch hours
				and current_action not in ('U', 'D') -- It is necessary to take out these hours because they should not be considered for counting
     ) -- for each result of the CTE, insert it in the temp table
     insert into #ResultHourEmployee ([employee_number], [employee_name], [total_worked_hours]) 
			 select emp_num, name, round((sum(bef_hrs)),1) as [Total worked hours] 
			 from EmployeeHours where RowNumber < 2 group by name, emp_num 	 	 
			 set @LoopCounter = @LoopCounter + 1
end

select employee_number, employee_name, total_worked_hours, @beginning_time as [Initial Date], @ending_time as [End Date], supervisor_primary, supervisor_alternate  
	   from #ResultHourEmployee 
	   inner join [SL_XXX_App].[dbo].[lc_lt_employee_profile] lct_emp on #ResultHourEmployee.employee_number = lct_emp.emp_num -- job transaction with supervisor relationship
	   order by total_worked_hours desc
	   

drop table #EmployeeNumber
drop table #ResultHourEmployee