from tkinter import Tk, Button, font
from tkinter.ttk import *
from modules.new_racer import EnterRacer
from modules.racer_statistics import RacerStatistics
from modules.racertrack import RaceTrack
from modules.show_statistics import ShowStatistics
from modules.compare_racers import CompareRacers

#create window object
app = Tk()
app.title('Racing Bet')
app.geometry('700x400')
app['background']='#2A3132'

# style object
style = Style()
style.theme_use('alt')
style.configure('W.TButton', font =
               ('Arial CYR', 10), 
                foreground = 'white', background = '#336B87', borderwidth = '1')
style.map('W.TButton', background=[('active','#336B87')])                 

racerWindow = EnterRacer()
# enter new racer
btnNewRacer = Button(app, text = "Enter New Racer", style = 'W.TButton', command = racerWindow.EnterRacerWindow)
btnNewRacer.grid(row = 0, column = 0, pady = 50, padx = 50)

# enter racer statistics
btnRacerStatistics = Button(app, text = "Enter Racer Statistics", style = 'W.TButton', command = RacerStatistics)
btnRacerStatistics.grid(row = 0, column = 1, pady = 50, padx = 50)

# enter racetrack information
btnRaceTrack = Button(app, text = "Enter Racetrack Information", style = 'W.TButton', command = RaceTrack)
btnRaceTrack.grid(row = 0, column = 2, pady = 50, padx = 50)

# show racer statistics
btnShowStatistics = Button(app, text = "Show Racer's Statistics", style = 'W.TButton', command = ShowStatistics)
btnShowStatistics.grid(row = 1, column = 0, pady = 50, padx = 50)

# compare racers
btnCompareRacers = Button(app, text = "Compare Racers", style = 'W.TButton', command = CompareRacers)
btnCompareRacers.grid(row = 1, column = 1, pady = 50, padx = 50)

# start app
app.mainloop()