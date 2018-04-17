from .converter import ScheduleConverter
from  tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import logging
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
class MainWindow:
    def __init__(self):
        self.selectBTNText = "Bläddra"
        self.saveBTNText = "konvertera"
        self.sc = ScheduleConverter()

        self.selectFileName=""
        self.addFileEntry = None
        self.saveFileEntry = None

        root = tkinter.Tk()
        root.wm_title("Motvind")
        print(dir_path)
        root.iconbitmap(dir_path+r'\resources\cbt.ico')

        # Add a grid
        self.mainframe = Frame(root)
        self.mainframe.grid(column = 0, row = 0, sticky=(N,W,E,S) )
        self.mainframe.columnconfigure(0, weight = 1)
        self.mainframe.rowconfigure(0, weight = 1)
        self.mainframe.pack(pady = 20, padx = 10)

        # first row of grid
        self.labelSelect = tkinter.Label(self.mainframe, text="Filsökväg:")
        self.labelSelect.grid(row=0, column=0,padx="2")
        self.addFileEntry = tkinter.Entry(self.mainframe, bg='white', relief=SUNKEN,width=40)
        self.addFileEntry.grid(row=0,column=1, padx=2)
        self.selectBTN = tkinter.Button(self.mainframe, text =self.selectBTNText, command = self.selectFile, width=20)
        self.selectBTN.grid(row=0, column=2, padx=2)
        self.saveBTN = tkinter.Button(self.mainframe, text=self.saveBTNText,command = self.saveFile, width=20)
        self.saveBTN.grid(row=0, column=3 , padx=2)
        self.listBox = tkinter.Listbox(self.mainframe, bg='black',  fg='white')
        self.listBox.grid(row=1, columnspan=4, sticky=W+E+N+S)

        root.mainloop()

    def setText(self, text, entry):
        entry.delete(0,END)
        entry.insert(0,text)

    def selectFile(self):
        self.selectFileName = (
        filedialog.askopenfilename(initialdir = dir_path,title = "Select file",filetypes = (("csv  files xlsx","*.xlsx"),("all files","*.*"))))
        self.setText(self.selectFileName,self.addFileEntry)

    def saveFile(self):
        self.selectFileName = self.addFileEntry.get();
        self.saveFileName = filedialog.asksaveasfilename(initialdir = dir_path,title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        try:
            events = self.sc.convert(self.selectFileName, self.saveFileName)
            self.setText("konverteringen klar!", self.addFileEntry)
            for event in events:
                self.listBox.insert(END, event.toCSV())
        except FileNotFoundError as e:
            var = tkinter.messagebox.showinfo("Filen kunde inte hittas"," Fel filen med sökväg \' "+self.selectFileName+"  \' kunde inte hittas!")
        except Exception as e:
            loggin.exception("Something went wrong while parsing the file")
