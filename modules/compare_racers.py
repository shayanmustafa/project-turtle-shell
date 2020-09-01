from tkinter import * 
from tkinter.ttk import *
from tkinter import ttk

import sqlite3

#path = 'c:/users/shaya/turtle-shell.db'
path = 'store.db'

conn = sqlite3.connect(path)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS racer (racer_id INTEGER PRIMARY KEY UNIQUE, first_name CHAR, last_name CHAR, racing_name CHAR UNIQUE, age INTEGER, country CHAR, team CHAR, league CHAR)')
cursor.execute('CREATE TABLE IF NOT EXISTS racer_statistics (racer_id INTEGER, first_name CHAR, last_name CHAR, racing_name CHAR, race_num INTEGER, placement CHAR, num_of_racers INTEGER, league CHAR, racetrack CHAR)')
cursor.execute('CREATE TABLE IF NOT EXISTS racetrack (racetrack_id INTEGER PRIMARY KEY, racetrack_name CHAR, lap INTEGER, racetrack_cup CHAR)')

class CompareRacers:
    
    def addToCompareList(self):
        selected_items = self.tv_total_racers.selection()
        items_to_delete = []
        for selected_item in selected_items:
            items_to_delete.append(self.tv_total_racers.item(selected_item)['values'][2])
            racing_name = self.tv_total_racers.item(selected_item)['values'][2]
            self.tv_total_racers.delete(selected_item)
            
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute('SELECT DISTINCT first_name, last_name, racing_name FROM racer_statistics WHERE racing_name = ?', (racing_name,))
        self.compare_rows = cursor.fetchall()
        for row in self.compare_rows:
            self.tv_compare_racers.insert("", "end", text="0", values=row)
        conn.close()
        
        
    
    def predictWinner(self):
        racing_name_list = []
        for line in self.tv_compare_racers.get_children():
            for value in self.tv_compare_racers.item(line)['values']:
                racing_name_list.append(value)
               
        racing_name_values = racing_name_list[2::3]
        print(racing_name_values)
        #Connecting to sqlite
        conn = sqlite3.connect(path)
        
        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        
        #select_placement_query = 'SELECT placement from racer_statistics where placement = ?'
        placement_rows = []
        racer_placement = []
        for values in racing_name_values:
            cursor.execute('SELECT placement from racer_statistics where racing_name = ?', (values,))
            placement_rows = cursor.fetchall()
            racer_placement.append(placement_rows)
        
        placement_values = [[x for tup in lst for x in tup] for lst in racer_placement]
        
        points_dictionary = {'1st': 15, '2nd': 12, '3rd': 10, '4th': 9, '5th': 8, '6th': 7, '7th': 6, '8th': 5,
                      '9th': 4, '10th': 3, '11th': 2, '12th': 1}
        placement_points = [[points_dictionary.get(item, item) for item in lst] for lst in placement_values]
        #print(placement_points)
        sum_of_points = []
        for points in placement_points:
            sum_of_points.append(sum(points))
        print(sum_of_points)
        
        racenum_rows = []
        racer_racenum = []
        for name_values in racing_name_values:
            cursor.execute('SELECT race_num from racer_statistics where racing_name = ?', (name_values,))
            racenum_rows = cursor.fetchall()
            racer_racenum.append(racenum_rows)
        racenum_values = [[x for tup in lst for x in tup] for lst in racer_racenum]
        
        race_number = []
        for values in racenum_values:
            race_number.append(values[-1])
        print(race_number)
        
        avg = [i / j for i, j in zip(sum_of_points, race_number)] 
        win_avg = [x / 15 for x in avg]
        self.win_percentage = [int(y * 100) for y in win_avg]
        
        print(self.win_percentage)
        pred_result = list(zip(racing_name_values, self.win_percentage))
        print(pred_result)
        for pred in pred_result:
            self.tv_prediction.insert("", "end", text="0", values=pred)
        
    # function to open a new window  
    # on a button click 
    def compareRacersWindow(self): 
      
        # Toplevel object which will  
        # be treated as a new window 
        compareRacersWindow = Toplevel() 
        compareRacersWindow['background']='#2A3132'
  
        # sets the title of the 
        # Toplevel widget 
        compareRacersWindow.title("Compare Racers") 
  
        # sets the geometry of toplevel 
        compareRacersWindow.geometry("700x500")
        compareRacersWindow.columnconfigure(0, weight=1)
        compareRacersWindow.rowconfigure(0, weight=1)
        
        #content frame (first frame)
        content = ttk.Frame(compareRacersWindow, borderwidth=6, relief='sunken')
        content.grid(column=0, row=0, sticky=(N+S, E+W), padx=20, pady=20)
        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=1)
        
        treeview_content = ttk.Frame(content)
        treeview_content.grid(column=0, row=0, sticky=(N, E+W), padx=20, pady=20)
        
        #total racers table
        self.tv_total_racers = Treeview(treeview_content, show='headings', selectmode='browse')
        self.tv_total_racers['columns'] = ('First Name', 'Last Name', 'Racing Name')
        self.tv_total_racers.heading('First Name', text='First Name')
        self.tv_total_racers.column('First Name', anchor='center', width=100)
        self.tv_total_racers.heading('Last Name', text='Last Name')
        self.tv_total_racers.column('Last Name', anchor='center', width=100)
        self.tv_total_racers.heading('Racing Name', text='Racing Name')
        self.tv_total_racers.column('Racing Name', anchor='center', width=100)
        
        self.tv_total_racers.grid(row=0, column=0, sticky = (N,S,W,E))
        treeview_content.treeview = self.tv_total_racers
        treeview_content.grid_rowconfigure(0, weight = 1)
        treeview_content.grid_columnconfigure(0, weight = 1)
        
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT first_name, last_name, racing_name FROM racer_statistics")
        self.rows = cursor.fetchall()
        for row in self.rows:
            self.tv_total_racers.insert("", "end", text="0", values=row)
        conn.close()
        
        # add racer to compare list
        btnAddRacerToCompare = Button(treeview_content, text = "Add to Compare List", command=self.addToCompareList)
        btnAddRacerToCompare.grid(row = 0, column = 1, pady = 20, padx = 20, sticky=(E+W))
        
        #racers to compare table
        self.tv_compare_racers = Treeview(treeview_content, show='headings', selectmode='browse')
        self.tv_compare_racers['columns'] = ('First Name', 'Last Name', 'Racing Name')
        self.tv_compare_racers.heading('First Name', text='First Name')
        self.tv_compare_racers.column('First Name', anchor='center', width=100)
        self.tv_compare_racers.heading('Last Name', text='Last Name')
        self.tv_compare_racers.column('Last Name', anchor='center', width=100)
        self.tv_compare_racers.heading('Racing Name', text='Racing Name')
        self.tv_compare_racers.column('Racing Name', anchor='center', width=100)
        
        self.tv_compare_racers.grid(row=0, column=2, sticky = (N,S,W,E))
        treeview_content.treeview = self.tv_compare_racers
        treeview_content.grid_rowconfigure(0, weight = 1)
        treeview_content.grid_columnconfigure(2, weight = 1)
        
        # predict button
        btnPredict = Button(treeview_content, text = "Calculate Prediction", command=self.predictWinner)
        btnPredict.grid(row = 3, column = 1, pady = 20, padx = 20, sticky=(E+W))
        
        
        #racers to compare table
        self.tv_prediction = Treeview(treeview_content, show='headings', selectmode='browse')
        self.tv_prediction['columns'] = ('Racing Name', 'Win Prediction')
        self.tv_prediction.heading('Racing Name', text='Racing Name')
        self.tv_prediction.column('Racing Name', anchor='center', width=100)
        self.tv_prediction.heading('Win Prediction', text='Win Prediction')
        self.tv_prediction.column('Win Prediction', anchor='center', width=100)
        
        self.tv_prediction.grid(row=4, column=1, sticky = (N,S,W,E))
        treeview_content.treeview = self.tv_prediction
        treeview_content.grid_rowconfigure(1, weight = 1)
        treeview_content.grid_columnconfigure(2, weight = 1)