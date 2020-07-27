from tkinter import * 
from tkinter.ttk import *

# function to open a new window  
# on a button click 
def CompareRacers(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    compareRacersWindow = Toplevel() 
  
    # sets the title of the 
    # Toplevel widget 
    compareRacersWindow.title("Compare Racers") 
  
    # sets the geometry of toplevel 
    compareRacersWindow.geometry("200x200") 
  
    # A Label widget to show in toplevel 
    Label(compareRacersWindow,  
          text ="Compare Races").pack()