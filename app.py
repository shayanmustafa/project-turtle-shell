#from tkinter import Tk, Button, font
from tkinter import *
from tkinter.ttk import *
from modules.new_racer import EnterRacer
from modules.racer_statistics import RacerStatistics
from modules.racertrack import RaceTrack
from modules.show_statistics import ShowStatistics
from modules.compare_racers import CompareRacers
import sqlite3

path = 'store.db'

conn = sqlite3.connect(path)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS racer (racer_id INTEGER PRIMARY KEY UNIQUE, first_name CHAR, last_name CHAR, racing_name CHAR UNIQUE, age INTEGER, country CHAR, team CHAR, league CHAR)')
cursor.execute('CREATE TABLE IF NOT EXISTS racer_statistics (racer_id INTEGER, first_name CHAR, last_name CHAR, racing_name CHAR, race_num INTEGER, placement CHAR, num_of_racers INTEGER, league CHAR, racetrack CHAR)')
cursor.execute('CREATE TABLE IF NOT EXISTS racetrack (racetrack_id INTEGER PRIMARY KEY, racetrack_name CHAR, lap INTEGER, racetrack_cup CHAR)')


#create window object
app = Tk()
app.title('Racing Bet')
app.geometry('800x500')
app['background']='#2A3132'

# style object
style = Style()
style.theme_use('alt')
style.configure('W.TButton', font =
               ('Arial CYR', 10), 
                width = 25, height = 50, foreground = 'white', background = '#336B87', borderwidth = '1')
style.map('W.TButton', background=[('active','#336B87')])                 

titleLabel = Label(app, text="Project Turtle Shell")
titleLabel.place(relx=.5, rely=.15, anchor="center")
titleLabel.configure(font=("Courier", 25), borderwidth=2, relief="solid")

racerWindow = EnterRacer()
# enter new racer
btnNewRacer = Button(app, text = "Enter New Racer", style = 'W.TButton', command = racerWindow.EnterRacerWindow)
btnNewRacer.place(bordermode=OUTSIDE, relx=0.3, rely=0.4, height=50, width=200, anchor=E)

# enter racer statistics
racerStatisticsWindow = RacerStatistics()
btnRacerStatistics = Button(app, text = "Enter Racer Statistics", style = 'W.TButton', command = racerStatisticsWindow.RacerStatisticsWindow)
btnRacerStatistics.place(bordermode=OUTSIDE, relx=0.7, rely=0.4, height=50, width=200, anchor=W)

# enter racetrack information
racetrackWindow = RaceTrack()
btnRaceTrack = Button(app, text = "Enter Racetrack Information", style = 'W.TButton', command = racetrackWindow.raceTrackWindow)
btnRaceTrack.place(bordermode=OUTSIDE, relx=0.7, rely=0.7, height=50, width=200, anchor=W)

# show racer statistics
showStatistics = ShowStatistics()
btnShowStatistics = Button(app, text = "Show Racer's Statistics", style = 'W.TButton', command = showStatistics.ShowStatisticsWindow)
btnShowStatistics.place(bordermode=OUTSIDE, relx=0.3, rely=0.7, height=50, width=200, anchor=E)

# compare racers
compareRacers = CompareRacers()
btnCompareRacers = Button(app, text = "Compare Racers", style = 'W.TButton', command = compareRacers.compareRacersWindow)
btnCompareRacers.place(bordermode=OUTSIDE, relx=0.5, rely=0.6, height=50, width=200, anchor=S)

# start app
app.mainloop()