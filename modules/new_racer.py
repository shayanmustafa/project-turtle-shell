from tkinter import * 
from tkinter.ttk import *
from tkinter import ttk
from tkinter import Tk, Button, font

# function to open a new window  
# on a button click 

def EnterRacer(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    racerWindow = Toplevel() 
    racerWindow['background']='#2A3132'
  
    style = Style()
    style.theme_use('alt')
    style.configure('W.AddButton', font =
               ('Arial CYR', 10), 
                foreground = 'white', background = '#336B87', borderwidth = '1')
    style.map('W.AddButton', background=[('active','#336B87')])  

    # sets the title of the 
    # Toplevel widget 
    racerWindow.title("Enter New Racer")
    racerWindow.columnconfigure(0, weight=1)
    racerWindow.rowconfigure(0, weight=1)
    # sets the geometry of toplevel 
    racerWindow.geometry("700x500") 

    #content frame (first frame)
    content = ttk.Frame(racerWindow, borderwidth=6, relief='sunken')
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
    Label(form_content, text ="First Name").grid(row=0,column=0, sticky=(N, W, E, S), padx=15)
    first_name = Entry(form_content)
    first_name.grid(row=1,column=0,columnspan=1, sticky=(E+W), padx=15)

    Label(form_content, text ="Last Name").grid(row=0,column=1, sticky=(N, W, E, S), padx=15)
    last_name = Entry(form_content)
    last_name.grid(row=1,column=1,columnspan=1, sticky=(E+W), padx=15)

    Label(form_content, text="Racing Name").grid(row=0,column=2, sticky=(N, W, E, S), padx=15)
    racing_name = Entry(form_content)
    racing_name.grid(row=1,column=2,columnspan=1, sticky=(E+W), padx=15)

    Label(form_content, text="Age").grid(row=0,column=3, sticky=(N, W, E, S), padx=15)
    age = Entry(form_content)
    age.grid(row=1,column=3,columnspan=1, sticky=(E+W), padx=15)

    Label(form_content, text="Country").grid(row=3,column=0, sticky=(N, W, E, S), padx=15)
    country = Entry(form_content)
    country.grid(row=4,column=0,columnspan=1, sticky=(E+W), padx=15)

    Label(form_content, text="Team").grid(row=3,column=1, sticky=(N, W, E, S), padx=15)
    team = Entry(form_content)
    team.grid(row=4,column=1,columnspan=1, sticky=(E+W), padx=15)

    Label(form_content, text="League").grid(row=3,column=2, sticky=(N, W, E, S), padx=15)
    league = Entry(form_content)
    league.grid(row=4,column=2,columnspan=1, sticky=(E+W), padx=15)
    
    # show racer statistics
    btnAdd = Button(form_content, text = "Add")
    btnAdd.grid(row = 5, column = 0, pady = 20, padx = 20, sticky=(E+W))

    table_frame = ttk.Frame(content, borderwidth=6, relief='sunken')
    table_frame.grid(column=0, row=1, sticky=(N+S, E+W), padx=20, pady=20)
    tv = Treeview(table_frame)
    tv['columns'] = ('First Name', 'Last Name', 'Racing Name', 'Age', 'Country', 'Team', 'League')
    tv.heading('#0', text="Racer ID")
    tv.column('#0', width=50)
    tv.heading('First Name', text='First Name')
    tv.column('First Name', anchor='center', width=100)
    tv.heading('Last Name', text='Last Name')
    tv.column('Last Name', anchor='center', width=100)
    tv.heading('Racing Name', text='Racing Name')
    tv.column('Racing Name', anchor='center', width=100)
    tv.heading('Age', text='Age')
    tv.column('Age', anchor='center', width=100)
    tv.heading('Country', text='Country')
    tv.column('Country', anchor='center', width=100)
    tv.heading('Team', text='Team')
    tv.column('Team', anchor='center', width=100)
    tv.heading('League', text='League')
    tv.column('League', anchor='center', width=100)
    tv.insert("", "end", text="0", values=("Shayan", "Mustafa", "Racing Legend", "22", "Pakistan", "Liverpool", "PL"))
    tv.insert("", "end", text="0", values=("Roohan", "Mustafa", "Racing Legend", "28", "Pakistan", "Liverpool", "PL"))
    tv.grid(sticky = (N,S,W,E))
    table_frame.treeview = tv
    table_frame.grid_rowconfigure(0, weight = 1)
    table_frame.grid_columnconfigure(0, weight = 1)