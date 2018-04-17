#
from openpyxl import load_workbook
from .csvio import DAO as DAO
from .events import *
from .xparser import TimeParser as TP

#
# Converts medvinds format to a csv format suited for google calendat
#
class ScheduleConverter :
    def __init__(self):
        self.sheetName = "Medvind"
        self.dao = DAO()
        self.events = []
        self.tp = TP(Event(
                        "Arbete",
                         None,
                         None,
                         None,
                         None,
                         False,
                         "107",
                         "Nya hamngatan 13",
                         False
                         ))
    def  convert(self,input,output) :
        wb = self.dao.readWorkBook(input)
        sheet = wb[self.sheetName]
        for cellObj in sheet['B3':'H7']:
            for cell in cellObj:
                    self.tp.parse(cell.value, self.events)
        self.dao.createCSV(output, self.events)
        return self.events
