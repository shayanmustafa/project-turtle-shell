from tkinter import * 
from tkinter.ttk import *

# function to open a new window  
# on a button click 
def ShowStatistics(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    showStatisticsWindow = Toplevel() 
  
    # sets the title of the 
    # Toplevel widget 
    showStatisticsWindow.title("Show Racer's Statistics") 
  
    # sets the geometry of toplevel 
    showStatisticsWindow.geometry("200x200") 
  
    # A Label widget to show in toplevel 
    Label(showStatisticsWindow,  
          text ="Show Racer's Statistics").pack()