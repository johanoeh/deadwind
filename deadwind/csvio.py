from openpyxl import load_workbook
import configparser
class DAO:
    def __init__(self):
        self.headerString ="subject,Start date,Start time,End date,End time,All Day Event,Description,Location, Private";
        self.settingsFile = "deadwind.settings"
    def createCSV(self,fileName,events):
        file = open(fileName,"w")
        file.write(self.headerString+"\n")
        for event in events:
            file.write(event.toCSV()+"\n")
        file.close()
    def readWorkBook(self,resource):
        return load_workbook(resource)

    def readSettings(self):
        config = configparser.RawConfigParser()
        config.read('example.ini')
        return config['presets']

    def createSettings(self,settings):
        config = configparser.RawConfigParser()
        config['presets'] = settings;
        for  key in settings:
            config.set('presets',key,settings[key])
        with open('example.ini', 'w') as configfile:
            config.write(configfile)
