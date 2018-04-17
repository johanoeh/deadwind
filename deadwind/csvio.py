from openpyxl import load_workbook
class DAO:
    def __init__(self):
        self.headerString ="subject,Start date,Start time,End date,End time,All Day Event,Description,Location, Private";
    def createCSV(self,fileName,events):
        file = open(fileName,"w")
        file.write(self.headerString+"\n")
        for event in events:
            file.write(event.toCSV()+"\n")
        file.close()
    def readWorkBook(self,resource):
        return load_workbook(resource)
