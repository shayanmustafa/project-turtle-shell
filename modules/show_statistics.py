from tkinter import * 
from tkinter.ttk import *
from tkinter import ttk
import sqlite3

path = 'c:/users/shaya/turtle-shell.db'

# function to open a new window  
# on a button click 
class ShowStatistics:

    def ShowStatisticsWindow(self): 
      
        # Toplevel object which will  
        # be treated as a new window 
        showStatisticsWindow = Toplevel() 
  
        # sets the title of the 
        # Toplevel widget 
        showStatisticsWindow.title("Show Racer's Statistics") 
        showStatisticsWindow.columnconfigure(0, weight=1)
        showStatisticsWindow.rowconfigure(0, weight=1)
        # sets the geometry of toplevel 
        showStatisticsWindow.geometry("700x500")
        
        #content frame (first frame)
        content = ttk.Frame(showStatisticsWindow, borderwidth=6, relief='sunken')
        content.grid(column=0, row=0, sticky=(N+S, E+W), padx=20, pady=20)
        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=1)
        
        #Connecting to sqlite
        conn = sqlite3.connect(path)
        
        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        
        select_placement_query = 'SELECT placement from racer_statistics where racer_id = ?'
        select_first_name_query = 'SELECT DISTINCT first_name from racer_statistics where racer_id = ?'
        select_last_name_query = 'SELECT DISTINCT last_name from racer_statistics where racer_id = ?'
        select_racing_name_query = 'SELECT DISTINCT racing_name from racer_statistics where racer_id = ?'
        select_league_query = 'SELECT DISTINCT league from racer_statistics where racer_id = ?'
        get_id_query = 'SELECT DISTINCT racer_id from racer_statistics'
        
        
        cursor.execute(get_id_query)
        rows_id = cursor.fetchall()
        
        racer_first_name = []
        for row_id in rows_id:
            cursor.execute(select_first_name_query, row_id)
            first_name_rows = cursor.fetchall()
            racer_first_name.append(first_name_rows)
        #print(racer_first_name)
        
        
        racer_last_name = []
        for row_id in rows_id:
            cursor.execute(select_last_name_query, row_id)
            last_name_rows = cursor.fetchall()
            racer_last_name.append(last_name_rows)
        #print(racer_last_name)
        
        racer_racing_name = []
        for row_id in rows_id:
            cursor.execute(select_racing_name_query, row_id)
            racing_name_rows = cursor.fetchall()
            racer_racing_name.append(racing_name_rows)
        #print(racer_racing_name)
            
        placement_rows = []
        racer_placement = []
        
        for row_id in rows_id:
            cursor.execute(select_placement_query, row_id)
            placement_rows = cursor.fetchall()
            racer_placement.append(placement_rows)
        #print(racer_placement)
        
        racer_league_name = []
        for row_id in rows_id:
            cursor.execute(select_league_query, row_id)
            league_rows = cursor.fetchall()
            racer_league_name.append(league_rows)
        #print(racer_league_name)
        
        table_frame = ttk.Frame(content, borderwidth=6, relief='sunken')
        table_frame.grid(column=0, row=0, sticky=(N+S, E+W), padx=20, pady=20)
        self.tv = Treeview(table_frame, show='headings', selectmode='browse')
        self.tv['columns'] = ('First Name', 'Last Name', 'Racing Name', '1', '2', '3', '4', '5', '6', '7', '8',
                              '9', '10', '11', '12', '13', '14', '15', 'League')
        self.tv.heading('First Name', text='First Name')
        self.tv.column('First Name', anchor='center', width=120)
        self.tv.heading('Last Name', text='Last Name')
        self.tv.column('Last Name', anchor='center', width=120)
        self.tv.heading('Racing Name', text='Racing Name')
        self.tv.column('Racing Name', anchor='center', width=120)
        self.tv.heading('1', text='1')
        self.tv.column('1', anchor='center', width=45)
        self.tv.heading('2', text='2')
        self.tv.column('2', anchor='center', width=45)
        self.tv.heading('3', text='3')
        self.tv.column('3', anchor='center', width=45)
        self.tv.heading('4', text='4')
        self.tv.column('4', anchor='center', width=45)
        self.tv.heading('5', text='5')
        self.tv.column('5', anchor='center', width=45)
        self.tv.heading('6', text='6')
        self.tv.column('6', anchor='center', width=45)
        self.tv.heading('7', text='7')
        self.tv.column('7', anchor='center', width=45)
        self.tv.heading('8', text='8')
        self.tv.column('8', anchor='center', width=45)
        self.tv.heading('9', text='9')
        self.tv.column('9', anchor='center', width=45)
        self.tv.heading('10', text='10')
        self.tv.column('10', anchor='center', width=45)
        self.tv.heading('11', text='11')
        self.tv.column('11', anchor='center', width=45)
        self.tv.heading('12', text='12')
        self.tv.column('12', anchor='center', width=45)
        self.tv.heading('13', text='13')
        self.tv.column('13', anchor='center', width=45)
        self.tv.heading('14', text='14')
        self.tv.column('14', anchor='center', width=45)
        self.tv.heading('15', text='15')
        self.tv.column('15', anchor='center', width=45)
        self.tv.heading('League', text='League')
        self.tv.column('League', anchor='center', width=120)
        
        self.tv.grid(sticky = (N,S,W,E))
        table_frame.treeview = self.tv
        table_frame.grid_rowconfigure(0, weight = 1)
        table_frame.grid_columnconfigure(0, weight = 1)
        
        # attach a Horizontal (x) scrollbar to the frame
        treeXScroll = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        treeXScroll.configure(command=self.tv.xview)
        self.tv.configure(xscrollcommand=treeXScroll.set)
        treeXScroll.grid(column=0, row=1, columnspan=3, sticky=E+W)
        
        len_of_empty_space = 18 - (len(racer_placement[0]) + 3)
        empty_space_list = []
        for i in range(len_of_empty_space):
            empty_space_list.append((''))
        
        #res = racer_first_name[0] + racer_last_name[0] + racer_racing_name[0] + racer_placement[0] + empty_space_list + racer_league_name[0]
        
        #print(tuple(item for tup in res for item in tup))
        
        stats_results = []
        for (racer_first_name_row, racer_last_name_row, racer_racing_name_row, racer_placement_row, racer_league_name_row) in zip(racer_first_name, racer_last_name, racer_racing_name, racer_placement, racer_league_name):
            len_of_empty_space = (19 - len(racer_placement_row) - 4)
            empty_space_list = []
            for i in range(len_of_empty_space):
                empty_space_list.append(tuple((' ')))
            res = racer_first_name_row + racer_last_name_row + racer_racing_name_row + racer_placement_row + empty_space_list + racer_league_name_row
            res_tup = tuple(item for tup in res for item in tup)
            stats_results.append(res_tup)
            #print(res)
        for results_row in stats_results:
            self.tv.insert("", "end", text="0", values=results_row)
        #print(stats_results)
        #print(empty_space_list)