import openpyxl
import datetime
from datetime import date, timedelta
from openpyxl import Workbook, load_workbook


class ExcelProject(object):
#########################################################################
    def __init__(self):    
        #creating global_values
        self.number = 1
        self.app_cell = 'B2'
        self.date_cell = 'F2'
        self.count = 0
        self.app_dict = {   21 : 'VAST'}

        #target sheet initialization
        self.graph_workbook = Workbook(write_only= True)
        self.graph_workbook_sheet = self.graph_workbook.create_sheet()
        print ("Default sheet name is: "+ str(self.graph_workbook_sheet))
        #source sheet initialization
        self.report_workbook = load_workbook('report1495629734867.xlsx')
        #getting the active sheet in source
        self.report_workbook_sheet = self.report_workbook.active
        print ("Work sheet name is:"+ str(self.report_workbook_sheet))

        #initialize the list and append the first row.
        self.rows =[]
        for i in range(23):
            self.rows.append([])
        
        #pushing the first row to the list
        self.rows[0].append('Row Labels')
        self.nth = 5
        while self.nth > 0:
            self.rows[0].append(date.today() - timedelta(self.nth))
            self.nth -= 1

        print(self.rows)

#######################################################################
 
    #function for getting cell values
    def cell_value(self,number):
        self.app_cell = 'B' + str(number)
        self.date_cell = 'F' + str(number)


    def access_values_dummy(self):
        if self.app_dict[21] == 'VAST':
        #for i in range(1,23):
            self.application_name = self.app_dict[21]
            self.rows[21].append(self.application_name)
            self.repeat = 5
            self.application_incident_count = 0
            while self.repeat > 0 :
                self.full_date = str(date.today() - timedelta(self.repeat))
                self.compare_date = self.full_date[:10]
                print ("date_cell renamed to: " + str(self.date_cell))
                while True:
                    #selecting the application name and counting the IRs on the particular
                    #day, and then pushing it to the list
                    
                    self.time_stamp = str(self.report_workbook_sheet[self.date_cell].value)
                    self.actual_time = self.time_stamp[:10]
                    print("actual time: " + self.actual_time)
                    if self.compare_date == self.actual_time:
                        self.application_incident_count += 1
                    self.cell_value(self.number)
                    self.number += 1
                    check_none = self.report_workbook_sheet[self.app_cell].value
                    if str(check_none) == "None":
                        self.rows[21].append(self.application_incident_count)
                        print ("self.app_name" + self.application_name + "date: " + self.compare_date + \
                               "self.application_incident_count "+ str(self.application_incident_count ))
                        break
                    
                self.repeat -= 1
                self.application_incident_count = 0
                self.date_cell = 'F2'
                self.app_cell = 'B2'
                self.number = 1
            
        
        print (self.rows)
            

######################################################################
"""    
    #get all the values from the sheet
    def access_values(self):
        self.repeat = 5
        self.application_num = 1
        count = 5
        while self.application_num < 23:
            self.application_name = str(self.report_workbook_sheet[self.app_cell].value)
            self.rows[self.application_num].append(self.application_name)
            self.full_date = str(date.today() - timedelta(self.repeat))
            self.compare_date = self.full_date[:10]
            self.application_incident_count  = 0
            while True:
                #selecting the application name and counting the IRs on the particular
                #day, and then pushing it to the list
                self.time_stamp = str(self.report_workbook_sheet[self.date_cell].value)
                self.actual_time = self.time_stamp[:10]
                if self.compare_date == self.actual_time:
                    self.application_incident_count += 1
                self.cell_value(self.number)
                self.number += 1
                check_none = self.report_workbook_sheet[self.app_cell].value
                if str(check_none) == "None" and self.count == 1 :
                    self.rows[self.application_num].append(self.application_incident_count)
                    print (self.count)
                    break
                else:
                    self.
            self.application_incident_count = 0
            self.application_num += 1
            
"""                

########################################################################
        

excel_proj = ExcelProject()
excel_proj.access_values_dummy()

