from tkinter import * 
from tkinter.ttk import *

# function to open a new window  
# on a button click 
def RacerStatistics(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    enterRacerStatisticsWindow = Toplevel() 
  
    # sets the title of the 
    # Toplevel widget 
    enterRacerStatisticsWindow.title("Enter Racer Statistics") 
  
    # sets the geometry of toplevel 
    enterRacerStatisticsWindow.geometry("200x200") 
  
    # A Label widget to show in toplevel 
    Label(enterRacerStatisticsWindow,  
          text ="Enter Racer Statistics window").pack()