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
        #self.edit_form_content.grid_remove()
        selected_items = []
        selected_items = self.tv.selection()
        if not selected_items:
            messagebox.showinfo(title="Select Racer", message="Please first select one of the racers from the list to add statistics.")
            self.form_content.grid_remove()
            
    def showEditForm(self):
        #Edit Form 
        
        selected_rows = []
        selected_rows = self.tv_stats.selection()
        if not selected_rows:
            messagebox.showinfo(title="Select Editable Row", message="Please first select one of the rows from the list to edit statistics.")
        else:
            items_race_num = []     
            for selected_row in selected_rows:          
                items_race_num.append(self.tv_stats.item(selected_row)['values'][4])
            
            items_num_racers = []
            for selected_row in selected_rows:          
                items_num_racers.append(self.tv_stats.item(selected_row)['values'][6])
                
            items_league = []
            for selected_row in selected_rows:          
                items_league.append(self.tv_stats.item(selected_row)['values'][7])
                
            items_racetrack = []
            for selected_row in selected_rows:          
                items_racetrack.append(self.tv_stats.item(selected_row)['values'][8])
                
            race_num_entry = items_race_num[0]
            num_racers_entry = items_num_racers[0]
            league_entry = items_league[0]
            racetrack_entry = items_racetrack[0]
        
        self.edit_form_content = ttk.Frame(self.enterRacerStatisticsWindow, borderwidth=6, relief='sunken')
        self.edit_form_content.grid(column=0, row=3, sticky=(N+S, E+W), padx=20, pady=20)
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
        self.edit_race_number_val = StringVar()
        self.edit_race_number = Entry(self.edit_form_content, textvariable=self.edit_race_number_val)
        self.edit_race_number_val.set(race_num_entry)
        self.edit_race_number.grid(row=1,column=0,columnspan=1, sticky=(E+W), padx=15)

        Label(self.edit_form_content, text ="Placement").grid(row=0,column=1, sticky=(N, W, E, S), padx=15)
        self.edit_placement_val = StringVar()
        self.edit_placement = Entry(self.edit_form_content, textvariable=self.edit_placement_val)
        self.edit_placement.grid(row=1,column=1,columnspan=1, sticky=(E+W), padx=15)

        Label(self.edit_form_content, text="Number of Racers").grid(row=0,column=2, sticky=(N, W, E, S), padx=15)
        self.edit_num_racers_val = StringVar()
        self.edit_num_racers = Entry(self.edit_form_content, textvariable=self.edit_num_racers_val)
        self.edit_num_racers_val.set(num_racers_entry)
        self.edit_num_racers.grid(row=1,column=2,columnspan=1, sticky=(E+W), padx=15)

        Label(self.edit_form_content, text="League").grid(row=0,column=3, sticky=(N, W, E, S), padx=15)
        self.edit_league_val = StringVar()
        self.edit_league = Entry(self.edit_form_content, textvariable=self.edit_league_val)
        self.edit_league_val.set(league_entry)
        self.edit_league.grid(row=1,column=3,columnspan=1, sticky=(E+W), padx=15)

        Label(self.edit_form_content, text="Racetrack").grid(row=3,column=0, sticky=(N, W, E, S), padx=15)
        self.edit_racetrack_val = StringVar()
        self.edit_racetrack = Entry(self.edit_form_content, textvariable=self.edit_racetrack_val)
        self.edit_racetrack_val.set(racetrack_entry)
        self.edit_racetrack.grid(row=4,column=0,columnspan=1, sticky=(E+W), padx=15)
        
        btnEdit = Button(self.edit_form_content, text = "Edit", style = 'W.TButton')
        btnEdit.grid(row = 4, column = 1, pady = 0, padx = 50)
        
    def showEditableRows(self):
        #self.edit_form_content.grid(column=0, row=3, sticky=(N+S, E+W), padx=20, pady=20)
        
        self.form_content.grid_remove()
        
        
        selected_items = []
        selected_items = self.tv.selection()
        
        if not selected_items:
            messagebox.showinfo(title="Select Racer", message="Please first select one of the racers from the list to edit statistics.")
        else:
            self.btnFrame.grid_remove()
            stats_table_frame = ttk.Frame(self.content, borderwidth=6, relief='sunken')
            stats_table_frame.grid(column=0, row=0, sticky=(N, S, E, W), padx=20, pady=20)
            self.tv_stats = Treeview(stats_table_frame, show='headings', selectmode='browse')
            self.tv_stats['columns'] = ('Racer ID', 'First Name', 'Last Name', 'Racing Name', 'Race Number', 'Placement', 'Number of Racers', 'League', 'Racetrack')
            self.tv_stats.heading('Racer ID', text='Racer ID')
            self.tv_stats.column('Racer ID', anchor='center', width=100)
            self.tv_stats.heading('First Name', text='First Name')
            self.tv_stats.column('First Name', anchor='center', width=100)
            self.tv_stats.heading('Last Name', text='Last Name')
            self.tv_stats.column('Last Name', anchor='center', width=100)
            self.tv_stats.heading('Racing Name', text='Racing Name')
            self.tv_stats.column('Racing Name', anchor='center', width=100)
            self.tv_stats.heading('Race Number', text='Race Number')
            self.tv_stats.column('Race Number', anchor='center', width=100)
            self.tv_stats.heading('Placement', text='Placement')
            self.tv_stats.column('Placement', anchor='center', width=100)
            self.tv_stats.heading('Number of Racers', text='Number of Racers')
            self.tv_stats.column('Number of Racers', anchor='center', width=100)
            self.tv_stats.heading('League', text='League')
            self.tv_stats.column('League', anchor='center', width=100)
            self.tv_stats.heading('Racetrack', text='Racetrack')
            self.tv_stats.column('Racetrack', anchor='center', width=100)
        
            items_to_search = []     
            for selected_item in selected_items:          
                items_to_search.append(self.tv.item(selected_item)['values'][3])
                tuple(items_to_search)
        
            conn = sqlite3.connect(path)
            cursor = conn.cursor()
            select_query = 'SELECT racer_id, first_name, last_name, racing_name, race_num, placement, num_of_racers, league, racetrack from racer_statistics where racing_name=?'
            cursor.execute(select_query, (items_to_search))
            self.rows_stats = cursor.fetchall()
            for row in self.rows_stats:
                self.tv_stats.insert("", "end", text="0", values=row)
            conn.close()
        
            self.tv_stats.grid(sticky = (N,S,W,E))
            stats_table_frame.treeview = self.tv_stats
            stats_table_frame.grid_rowconfigure(0, weight = 1)
            stats_table_frame.grid_columnconfigure(0, weight = 1)
            
            btnSelectedEdit = Button(self.content, text = "Edit Selected Row", style = 'W.TButton', command=self.showEditForm)
            btnSelectedEdit.grid(row = 4, column = 0, pady = 0, padx = 50)   
    
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
        self.enterRacerStatisticsWindow = Toplevel()
        self.enterRacerStatisticsWindow['background']='#2A3132'
        
        style = Style()
        style.theme_use('alt')
        style.configure('W.AddButton', font =
            ('Arial CYR', 10), 
            foreground = 'white', background = '#336B87', borderwidth = '1')
        style.map('W.AddButton', background=[('active','#336B87')]) 
  
        # sets the title of the 
        # Toplevel widget 
        self.enterRacerStatisticsWindow.title("Enter Racer Statistics") 
        self.enterRacerStatisticsWindow.columnconfigure(0, weight=1)
        self.enterRacerStatisticsWindow.rowconfigure(0, weight=1)
        # sets the geometry of toplevel 
        self.enterRacerStatisticsWindow.geometry("700x500") 
  
        #content frame (first frame)
        self.content = ttk.Frame(self.enterRacerStatisticsWindow, borderwidth=6, relief='sunken')
        self.content.grid(column=0, row=0, sticky=(N+S, E+W), padx=20, pady=20)
        self.content.columnconfigure(0, weight=1)
        self.content.rowconfigure(0, weight=1)
        
        table_frame = ttk.Frame(self.content, borderwidth=6, relief='sunken')
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
        
        
        
        self.btnFrame = ttk.Frame(self.enterRacerStatisticsWindow, borderwidth=6, relief='sunken')
        self.btnFrame.grid(column=0, row=1, sticky=(N+S), padx=20, pady=20)
        self.btnFrame.columnconfigure(1, weight=1)
        self.btnFrame.rowconfigure(1, weight=1)
        self.btnAddRacerStatistics = Button(self.btnFrame, text = "Add Statistics", style = 'W.TButton', command=self.showForm)#command=addButtonWindow.addStatisticsWindow)
        self.btnAddRacerStatistics.grid(row = 0, column = 0, pady = 0, padx = 10)
        
        self.btnEditRacerStatistics = Button(self.btnFrame, text = "Edit Statistics", style = 'W.TButton', command=self.showEditableRows)
        self.btnEditRacerStatistics.grid(row = 1, column = 0, pady = 0, padx = 10)
        
        self.form_content = ttk.Frame(self.enterRacerStatisticsWindow, borderwidth=6, relief='sunken')
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
        
        