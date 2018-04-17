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
        root.wm_title("Motvind")
        self.mainframe = tkinter.Frame(root)
        self.mainframe.grid(column = 0, row = 0, sticky=(tkinter.N,tkinter.W,tkinter.E,tkinter.S) )
        self.mainframe.columnconfigure(0, weight = 1)
        self.mainframe.rowconfigure(0, weight = 1)
        self.mainframe.pack(pady = 20, padx = 10)

        ## first row of grid
        ########################################################################
        #Label for subject
        self.labelSubject = tkinter.Label(
                                           self.mainframe,
                                           text=lang['subject'],
                                           width=40
                                         )
        self.labelSubject.grid(row=0, column=0, padx="2")
        # Entry for subject (textinput for a subjectname)
        self.subjectEntry = tkinter.Entry(
                                          self.mainframe,
                                          bg="white",
                                          relief=tkinter.SUNKEN,
                                          width=40,
                                         )
        self.subjectEntry.grid(
                                row = 0, column = 1,
                                padx=2,
                                sticky=(tkinter.N,tkinter.W,tkinter.E,tkinter.S)
                            );

        ## Second row of grid
        ########################################################################
        #Label for description
        self.labelDescription = tkinter.Label(
                                           self.mainframe,
                                           text = lang['description'],
                                           width = 40
                                         )
        self.labelDescription.grid(row=1, column=0, padx="2")

        #Textfield for a description text
        self.descText = tkinter.Text(
                                        self.mainframe,
                                        height = "4",
                                        width = 40
                                    )
        self.descText.grid(row=1,column=1,padx=2)

        ## Third row of grid
        ########################################################################
        #Label for location
        self.labelLocation = tkinter.Label(
                                           self.mainframe,
                                           text = lang['location']
                                          )
        self.labelLocation.grid(row=2, column=0, padx="2")

        #Textfield for location text
        self.locationText = tkinter.Text(self.mainframe, height="4", width=40)
        self.locationText.grid(row=2,column=1,padx=2)

        ## Fourth row of grid
        ########################################################################
        # button to save userinputs
        self.saveBTN = tkinter.Button(
                                       self.mainframe,
                                       text = lang['save'],
                                       command = self.save,
                                       width = 20
                                     )
        self.saveBTN.grid(row=3, column=0, padx=5)

        # button to clear userinputs
        self.clearBTN = tkinter.Button(
                                        self.mainframe,
                                        text = lang['clear'],
                                        command = self.clear,
                                        width = 20
                                    )
        self.clearBTN.grid(row=3, column=1, padx=5)
        root.mainloop()

    def addLabel(text,ro,col):
        label = tkinter.Label(
                       self.mainframe,
                       text=lang['subject'],
                       width=40
                     )
        self.labelSubject.grid(row=ro, column=col, padx="2")
        return label

    def addEntry(ro, col):
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

    def save(self):
        print(
                self.subjectEntry.get(),
                self.descText.get("1.0",tkinter.END),
                self.locationText.get("1.0",tkinter.END)
            )

    def clear(self):
        print("clear")

settingsView = settings_view(lang)
