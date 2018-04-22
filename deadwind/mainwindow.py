from converter import ScheduleConverter
from  tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import logging
import os
from settings import SettingsController
import settings
import lang_se_sv

dir_path = os.path.dirname(os.path.realpath(__file__))
# The main graphical window
# This is the first visible window that should be opened
class MainWindow:
    def __init__(self, lang):
        self.sc = ScheduleConverter()
        self.lang = lang

        self.selectFileName=""
        self.addFileEntry = None
        self.saveFileEntry = None

        self.convertFileEvent = settings.Event()

        root = tkinter.Tk()
        menubar = Menu(root)
        menubar.add_command(label=lang['settings'], command=self.openSettings)
        menubar.add_command(label=lang['quit'], command=root.quit)
        root.config(menu=menubar)
        root.wm_title(lang['deadwind'])
        root.iconbitmap(dir_path+r'\resources\cbt.ico')

        # Add a grid
        self.mainframe = Frame(root)
        self.mainframe.grid(column = 0, row = 0, sticky=(N,W,E,S) )
        self.mainframe.columnconfigure(0, weight = 1)
        self.mainframe.rowconfigure(0, weight = 1)
        self.mainframe.pack(pady = 20, padx = 10)

        # first row of grid
        self.labelSelect = tkinter.Label(self.mainframe, text=lang['file_path'])
        self.labelSelect.grid(row=0, column=0,padx="2")
        self.addFileEntry = tkinter.Entry(self.mainframe, bg='white', relief=SUNKEN,width=40)
        self.addFileEntry.grid(row=0,column=1, padx=2)
        self.selectBTN = tkinter.Button(self.mainframe, text = lang['browse'], command = self.selectFile, width=20)
        self.selectBTN.grid(row=0, column=2, padx=2)
        self.saveBTN = tkinter.Button(self.mainframe, text=lang['convert'],command = self.saveFile, width=20)
        self.saveBTN.grid(row=0, column=3 , padx=2)
        self.listBox = tkinter.Listbox(self.mainframe, bg='black',  fg='white')
        self.listBox.grid(row=1, columnspan=4, sticky=W+E+N+S)
        root.mainloop()

    def setText(self, text, entry):
        entry.delete(0,END)
        entry.insert(0,text)

    def openSettings(self):
        SettingsController()


    def selectFile(self):
        self.selectFileName = (
        filedialog.askopenfilename(initialdir = dir_path,title = self.lang['select_file_t'],filetypes = (("csv  files xlsx","*.xlsx"),("all files","*.*"))))
        self.setText(self.selectFileName,self.addFileEntry)

    def saveFile(self):
        self.selectFileName = self.addFileEntry.get();
        if self.selectFileName == "" or self.selectFileName == None :
            tkinter.messagebox.showinfo(self.lang['no_file_selected_h'],self.lang['no_file_selected_m'])
            return
        self.saveFileName = filedialog.asksaveasfilename(initialdir = dir_path,title = self.lang['select_file_t'],filetypes = (("csv files","*.csv"),("all files","*.*")))
        if self.saveFileName == None or self.saveFileName =="":
            return
        self.listBox.delete(0,tkinter.END)
        try:
            events = ScheduleConverter().convert(self.selectFileName, self.saveFileName)
            self.setText(self.lang['conversion_success'], self.addFileEntry)
            for event in events:
                self.listBox.insert(END, event.toList())
        except FileNotFoundError as e:
            var = tkinter.messagebox.showinfo(self.lang['file_not_found_h'],"\""+ self.selectFileName+" \" "+self.lang['file_not_found_message'])
        except Exception as e:
            logging.exception("Something went wrong while parsing the file")

MainWindow(lang_se_sv.lang_main)
