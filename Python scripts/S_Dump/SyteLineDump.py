#! Python 3.6.4
# Version 0.1 - Code that displays the latest changes in SyteLine related to groups,  license modules, users info and permissions. 
# Author: Alejandro Bautista R.

import pypyodbc, SyteLineDump_Groups, SyteLineDump_Groups_per_Site, SyteLineDump_Module_List, SyteLineDump_Modules_per_User, SyteLineDump_UserInfoAll, SyteLineDump_Not_in_Groups
from datetime import datetime
from subprocess import call

def main():
    # read the SQL queries externally
    queries = ['C:\\Temp\\Ready_to_use_queries\\SyteLine_Dump\\Group_Permissions_to_Forms.sql',
               'C:\\Temp\\Ready_to_use_queries\\SyteLine_Dump\\User_Permission_Groups_per_Site.sql',
               'C:\\Temp\\Ready_to_use_queries\\SyteLine_Dump\\Module_List.sql',
               'C:\\Temp\\Ready_to_use_queries\\SyteLine_Dump\\Modules_per_User.sql',
               'C:\\Temp\\Ready_to_use_queries\\SyteLine_Dump\\UserInfo.sql',
               'C:\\Temp\\Ready_to_use_queries\\SyteLine_Dump\\User_Permissions_not_Groups.sql']

    for index, query in enumerate(queries):
        #print(query)
        cursor = initiate_connection_db()
        results = retrieve_results_query(cursor, query)
        if index == 0:
            SyteLineDump_Groups.write_to_workbook(results)
            print("The workbook has been created and data has been inserted.\n")
        elif index == 1: 
            SyteLineDump_Groups_per_Site.write_to_workbook(results)
            print("The workbook has been updated and data has been inserted.\n")
        elif index == 2: 
            SyteLineDump_Module_List.write_to_workbook(results)
            print("The workbook has been updated and data has been inserted.\n")
        elif index == 3: 
            SyteLineDump_Modules_per_User.write_to_workbook(results)
            print("The workbook has been updated and data has been inserted.\n")
        elif index == 4: 
            SyteLineDump_UserInfoAll.write_to_workbook(results)
            print("The workbook has been updated and data has been inserted.\n")
        elif index == 5: 
            SyteLineDump_Not_in_Groups.write_to_workbook(results)
            print("The workbook has been updated and data has been inserted.\n")

    send_email()

def initiate_connection_db():
    print("Initiating connection to the database...")
    connection_live_db = pypyodbc.connect(driver="{SQL Server}", server="10.5.200.103", uid="user-name",
                                          pwd="try-and-guess", Trusted_Connection="No")
    connection = connection_live_db.cursor()
    return connection


def retrieve_results_query(cursor, txt_query):
    read_sql_file = open(txt_query, 'r', encoding="UTF-8", errors="replace")
    sql_file = read_sql_file.read()
    read_sql_file.close()
    cursor.execute(sql_file)
    results = cursor.fetchall()
    cursor.close()
    return results

def send_email():
    date_of_xlsx = str(datetime.now()).split(' ')[0]
    blatstring = 'cmd  /cC:\\Temp\\blat_email\\blat.exe C:\\Temp\\PythonInputFiles\\Emails\\email_mandatory_file.txt -attach C:\\Temp\\PythonOutputFiles\\Dump_' + date_of_xlsx + '.xlsx -to alejandro.bautista@dnow.com -cc alejandro.bautista@dnow.com -subject "Dump"'
    call(blatstring)
    print("Email was sent!")

if __name__ == "__main__":
    main()
