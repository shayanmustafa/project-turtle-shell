from tkinter import * 
from tkinter.ttk import *
from tkinter import ttk
import sqlite3

#path = 'c:/users/shaya/turtle-shell.db'
path = 'd:/project-turtle-shell/store.db'

class AddRacerStatistics:
    def addStatisticsWindow(self):
        addStatisticsButtonWindow = Toplevel()
        addStatisticsButtonWindow['background']='#2A3132'
        
        style = Style()
        style.theme_use('alt')
        style.configure('W.AddButton', font =
            ('Arial CYR', 10), 
            foreground = 'white', background = '#336B87', borderwidth = '1')
        style.map('W.AddButton', background=[('active','#336B87')]) 
  
        # sets the title of the 
        # Toplevel widget 
        addStatisticsButtonWindow.title("Add Statistics") 
        addStatisticsButtonWindow.columnconfigure(0, weight=1)
        addStatisticsButtonWindow.rowconfigure(0, weight=1)
        # sets the geometry of toplevel 
        addStatisticsButtonWindow.geometry("700x300")
        
        #content frame (first frame)
        content = ttk.Frame(addStatisticsButtonWindow, borderwidth=6, relief='sunken')
        content.grid(column=0, row=0, sticky=(N+S, E+W), padx=20, pady=20)
        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=1)

        form_content = ttk.Frame(content)
        form_content.grid(column=0, row=0, sticky=(N, E+W), padx=20, pady=20)
        form_content.columnconfigure(0, weight=1)
        form_content.columnconfigure(1, weight=1)
        form_content.columnconfigure(2, weight=1)
        form_content.columnconfigure(3, weight=1)
        form_content.rowconfigure(0, weight=2)
        form_content.rowconfigure(1, weight=2)
        form_content.rowconfigure(2, weight=2)
        form_content.rowconfigure(3, weight=2)
    
        # A Label widget to show in toplevel 
        Label(form_content, text ="Race Number").grid(row=0,column=0, sticky=(N, W, E, S), padx=15)
        self.race_number_val = StringVar()
        self.race_number = Entry(form_content, textvariable=self.race_number_val)
        self.race_number.grid(row=1,column=0,columnspan=1, sticky=(E+W), padx=15)

        Label(form_content, text ="Placement").grid(row=0,column=1, sticky=(N, W, E, S), padx=15)
        self.placement_val = StringVar()
        self.placement = Entry(form_content, textvariable=self.placement_val)
        self.placement.grid(row=1,column=1,columnspan=1, sticky=(E+W), padx=15)

        Label(form_content, text="Number of Racers").grid(row=0,column=2, sticky=(N, W, E, S), padx=15)
        self.num_racers_val = StringVar()
        self.num_racers = Entry(form_content, textvariable=self.num_racers_val)
        self.num_racers.grid(row=1,column=2,columnspan=1, sticky=(E+W), padx=15)

        Label(form_content, text="League").grid(row=0,column=3, sticky=(N, W, E, S), padx=15)
        self.league_val = StringVar()
        self.league = Entry(form_content, textvariable=self.league_val)
        self.league.grid(row=1,column=3,columnspan=1, sticky=(E+W), padx=15)

        Label(form_content, text="Racetrack").grid(row=3,column=0, sticky=(N, W, E, S), padx=15)
        self.racetrack_val = StringVar()
        self.racetrack = Entry(form_content, textvariable=self.racetrack_val)
        self.racetrack.grid(row=4,column=0,columnspan=1, sticky=(E+W), padx=15)
        
        btnAdd = Button(content, text = "Add", style = 'W.TButton')
        btnAdd.grid(row = 2, column = 0, pady = 0, padx = 50)