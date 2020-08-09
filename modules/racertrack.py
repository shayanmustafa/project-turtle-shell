from tkinter import * 
from tkinter.ttk import *
from tkinter import ttk
import sqlite3

path = 'c:/users/shaya/turtle-shell.db'
# function to open a new window  
# on a button click 

class RaceTrack:
    
    def addRaceTrackIntoDb(self):
        #Connecting to sqlite
        conn = sqlite3.connect(path)
        
        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        insert_query = """ INSERT INTO racetrack (racetrack_name, lap, racetrack_cup)
                            VALUES(?, ?, ?) """
                            
        racetrack_name = self.racetrack_name_val.get()
        lap = self.lap_val.get()
        racetrack_cup = self.racetrack_cup_val.get()
        
        self.racetrack_name.delete(0, "end")
        self.lap.delete(0, "end")
        self.racetrack_cup.delete(0, "end")
        
        cursor.execute(insert_query, (racetrack_name, lap, racetrack_cup))
        last_row_id = cursor.lastrowid
        conn.commit()
        
        cursor.execute("SELECT racetrack_name, lap, racetrack_cup FROM racetrack WHERE racetrack_id = " + str(last_row_id))
        self.rows = cursor.fetchall()
        for row in self.rows:
            self.tv.insert("", "end", text="0", values=row)
        conn.close()

    def raceTrackWindow(self): 
      
        # Toplevel object which will  
        # be treated as a new window 
        racetrackWindow = Toplevel()
        racetrackWindow['background']='#2A3132'

        style = Style()
        style.theme_use('alt')
        style.configure('W.AddButton', font =
            ('Arial CYR', 10), 
            foreground = 'white', background = '#336B87', borderwidth = '1')
        style.map('W.AddButton', background=[('active','#336B87')]) 
  
        # sets the title of the 
        # Toplevel widget 
        racetrackWindow.title("Enter Racetrack Information") 
        racetrackWindow.columnconfigure(0, weight=1)
        racetrackWindow.rowconfigure(0, weight=1)
        # sets the geometry of toplevel 
        racetrackWindow.geometry("700x500") 
        
        #content frame (first frame)
        content = ttk.Frame(racetrackWindow, borderwidth=6, relief='sunken')
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
        Label(form_content, text ="Racetrack Name").grid(row=0,column=0, sticky=(N, W, E, S), padx=15)
        self.racetrack_name_val = StringVar()
        self.racetrack_name = Entry(form_content, textvariable=self.racetrack_name_val)
        self.racetrack_name.grid(row=1,column=0,columnspan=1, sticky=(E+W), padx=15)

        Label(form_content, text ="Laps").grid(row=0,column=1, sticky=(N, W, E, S), padx=15)
        self.lap_val = StringVar()
        self.lap = Entry(form_content, textvariable=self.lap_val)
        self.lap.grid(row=1,column=1,columnspan=1, sticky=(E+W), padx=15)

        Label(form_content, text="Racetrack Cup").grid(row=0,column=2, sticky=(N, W, E, S), padx=15)
        self.racetrack_cup_val = StringVar()
        self.racetrack_cup = Entry(form_content, textvariable=self.racetrack_cup_val)
        self.racetrack_cup.grid(row=1,column=2,columnspan=1, sticky=(E+W), padx=15)
        
        # add racer
        btnAdd = Button(form_content, text = "Add", command=self.addRaceTrackIntoDb)
        btnAdd.grid(row = 5, column = 0, pady = 20, padx = 20, sticky=(E+W))
        
        # delete racer row
        btnAdd = Button(form_content, text = "Delete")
        btnAdd.grid(row = 5, column = 1, pady = 20, padx = 20, sticky=(E+W))
        
        table_frame = ttk.Frame(content, borderwidth=6, relief='sunken')
        table_frame.grid(column=0, row=1, sticky=(N+S, E+W), padx=20, pady=20)
        self.tv = Treeview(table_frame, show='headings', selectmode='browse')
        self.tv['columns'] = ('Racetrack Name', 'Laps', 'Racetrack Cup')
        self.tv.heading('Racetrack Name', text='Racetrack Name')
        self.tv.column('Racetrack Name', anchor='center', width=100)
        self.tv.heading('Laps', text='Laps')
        self.tv.column('Laps', anchor='center', width=100)
        self.tv.heading('Racetrack Cup', text='Racetrack Cup')
        self.tv.column('Racetrack Cup', anchor='center', width=100)
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute("SELECT racetrack_name, lap, racetrack_cup FROM racetrack")
        self.rows = cursor.fetchall()
        for row in self.rows:
            self.tv.insert("", "end", text="0", values=row)
        conn.close()
        self.tv.grid(sticky = (N,S,W,E))
        table_frame.treeview = self.tv
        table_frame.grid_rowconfigure(0, weight = 1)
        table_frame.grid_columnconfigure(0, weight = 1)