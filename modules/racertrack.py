from tkinter import * 
from tkinter.ttk import *
from tkinter import ttk

# function to open a new window  
# on a button click 

class RaceTrack:

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
        self.first_name_val = StringVar()
        self.first_name = Entry(form_content, textvariable=self.first_name_val)
        self.first_name.grid(row=1,column=0,columnspan=1, sticky=(E+W), padx=15)

        Label(form_content, text ="Laps").grid(row=0,column=1, sticky=(N, W, E, S), padx=15)
        self.last_name_val = StringVar()
        self.last_name = Entry(form_content, textvariable=self.last_name_val)
        self.last_name.grid(row=1,column=1,columnspan=1, sticky=(E+W), padx=15)

        Label(form_content, text="Racetrack Cup").grid(row=0,column=2, sticky=(N, W, E, S), padx=15)
        self.racing_name_val = StringVar()
        self.racing_name = Entry(form_content, textvariable=self.racing_name_val)
        self.racing_name.grid(row=1,column=2,columnspan=1, sticky=(E+W), padx=15)
        
        # add racer
        btnAdd = Button(form_content, text = "Add")
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
        
        self.tv.grid(sticky = (N,S,W,E))
        table_frame.treeview = self.tv
        table_frame.grid_rowconfigure(0, weight = 1)
        table_frame.grid_columnconfigure(0, weight = 1)