'''
    Main class
    Main function is the starting point to execute Advocate tool.
    Main Function accepts parameters passed from UnitTest project. These parameters are passed to SourceConnection class

'''

import sys
from Read_Hive_table import *
from Read_Table import *
from validator import *
from config import *
from Read_Hive_table_Source import *
from SourceConnection import *
import os

def main():          
    arglist = str(sys.argv[1]) 
           
    testcaselist = arglist.split(",") 
    PlanId = str(testcaselist[0])
    TestCaseId = str(testcaselist[1])
    RunId = str(testcaselist[2])
    #ResultId = str(testcaselist[4])
    os.chdir(testcaselist[3]) 
    DirPath = os.getcwd()
    
    if not os.path.exists("C:\\advocate_logs"):
        os.makedirs("C:\\advocate_logs")

    file_name="file_" + TestCaseId+ ".txt"
    file_path = "C:\\advocate_logs\\" + file_name

    file = open(file_path,'a',encoding='utf-8')
    file.write("\n" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")) + ":: Main Execution started for Test Plan " + PlanId + "and Test Case " + TestCaseId + " and Test Run " + RunId + ".\n")
    file.close()         
                
    resdict = rest_requests.read_config_file('self',TestCaseId,DirPath,file_path)
    #with open(file_path, "a") as logfile:
    #    logfile.write("\n Case Execution Called.\n")
    #    logfile.close() 
    SourceConnection.execute('self',PlanId,TestCaseId,DirPath,RunId,file_path,resdict)
    
    with open(file_path, "a") as logfile:
        logfile.write("\n" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")) + ":: Main Execution ended for Test Plan " + PlanId + "and Test Case " + TestCaseId + " and Test Run " + RunId + ".\n")
        logfile.close()
            
if __name__ == "__main__":
    main()




