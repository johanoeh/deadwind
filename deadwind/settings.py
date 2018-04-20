import events
import tkinter
from csvio import DAO

#TextFields subject, description and location
lang = {
          "settings" : "Inställningar",
          "save" : "Spara",
          "clear" : "rensa",
          "subject" : "Ämne",
          "description" : "beskrivning",
          "location" : "plats"
        }

class SettingsView:
    def __init__(self,lang,settings):
        self.settings = settings
        self.saveBTNClick = Event()
        self.root = tkinter.Toplevel()
        self.root.wm_title(lang['settings'])

        self.mainframe = tkinter.Frame(self.root)
        self.mainframe.grid(column = 0, row = 0, sticky=(tkinter.N,tkinter.W,tkinter.E,tkinter.S) )
        self.mainframe.columnconfigure(0, weight = 1)
        self.mainframe.rowconfigure(0, weight = 1)
        self.mainframe.pack(pady = 20, padx = 10)

        ## first row of grid
        ########################################################################
        #Label for subject
        self.labelSubject = self.addLabel(lang['subject'],0,0)
        # Entry for subject (textinput for a subjectname)
        self.subjectEntry = self.addEntry(0,1)

        ## Second row of grid
        ########################################################################
        #Label for description
        self.labelDescription = self.addLabel(lang['description'], 1, 0)

        #Textfield for a description text
        self.descText = self.addText(1,1)

        ## Third row of grid
        ########################################################################
        #Label for location
        self.labelLocation = self.addLabel(lang['location'],2,0)
        #Textfield for location text
        self.locationText = self.addText(2,1)

        ## Fourth row of grid
        ########################################################################
        # A wrappert for the buttons
        self.btnWrapper = tkinter.Frame(self.mainframe)
        self.btnWrapper.grid(row=3, column=1, pady=15)

        # button to save userinputs
        self.saveBTN = tkinter.Button(
                                       self.btnWrapper,
                                       text = lang['save'],
                                       command = self.save,
                                       width = 20
                                     )
        self.saveBTN.grid(row=0, column=0, padx=5)

        # button to clear userinputs
        self.clearBTN = tkinter.Button(
                                        self.btnWrapper,
                                        text = lang['clear'],
                                        command = self.clear,
                                        width = 20
                                    )
        self.clearBTN.grid(row=0, column=1, padx=5)

        self.setTextFields()

    def addText(self,ro,col):
        text = tkinter.Text( self.mainframe, height = "4", width = 40 )
        text.grid(row = ro, column=col, padx=2)
        return text

    #Adds label to view
    def addLabel(self, tex, ro, col):
        label = tkinter.Label(
                       self.mainframe,
                       text=tex,
                       width=20
                     )
        label.grid(row=ro, column=col, padx="2")
        return label

    ## Adds entry to view
    def addEntry(self, ro, col):
        entry = tkinter.Entry(
                              self.mainframe,
                              bg="white",
                              relief=tkinter.SUNKEN,
                              width=40,
                             )
        entry.grid(
                    row = ro, column = col,
                    padx=2,
                    sticky=(tkinter.N,tkinter.W,tkinter.E,tkinter.S)
                  )
        return entry

    def save(self):
        subject = self.subjectEntry.get()
        description = self.descText.get("1.0",tkinter.END)
        location = self.locationText.get("1.0",tkinter.END)
        self.saveBTNClick.notify({'subject':subject, 'description':description, 'location':location})

    def setTextFields(self):
        self.setEntry(self.settings['subject'], self.subjectEntry)
        self.setText(self.settings['description'], self.descText)
        self.setText(self.settings['location'], self.locationText)


    def clear(self):
        self.subjectEntry.delete(0,tkinter.END)
        self.descText.delete("1.0",tkinter.END)
        self.locationText.delete("1.0",tkinter.END)

    def setEntry(self, text, entry):
        entry.delete(0,tkinter.END)
        entry.insert(0,text)

    def setText(self,value,text):
        text.delete("1.0",tkinter.END)
        text.insert("1.0",value)


class Event:
    def __init__(self):
        self.listeners = []
    def notify(self, msg):
        for callBack in self.listeners :
            callBack(msg)
    def addListener(self, callBack):
        self.listeners.append(callBack)

class SettingsController:

    def __init__(self):
        self.dao = DAO()
        self.settingsView = SettingsView(lang, self.dao.readSettings())
        self.settingsView.root.grab_set()
        self.settingsView.saveBTNClick.addListener(self.saveSettings)

    def saveSettings(self,settings):
        settings['isAllDayEvent'] = 'False'
        settings['isPrivate'] = 'False'
        self.dao.createSettings(settings)
