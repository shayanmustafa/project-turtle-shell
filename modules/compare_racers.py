from tkinter import * 
from tkinter.ttk import *
from tkinter import ttk
import sqlite3

path = 'c:/users/shaya/turtle-shell.db'

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
        print(placement_values)
                
            
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
        btnPredict = Button(treeview_content, text = "Predict", command=self.predictWinner)
        btnPredict.grid(row = 1, column = 1, pady = 20, padx = 20, sticky=(E+W))