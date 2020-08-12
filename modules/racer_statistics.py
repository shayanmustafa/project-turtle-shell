from tkinter import * 
from tkinter.ttk import *
from tkinter import ttk
import sqlite3

path = 'c:/users/shaya/turtle-shell.db'

# function to open a new window  
# on a button click
class RacerStatistics:
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
        table_frame.grid(column=0, row=0, sticky=(N+S, E+W), padx=20, pady=20)
        self.tv = Treeview(table_frame, show='headings', selectmode='browse')
        self.tv['columns'] = ('First Name', 'Last Name', 'Racing Name')
        self.tv.heading('First Name', text='First Name')
        self.tv.column('First Name', anchor='center', width=100)
        self.tv.heading('Last Name', text='Last Name')
        self.tv.column('Last Name', anchor='center', width=100)
        self.tv.heading('Racing Name', text='Racing Name')
        self.tv.column('Racing Name', anchor='center', width=100)
        
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute("SELECT first_name, last_name, racing_name from racer")
        self.rows = cursor.fetchall()
        for row in self.rows:
            self.tv.insert("", "end", text="0", values=row)
        conn.close()
        
        self.tv.grid(sticky = (N,S,W,E))
        table_frame.treeview = self.tv
        table_frame.grid_rowconfigure(0, weight = 1)
        table_frame.grid_columnconfigure(0, weight = 1)