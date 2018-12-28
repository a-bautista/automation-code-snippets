#! Python 3.6.4
# Version 0.1 - Code that displays the latest changes in SyteLine related to groups,  license modules, users info and permissions. 
# Author: Alejandro Bautista R.

import sys
import os
import cx_Freeze
import openpyxl
import pypyodbc, SyteLineDump_Groups, SyteLineDump_Groups_per_Site, SyteLineDump_Module_List, SyteLineDump_Modules_per_User, SyteLineDump_UserInfoAll, SyteLineDump_Not_in_Groups
from datetime import datetime
from subprocess import call

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("SyteLineDump.py", base=base)]

cx_Freeze.setup(
    name = "Audit EY",
    options = {"build_exe":
               {"packages":
                ["openpyxl", "pypyodbc", "datetime", "subprocess", "SyteLineDump_Groups", "SyteLineDump_Groups_per_Site",
                 "SyteLineDump_Module_List", "SyteLineDump_Modules_per_User", "SyteLineDump_UserInfoAll", "SyteLineDump_Not_in_Groups"
                 ]
                
                }
               },
    version = "0.01",
    description = " Audit EY",
    executables = executables
    )
