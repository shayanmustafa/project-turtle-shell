from tkinter import * 
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import ttk
import sqlite3

path = 'c:/users/shaya/turtle-shell.db'

# function to open a new window  
# on a button click
class RacerStatistics:
    
    def showForm(self):
        self.form_content.grid(column=0, row=2, sticky=(N+S, E+W), padx=20, pady=20)
        self.edit_form_content.grid_remove()
        
    def showEditForm(self):
        self.edit_form_content.grid(column=0, row=3, sticky=(N+S, E+W), padx=20, pady=20)
        self.form_content.grid_remove()
    
    def addStatsIntoDb(self):
        #Connecting to sqlite
        exists = 0
        conn = sqlite3.connect(path)
        
        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        
        selected_items = self.tv.selection()
        self.id_to_enter = []
        for selected_item in selected_items:          
            self.id_to_enter.append(self.tv.item(selected_item)['values'][0])
            
        self.first_name_to_enter = []
        for selected_item in selected_items:          
            self.first_name_to_enter.append(self.tv.item(selected_item)['values'][1])
            
        self.last_name_to_enter = []
        for selected_item in selected_items:          
            self.last_name_to_enter.append(self.tv.item(selected_item)['values'][2])
            
        self.racing_name_to_enter = []
        for selected_item in selected_items:          
            self.racing_name_to_enter.append(self.tv.item(selected_item)['values'][3])    
        
        insert_query = """ INSERT INTO racer_statistics (racer_id, first_name, last_name, racing_name, race_num, placement, num_of_racers, league, racetrack)
                            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?) """
        
        race_id = self.id_to_enter[0]
        first_name = self.first_name_to_enter[0]
        last_name = self.last_name_to_enter[0]
        racing_name = self.racing_name_to_enter[0]
        race_num = self.race_number_val.get()
        placement = self.placement_val.get()
        num_of_racers = self.num_racers_val.get()
        league = self.league_val.get()
        racetrack = self.racetrack_val.get()

        
        cursor.execute("SELECT race_num, placement, league FROM racer_statistics")
        self.rows = cursor.fetchall()
        for row in self.rows:
            if (row[0] == int(self.race_number_val.get()) and row[1] == self.placement_val.get() and row[2] == self.league_val.get()):
                messagebox.showerror(title="Error Box", message="A racer already exists in the same placement")
                exists = 1
                break
        if exists == 0:
            cursor.execute(insert_query, (race_id, first_name, last_name, racing_name, race_num, placement,
                                          num_of_racers, league, racetrack))
            conn.commit()
        
        conn.close()
        
        self.race_number.delete(0, "end")
        self.placement.delete(0, "end")
        self.num_racers.delete(0, "end")
        self.league.delete(0, "end")
        self.racetrack.delete(0, "end")
        
        self.form_content.grid_remove()
    
    def RacerStatisticsWindow(self): 
      
        # Toplevel object which will  
        # be treated as a new window 
        enterRacerStatisticsWindow = Toplevel()
        enterRacerStatisticsWindow['background']='#2A3132'
        
        style = Style()
        style.theme_use('alt')
        style.configure('W.AddButton', font =
            ('Arial CYR', 10), 
            foreground = 'white', background = '#336B87', borderwidth = '1')
        style.map('W.AddButton', background=[('active','#336B87')]) 
  
        # sets the title of the 
        # Toplevel widget 
        enterRacerStatisticsWindow.title("Enter Racer Statistics") 
        enterRacerStatisticsWindow.columnconfigure(0, weight=1)
        enterRacerStatisticsWindow.rowconfigure(0, weight=1)
        # sets the geometry of toplevel 
        enterRacerStatisticsWindow.geometry("700x500") 
  
        #content frame (first frame)
        content = ttk.Frame(enterRacerStatisticsWindow, borderwidth=6, relief='sunken')
        content.grid(column=0, row=0, sticky=(N+S, E+W), padx=20, pady=20)
        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=1)
        
        table_frame = ttk.Frame(content, borderwidth=6, relief='sunken')
        table_frame.grid(column=0, row=0, sticky=(N, S, E, W), padx=20, pady=20)
        self.tv = Treeview(table_frame, show='headings', selectmode='browse')
        self.tv['columns'] = ('Racer ID', 'First Name', 'Last Name', 'Racing Name')
        self.tv.heading('Racer ID', text='Racer ID')
        self.tv.column('Racer ID', anchor='center', width=100)
        self.tv.heading('First Name', text='First Name')
        self.tv.column('First Name', anchor='center', width=100)
        self.tv.heading('Last Name', text='Last Name')
        self.tv.column('Last Name', anchor='center', width=100)
        self.tv.heading('Racing Name', text='Racing Name')
        self.tv.column('Racing Name', anchor='center', width=100)
        
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute("SELECT racer_id, first_name, last_name, racing_name from racer")
        self.rows = cursor.fetchall()
        for row in self.rows:
            self.tv.insert("", "end", text="0", values=row)
        conn.close()
        
        self.tv.grid(sticky = (N,S,W,E))
        table_frame.treeview = self.tv
        table_frame.grid_rowconfigure(0, weight = 1)
        table_frame.grid_columnconfigure(0, weight = 1)
        
        
        
        btnFrame = ttk.Frame(enterRacerStatisticsWindow, borderwidth=6, relief='sunken')
        btnFrame.grid(column=0, row=1, sticky=(N+S), padx=20, pady=20)
        btnFrame.columnconfigure(1, weight=1)
        btnFrame.rowconfigure(1, weight=1)
        btnAddRacerStatistics = Button(btnFrame, text = "Add Statistics", style = 'W.TButton', command=self.showForm)#command=addButtonWindow.addStatisticsWindow)
        btnAddRacerStatistics.grid(row = 0, column = 0, pady = 0, padx = 10)
        
        btnEditRacerStatistics = Button(btnFrame, text = "Edit Statistics", style = 'W.TButton', command=self.showEditForm)
        btnEditRacerStatistics.grid(row = 1, column = 0, pady = 0, padx = 10)
        
        self.form_content = ttk.Frame(enterRacerStatisticsWindow, borderwidth=6, relief='sunken')
        self.form_content.columnconfigure(0, weight=1)
        self.form_content.columnconfigure(1, weight=1)
        self.form_content.columnconfigure(2, weight=1)
        self.form_content.columnconfigure(3, weight=1)
        self.form_content.rowconfigure(0, weight=2)
        self.form_content.rowconfigure(1, weight=2)
        self.form_content.rowconfigure(2, weight=2)
        self.form_content.rowconfigure(3, weight=2)
        
        # A Label widget to show in toplevel 
        Label(self.form_content, text ="Race Number").grid(row=0,column=0, sticky=(N, W, E, S), padx=15)
        self.race_number_val = StringVar()
        self.race_number = Entry(self.form_content, textvariable=self.race_number_val)
        self.race_number.grid(row=1,column=0,columnspan=1, sticky=(E+W), padx=15)

        Label(self.form_content, text ="Placement").grid(row=0,column=1, sticky=(N, W, E, S), padx=15)
        self.placement_val = StringVar()
        self.placement = Entry(self.form_content, textvariable=self.placement_val)
        self.placement.grid(row=1,column=1,columnspan=1, sticky=(E+W), padx=15)

        Label(self.form_content, text="Number of Racers").grid(row=0,column=2, sticky=(N, W, E, S), padx=15)
        self.num_racers_val = StringVar()
        self.num_racers = Entry(self.form_content, textvariable=self.num_racers_val)
        self.num_racers.grid(row=1,column=2,columnspan=1, sticky=(E+W), padx=15)

        Label(self.form_content, text="League").grid(row=0,column=3, sticky=(N, W, E, S), padx=15)
        self.league_val = StringVar()
        self.league = Entry(self.form_content, textvariable=self.league_val)
        self.league.grid(row=1,column=3,columnspan=1, sticky=(E+W), padx=15)

        Label(self.form_content, text="Racetrack").grid(row=3,column=0, sticky=(N, W, E, S), padx=15)
        self.racetrack_val = StringVar()
        self.racetrack = Entry(self.form_content, textvariable=self.racetrack_val)
        self.racetrack.grid(row=4,column=0,columnspan=1, sticky=(E+W), padx=15)
        
        btnAdd = Button(self.form_content, text = "Add", style = 'W.TButton', command=self.addStatsIntoDb)
        btnAdd.grid(row = 4, column = 1, pady = 0, padx = 50)
        
        self.edit_form_content = ttk.Frame(enterRacerStatisticsWindow, borderwidth=6, relief='sunken')
        self.edit_form_content.columnconfigure(0, weight=1)
        self.edit_form_content.columnconfigure(1, weight=1)
        self.edit_form_content.columnconfigure(2, weight=1)
        self.edit_form_content.columnconfigure(3, weight=1)
        self.edit_form_content.rowconfigure(0, weight=2)
        self.edit_form_content.rowconfigure(1, weight=2)
        self.edit_form_content.rowconfigure(2, weight=2)
        self.edit_form_content.rowconfigure(3, weight=2)
        
        # A Label widget to show in toplevel 
        Label(self.edit_form_content, text ="Race Number").grid(row=0,column=0, sticky=(N, W, E, S), padx=15)
        self.race_number_val = StringVar()
        self.race_number = Entry(self.edit_form_content, textvariable=self.race_number_val)
        self.race_number.grid(row=1,column=0,columnspan=1, sticky=(E+W), padx=15)

        Label(self.edit_form_content, text ="Placement").grid(row=0,column=1, sticky=(N, W, E, S), padx=15)
        self.placement_val = StringVar()
        self.placement = Entry(self.edit_form_content, textvariable=self.placement_val)
        self.placement.grid(row=1,column=1,columnspan=1, sticky=(E+W), padx=15)

        Label(self.edit_form_content, text="Number of Racers").grid(row=0,column=2, sticky=(N, W, E, S), padx=15)
        self.num_racers_val = StringVar()
        self.num_racers = Entry(self.edit_form_content, textvariable=self.num_racers_val)
        self.num_racers.grid(row=1,column=2,columnspan=1, sticky=(E+W), padx=15)

        Label(self.edit_form_content, text="League").grid(row=0,column=3, sticky=(N, W, E, S), padx=15)
        self.league_val = StringVar()
        self.league = Entry(self.edit_form_content, textvariable=self.league_val)
        self.league.grid(row=1,column=3,columnspan=1, sticky=(E+W), padx=15)

        Label(self.edit_form_content, text="Racetrack").grid(row=3,column=0, sticky=(N, W, E, S), padx=15)
        self.racetrack_val = StringVar()
        self.racetrack = Entry(self.edit_form_content, textvariable=self.racetrack_val)
        self.racetrack.grid(row=4,column=0,columnspan=1, sticky=(E+W), padx=15)
        
        btnAdd = Button(self.edit_form_content, text = "Edit", style = 'W.TButton')
        btnAdd.grid(row = 4, column = 1, pady = 0, padx = 50)