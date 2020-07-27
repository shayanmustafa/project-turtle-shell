from tkinter import * 
from tkinter.ttk import *

# function to open a new window  
# on a button click 
def EnterRacer(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    racerWindow = Toplevel() 
  
    # sets the title of the 
    # Toplevel widget 
    racerWindow.title("Enter New Racer") 
  
    # sets the geometry of toplevel 
    racerWindow.geometry("200x200") 
  
    # A Label widget to show in toplevel 
    Label(racerWindow,  
          text ="Enter new racer window").pack()