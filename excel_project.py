import openpyxl
from openpyxl import load_workbook, Workbook
from openpyxl.chart import BarChart, Series, Reference
import datetime
from datetime import date, timedelta



class ExcelProject(object):
#########################################################################
    def __init__(self):    
        #creating global_values
        self.number = 2
        self.app_cell = 'B2'
        self.date_cell = 'F2'
        self.count = 0
        self.app_dict = {   1 : 'BIS',
                            2 : 'BPMS',
                            3 : 'Business Data Solutions - MDB',
                            4 : 'Client Portal' ,
                            5 : 'Client Portal Mobile - B2B',
                            6 : 'Content Assistant' ,
                            7 : 'DexBis' ,
                            8 : 'Dexnet' ,
                            9 : 'Distribution' ,
                            10 : 'DSS Request' ,
                            11 : 'Enterprise Apps - kGen' ,
                            12 : 'Enterprise Service Bus' ,
                            13 : 'Intranet' ,
                            14 : 'LSAP & PRP' ,
                            15 : 'Merchant Platform' ,
                            16 : 'NEMO' ,
                            17 : 'Proposal Builder' ,
                            18 : 'Salesforce Platform' ,
                            19 : 'SEM Estimator Tool' ,
                            20 : 'Superpages.com' ,
                            22 : 'Vision',
                            23 : 'Wireless',
                            21 : 'VAST'
                        }

        #target sheet initialization
        self.graph_workbook = Workbook(write_only= True)
        self.graph_workbook_sheet = self.graph_workbook.create_sheet()
        print ("Default sheet name is: "+ str(self.graph_workbook_sheet))
        #source sheet initialization
        self.report_workbook = load_workbook('Book77.xlsx')
        #getting the active sheet in source
        self.report_workbook_sheet = self.report_workbook.active
        print ("Work sheet name is:"+ str(self.report_workbook_sheet))

        #initialize the list and append the first row.
        self.rows =[]
        for i in range(24):
            self.rows.append([])
        
        #pushing the first row to the list
        self.rows[0].append('Row Labels')
        self.nth = 7
        while self.nth > 0:
            self.rows[0].append(date.today() - timedelta(self.nth))
            self.nth -= 1

        

#######################################################################
 
    #function for getting cell values
    def cell_value(self,number):
        self.app_cell = 'B' + str(self.number)
        self.date_cell = 'F' + str(self.number)


    def access_values_dummy(self):
        for i in range(1,24):
            self.application_name = self.app_dict[i]
            #print ("checking for application: "+ self.application_name)
            self.rows[i].append(self.application_name)
            self.repeat = 7
            self.application_incident_count = 0
            print ("Starting Application: " + self.application_name)
            while self.repeat > 0 :
                #print ("self.repeat value is:" + str(self.repeat))
                self.full_date = str(date.today() - timedelta(self.repeat))
                self.compare_date = self.full_date[:10]
                #print ("self.compare_date becomes: "+ self.compare_date)
                #print ("date_cell renamed to: " + str(self.date_cell))
                while True:
                    #selecting the application name and counting the IRs on the particular
                    #day, and then pushing it to the list
                    
                    self.time_stamp = str(self.report_workbook_sheet[self.date_cell].value)
                    self.actual_time = self.time_stamp[:10]
                    #print("actual time: " + self.actual_time)
                    if self.compare_date == self.actual_time and self.application_name == str(self.report_workbook_sheet[self.app_cell].value):
                        self.application_incident_count += 1
                    self.number += 1
                    self.cell_value(self.number)
                    #print (self.app_cell)
                    #print (self.date_cell)
                    check_none = self.report_workbook_sheet[self.app_cell].value
                    #print ("check_none: "+ str(check_none))
                    if str(check_none) == "None":
                        self.rows[i].append(self.application_incident_count)
                        #print ("self.app_name" + self.application_name + "date: " + self.compare_date + \
                               #"self.application_incident_count "+ str(self.application_incident_count ))
                        break
                    
                self.repeat -= 1
                self.application_incident_count = 0
                self.date_cell = 'F2'
                self.app_cell = 'B2'
                self.number = 2
            print ("Application Done: " + self.application_name)
            print ()
            print ()
                
        
        print (self.rows)
            

######################################################################

    def append_values_to_sheet(self):
        for row_values in self.rows:
            self.graph_workbook_sheet.append(row_values)
        print ("Alvalues got appended to sheet")

########################################################################


    def draw_graph(self):
        chart = BarChart()
        chart.type = "col"
        chart.title = "IR Inflow - Last 7 Days - Top 10 Apps"
        chart.style = 10
        chart.x_axis.title = 'Applications'
        chart.y_axis.title = 'Inflow_Value'
        data = Reference(self.graph_workbook_sheet, min_col=2, min_row=1, max_row= 6, max_col=8)
        cats = Reference(self.graph_workbook_sheet, min_col=1, min_row=2, max_row=6)
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(cats)
        chart.shape = 6
        self.graph_workbook_sheet.add_chart(chart, "K2")    
        self.graph_workbook.save('final_graph.xlsx')
        print ("######SUCCESSFUL......GRAPH IS READY######")

#####################################################################        

excel_proj = ExcelProject()
excel_proj.access_values_dummy()
excel_proj.append_values_to_sheet()
excel_proj.draw_graph()

