import events
import tkinter

#TextFields subject, description and location
lang = {
          "settings" : "Inställningar",
          "save" : "Spara",
          "clear" : "rensa",
          "subject" : "Ämne",
          "description" : "beskrivning",
          "location" : "plats"
        }
class settings_view:
    def __init__(self,lang):

        root = tkinter.Tk()
        root.wm_title("Inställningar")
        self.mainframe = tkinter.Frame(root)
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


        root.mainloop()

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
        print(
                self.subjectEntry.get(),
                self.descText.get("1.0",tkinter.END),
                self.locationText.get("1.0",tkinter.END)
            )

    def clear(self):
        print("clear")

settingsView = settings_view(lang)
