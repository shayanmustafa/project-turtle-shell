from tkinter import * 
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import ttk
from tkinter import Tk, Button, font
import sqlite3

#path = 'c:/users/shaya/turtle-shell.db'
path = 'store.db'

conn = sqlite3.connect(path)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS racer (racer_id INTEGER PRIMARY KEY UNIQUE, first_name CHAR, last_name CHAR, racing_name CHAR UNIQUE, age INTEGER, country CHAR, team CHAR, league CHAR)')
cursor.execute('CREATE TABLE IF NOT EXISTS racer_statistics (racer_id INTEGER, first_name CHAR, last_name CHAR, racing_name CHAR, race_num INTEGER, placement CHAR, num_of_racers INTEGER, league CHAR, racetrack CHAR)')
cursor.execute('CREATE TABLE IF NOT EXISTS racetrack (racetrack_id INTEGER PRIMARY KEY, racetrack_name CHAR, lap INTEGER, racetrack_cup CHAR)')

class EnterRacer:
    def editRacer(self):
        empty = 0
        if self.first_name_val.get() == '' or self.last_name_val.get() == '' or self.racing_name_val.get() == '' or self.age_val.get() == '' or self.country_val.get() == '' or self.team_val.get() == '' or self.league_val.get() == '':
            empty = 1
        if empty == 1:
            messagebox.showinfo(title="Input Error", message="Any information about the racer cannot be empty", parent=self.racerWindow)
        elif empty == 0:
            #cursor.execute('DELETE FROM racer WHERE racing_name = ?'(self.racing_name_entry,))
            self.tv.delete(self.selected_rows)
            add_for_edit_query = 'INSERT INTO racer (first_name, last_name, racing_name, age, country, team, league) VALUES(?, ?, ?, ?, ?, ?, ?)'
            delete_for_edit_query = 'DELETE FROM racer WHERE racing_name = ?'
            cursor.execute(delete_for_edit_query, (self.racing_name_entry,))
            conn.commit()
            cursor.execute(add_for_edit_query, (self.first_name_val.get(), self.last_name_val.get(), self.racing_name_val.get(),
                            self.age_val.get(), self.country_val.get(), self.team_val.get(), self.league_val.get()))
            last_row_id = cursor.lastrowid
            conn.commit()
        
            cursor.execute("SELECT first_name, last_name, racing_name, age, country, team, league FROM racer WHERE racer_id = " + str(last_row_id))
            self.new_rows = cursor.fetchall()
            for row in self.new_rows:
                self.tv.insert("", "end", text="0", values=row)
                
            self.first_name.delete(0, "end")
            self.last_name.delete(0, "end")
            self.racing_name.delete(0, "end")
            self.age.delete(0, "end")
            self.country.delete(0, "end")
            self.team.delete(0, "end")
            self.league.delete(0, "end")
            #conn.close()
            
    def editSelectedRow(self):
        self.selected = 0
        self.selected_rows = []
        self.selected_rows = self.tv.selection()
        if not self.selected_rows:
            #self.edit_form_content.grid_remove()
            messagebox.showinfo(title="Select Editable Row", message="Please first select one of the rows from the list to edit racer information.", parent=self.racerWindow)
        else:
            self.selected = 1
            #self.edit_form_content.grid(column=0, row=3, sticky=(N+S, E+W), padx=20, pady=20)
            items_first_name = []     
            for selected_row in self.selected_rows:          
                items_first_name.append(self.tv.item(selected_row)['values'][0])
            
            items_last_name = []
            for selected_row in self.selected_rows:          
                items_last_name.append(self.tv.item(selected_row)['values'][1])
                
            items_racing_name = []
            for selected_row in self.selected_rows:          
                items_racing_name.append(self.tv.item(selected_row)['values'][2])
                
            items_age = []
            for selected_row in self.selected_rows:          
                items_age.append(self.tv.item(selected_row)['values'][3])
                
            items_country = []
            for selected_row in self.selected_rows:          
                items_country.append(self.tv.item(selected_row)['values'][4])
            
            items_team = []
            for selected_row in self.selected_rows:          
                items_team.append(self.tv.item(selected_row)['values'][5])
            
            items_league = []
            for selected_row in self.selected_rows:          
                items_league.append(self.tv.item(selected_row)['values'][6])
                
            self.first_name_entry = items_first_name[0]
            self.last_name_entry = items_last_name[0]
            self.racing_name_entry = items_racing_name[0]
            self.age_entry = items_age[0]
            self.country_entry = items_country[0]
            self.team_entry = items_team[0]
            self.league_entry = items_league[0]
            
            self.first_name_val.set(self.first_name_entry)
            self.last_name_val.set(self.last_name_entry)
            self.racing_name_val.set(self.racing_name_entry)
            self.age_val.set(self.age_entry)
            self.country_val.set(self.country_entry)
            self.team_val.set(self.team_entry)
            self.league_val.set(self.league_entry)
    
    def addRacerIntoDb(self):
        exists = 0
        #Connecting to sqlite
        conn = sqlite3.connect(path)
        
        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        cursor.execute("SELECT first_name, last_name, racing_name FROM racer")
        racer_rows = cursor.fetchall()
        insert_query = """ INSERT INTO racer (first_name, last_name, racing_name, age, country, team, league)
                            VALUES(?, ?, ?, ?, ?, ?, ?) """
                            
        first_name = self.first_name_val.get()
        last_name = self.last_name_val.get()
        racing_name = self.racing_name_val.get()
        age = self.age_val.get()
        country = self.country_val.get()
        team = self.team_val.get()
        league = self.league_val.get()
        
        if first_name == '' or last_name == '' or racing_name == '' or age == '' or country == '' or team == '' or league == '':
           messagebox.showinfo(title="Input Error", message="Any information field cannot be empty.", parent=self.racerWindow)
           exists = 1
           conn.close()
        elif int(age) < 16:
           messagebox.showinfo(title="Input Error", message="Age should be between 16 and 100", parent=self.racerWindow)
           exists = 1
           conn.close()
        elif int(age) > 100:
            messagebox.showinfo(title="Input Error", message="Age should be between 16 and 100", parent=self.racerWindow)
            exists = 1
            conn.close()
        elif len(first_name) > 20:
            messagebox.showinfo(title="Input Error", message="First name cannot exceed 20 characters", parent=self.racerWindow)
            exists = 1
            conn.close()
        elif len(last_name) > 20:
            messagebox.showinfo(title="Input Error", message="Last name cannot exceed 20 characters", parent=self.racerWindow)
            exists = 1
            conn.close()
        elif len(racing_name) > 20:
            messagebox.showinfo(title="Input Error", message="Racing name cannot exceed 20 characters", parent=self.racerWindow)
            exists = 1
            conn.close()
        elif len(country) > 20:
            messagebox.showinfo(title="Input Error", message="Country name cannot exceed 20 characters", parent=self.racerWindow)
            exists = 1
            conn.close()
        elif len(team) > 20:
            messagebox.showinfo(title="Input Error", message="Team name cannot exceed 20 characters", parent=self.racerWindow)
            exists = 1
            conn.close()
        elif len(league) > 20:
            messagebox.showinfo(title="Input Error", message="League name cannot exceed 20 characters", parent=self.racerWindow)
            exists = 1
            conn.close()
        else:
            for row in racer_rows:
                if(row[0] == first_name and row[1] == last_name and row[2] == racing_name):
                    messagebox.showinfo(title="Input Error", message="The racer information already exists.", parent=self.racerWindow)
                    
                    conn.close()
                    exists = 1
                elif row[2] == racing_name:
                    messagebox.showinfo(title="Input Error", message="The racing name already exists. Please enter a unique racing name.", parent=self.racerWindow)
                    exists = 1
        if exists == 0:
            print(racing_name)
            self.first_name.delete(0, "end")
            self.last_name.delete(0, "end")
            self.racing_name.delete(0, "end")
            self.age.delete(0, "end")
            self.country.delete(0, "end")
            self.team.delete(0, "end")
            self.league.delete(0, "end")
            #conn = sqlite3.connect(path)
            cursor.execute(insert_query, (first_name, last_name, racing_name,
                            age, country, team, league))
            last_row_id = cursor.lastrowid
            conn.commit()
        
            cursor.execute("SELECT first_name, last_name, racing_name, age, country, team, league FROM racer WHERE racer_id = " + str(last_row_id))
            self.rows = cursor.fetchall()
            for row in self.rows:
                self.tv.insert("", "end", text="0", values=row)
            conn.close()
            
    
    def deleteRacer(self):
        conn = sqlite3.connect(path)
        selected_items = self.tv.selection()
        items_to_delete = []     
        for selected_item in selected_items:          
            items_to_delete.append(self.tv.item(selected_item)['values'][2])
            self.tv.delete(selected_item)
            tuple(items_to_delete)
            delete_query = 'DELETE FROM racer WHERE racing_name=?'
            delete_stats_query = 'DELETE FROM racer_statistics WHERE racing_name=?'
            cur = conn.cursor()
            cur.execute(delete_query, (items_to_delete))
            cur.execute(delete_stats_query, (items_to_delete))
            conn.commit()
        conn.close()
        
    def EnterRacerWindow(self):
        self.racerWindow = Toplevel() 
        self.racerWindow['background']='#2A3132'

        style = Style()
        style.theme_use('alt')
        style.configure('W.AddButton', font =
            ('Arial CYR', 10), 
            foreground = 'white', background = '#336B87', borderwidth = '1')
        style.map('W.AddButton', background=[('active','#336B87')])  

        # sets the title of the 
        # Toplevel widget 
        self.racerWindow.title("Enter New Racer")
        self.racerWindow.columnconfigure(0, weight=1)
        self.racerWindow.rowconfigure(0, weight=1)
        # sets the geometry of toplevel 
        self.racerWindow.geometry("700x500") 

        #content frame (first frame)
        content = ttk.Frame(self.racerWindow, borderwidth=6, relief='sunken')
        content.grid(column=0, row=0, sticky=(N+S, E+W), padx=20, pady=20)
        content.columnconfigure(0, weight=1)
        content.rowconfigure(1, weight=1)

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
        self.first_name_val = StringVar()
        self.first_name = Entry(form_content, textvariable=self.first_name_val)
        self.first_name.grid(row=1,column=0,columnspan=1, sticky=(E+W), padx=15)

        Label(form_content, text ="Last Name").grid(row=0,column=1, sticky=(N, W, E, S), padx=15)
        self.last_name_val = StringVar()
        self.last_name = Entry(form_content, textvariable=self.last_name_val)
        self.last_name.grid(row=1,column=1,columnspan=1, sticky=(E+W), padx=15)

        Label(form_content, text="Racing Name").grid(row=0,column=2, sticky=(N, W, E, S), padx=15)
        self.racing_name_val = StringVar()
        self.racing_name = Entry(form_content, textvariable=self.racing_name_val)
        self.racing_name.grid(row=1,column=2,columnspan=1, sticky=(E+W), padx=15)

        Label(form_content, text="Age").grid(row=0,column=3, sticky=(N, W, E, S), padx=15)
        self.age_val = StringVar()
        self.age = Entry(form_content, textvariable=self.age_val)
        self.age.grid(row=1,column=3,columnspan=1, sticky=(E+W), padx=15)

        Label(form_content, text="Country").grid(row=3,column=0, sticky=(N, W, E, S), padx=15)
        self.country_val = StringVar()
        self.country = Entry(form_content, textvariable=self.country_val)
        self.country.grid(row=4,column=0,columnspan=1, sticky=(E+W), padx=15)

        Label(form_content, text="Team").grid(row=3,column=1, sticky=(N, W, E, S), padx=15)
        self.team_val = StringVar()
        self.team = Entry(form_content, textvariable=self.team_val)
        self.team.grid(row=4,column=1,columnspan=1, sticky=(E+W), padx=15)

        Label(form_content, text="League").grid(row=3,column=2, sticky=(N, W, E, S), padx=15)
        self.league_val = StringVar()
        self.league = Entry(form_content, textvariable=self.league_val)
        self.league.grid(row=4,column=2,columnspan=1, sticky=(E+W), padx=15)

        # add racer
        btnAdd = Button(form_content, text = "Add", command=self.addRacerIntoDb)
        btnAdd.grid(row = 5, column = 0, pady = 20, padx = 20, sticky=(E+W))
        
        # delete racer row
        btnAdd = Button(form_content, text = "Delete", command=self.deleteRacer)
        btnAdd.grid(row = 5, column = 1, pady = 20, padx = 20, sticky=(E+W))
        
        # edit selected row
        btnAdd = Button(form_content, text = "Edit Selected Row", command=self.editSelectedRow)
        btnAdd.grid(row = 5, column = 2, pady = 20, padx = 20, sticky=(E+W))
        
        # edit racer
        btnAdd = Button(form_content, text = "Edit Racer", command=self.editRacer)
        btnAdd.grid(row = 5, column = 3, pady = 20, padx = 20, sticky=(E+W))
        
        table_frame = ttk.Frame(content, borderwidth=6, relief='sunken')
        table_frame.grid(column=0, row=1, sticky=(N+S, E+W), padx=20, pady=20)
        self.tv = Treeview(table_frame, show='headings', selectmode='browse')
        self.tv['columns'] = ('First Name', 'Last Name', 'Racing Name', 'Age', 'Country', 'Team', 'League')
        self.tv.heading('First Name', text='First Name')
        self.tv.column('First Name', anchor='center', width=100)
        self.tv.heading('Last Name', text='Last Name')
        self.tv.column('Last Name', anchor='center', width=100)
        self.tv.heading('Racing Name', text='Racing Name')
        self.tv.column('Racing Name', anchor='center', width=100)
        self.tv.heading('Age', text='Age')
        self.tv.column('Age', anchor='center', width=100)
        self.tv.heading('Country', text='Country')
        self.tv.column('Country', anchor='center', width=100)
        self.tv.heading('Team', text='Team')
        self.tv.column('Team', anchor='center', width=100)
        self.tv.heading('League', text='League')
        self.tv.column('League', anchor='center', width=100)
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute("SELECT first_name, last_name, racing_name, age, country, team, league FROM racer")
        self.rows = cursor.fetchall()
        for row in self.rows:
            self.tv.insert("", "end", text="0", values=row)
        conn.close()
        print(self.rows)
        #tv.insert("", "end", text="0", values=("Shayan", "Mustafa", "Racing Legend", "22", "Pakistan", "Liverpool", "PL"))
        #tv.insert("", "end", text="0", values=("Roohan", "Mustafa", "Racing Legend", "28", "Pakistan", "Liverpool", "PL"))
        self.tv.grid(sticky = (N,S,W,E))
        table_frame.treeview = self.tv
        table_frame.grid_rowconfigure(0, weight = 1)
        table_frame.grid_columnconfigure(0, weight = 1)
        
        # attach a Horizontal (x) scrollbar to the frame
        treeYScroll = ttk.Scrollbar(table_frame, orient=VERTICAL)
        treeYScroll.configure(command=self.tv.yview)
        self.tv.configure(yscrollcommand=treeYScroll.set)
        treeYScroll.grid(column=3, row=0, columnspan=3, sticky=N + S)