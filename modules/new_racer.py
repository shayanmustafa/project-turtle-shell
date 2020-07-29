from tkinter import * 
from tkinter.ttk import *
from tkinter import ttk

# function to open a new window  
# on a button click 

def EnterRacer(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    racerWindow = Toplevel() 
    racerWindow['background']='#2A3132'
  
    # sets the title of the 
    # Toplevel widget 
    racerWindow.title("Enter New Racer")
    racerWindow.columnconfigure(0, weight=1)
    racerWindow.rowconfigure(0, weight=1)
    # sets the geometry of toplevel 
    racerWindow.geometry("700x500") 

    #content frame (first frame)
    content = ttk.Frame(racerWindow, borderwidth=6, relief='sunken')
    content.grid(column=0, row=0, sticky=(N, W, E, S), padx=20, pady=20)

    form_content = ttk.Frame(content)
    form_content.grid(column=1, row=1, sticky=(N, W, E, S), padx=20, pady=20)

    # A Label widget to show in toplevel 
    Label(form_content, text ="First Name").grid(row=0,column=0, sticky=(N, W, E, S), padx=15)
    first_name = Entry(form_content)
    first_name.grid(row=1,column=0,columnspan=1, sticky=(N, W, E, S), padx=15)

    Label(form_content, text ="Last Name").grid(row=0,column=1, sticky=(N, W, E, S), padx=15)
    last_name = Entry(form_content)
    last_name.grid(row=1,column=1,columnspan=1, sticky=(N, W, E, S), padx=15)

    Label(form_content, text="Racing Name").grid(row=0,column=2, sticky=(N, W, E, S), padx=15)
    racing_name = Entry(form_content)
    racing_name.grid(row=1,column=2,columnspan=1, sticky=(N, W, E, S), padx=15)

    Label(form_content, text="Age").grid(row=0,column=3, sticky=(N, W, E, S), padx=15)
    age = Entry(form_content)
    age.grid(row=1,column=3,columnspan=1, sticky=(N, W, E, S), padx=15)

    Label(form_content, text="Country").grid(row=3,column=0, sticky=(N, W, E, S), padx=15)
    country = Entry(form_content)
    country.grid(row=4,column=0,columnspan=1, sticky=(N, W, E, S), padx=15)

    Label(form_content, text="Team").grid(row=3,column=1, sticky=(N, W, E, S), padx=15)
    team = Entry(form_content)
    team.grid(row=4,column=1,columnspan=1, sticky=(N, W, E, S), padx=15)

    Label(form_content, text="League").grid(row=3,column=2, sticky=(N, W, E, S), padx=15)
    league = Entry(form_content)
    league.grid(row=4,column=2,columnspan=1, sticky=(N, W, E, S), padx=15)
    