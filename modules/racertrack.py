from tkinter import * 
from tkinter.ttk import *

# function to open a new window  
# on a button click 
def RaceTrack(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    racetrackWindow = Toplevel() 
  
    # sets the title of the 
    # Toplevel widget 
    racetrackWindow.title("Enter Racetrack Information") 
  
    # sets the geometry of toplevel 
    racetrackWindow.geometry("200x200") 
  
    # A Label widget to show in toplevel 
    Label(racetrackWindow,  
          text ="Enter Racetrack information window").pack()