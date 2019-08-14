#latin_2
#teva delar on february 2018
#teva.delar at gmail.com

#imports
#from faker import Faker
import tkinter as tk
from tkinter import *
from tkinter import ttk

# from tinydb import TinyDB, Query
# db = TinyDB('./ir.json')


#tkinter themes
s = ttk.Style()
s.theme_use('aqua')


#Variables
year = None
age  = StringVar
tax_household = StringVar

welcome_message = "here goes nothing"
# ------------ functions --------------#
def show_frame(frame_name):
    for widget in  frame_name.get('container').winfo_children():
            widget.destroy()
    
    right = Label(frame_name.get('container'), text=frame_name.get('content'), background="grey")
    frame_name.get('container').add(right)
    

def onselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    value2 =  ('You selected item %d: "%s"' % (index, value))
    frame_name = {'container':RightContainer, 'content':value2}
    show_frame(frame_name)



def onselect_exploitation(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    print(index)
    exploitation_buttons.get(index)()


def get_names(fname_entry, lname_entry):
    # print("test"+" "+fname_entry, lname_entry)
    db.insert({'first_name':fname_entry,
              'lastname':lname_entry})
    print("here is the value " +str(fname_entry) +" "+ str(lname_entry))

def foyer_fiscal():
    #here should go the entry containers
    year_var = StringVar()
    if year == None:
        year_label = ttk.Label(Filter_Year, text=" please select a year")
        year_label.grid(row = 0, column=0,padx=5)

        year_combo_box = ttk.Combobox(Filter_Year, textvariable = year_var)
        year_combo_box["values"] = ("2017", "2018","2019","2020","2021")
        year_combo_box.grid(row=0, column=2, sticky="E")


    else:
        pass


    Label1 = Label(Main_W, text="First Name")
    Label1.grid(row=0)
    Label2 = Label(Main_W, text="Last Name")
    Label2.grid(row=1)


    fname_entry = ttk.Entry(Main_W, width=20)
    lname_entry = ttk.Entry(Main_W, width=20)
    fname_entry.grid(row=0, column=1)
    lname_entry.grid(row=1, column=1)
    Valid = Button(Main_W, text="Next", command = lambda: get_names(fname_entry.get(), lname_entry.get()))
    Valid.grid(row=3, column=0,sticky=W, pady=4)
    Quit = Button(Main_W, text="Quit", command = quit)
    Quit.grid(row=3, column=1,sticky=W, pady=4)



def membres():
    print ("one declaration per members")


def structure():
    print("here we will define the stucture elmnts")

exploitation_buttons = {
    0 :foyer_fiscal,
    1 : membres,
    2 : structure,
}



#------------ Frames --------------#
#As we can only add a widget to a PanedWindow (which is a frame) and not to a Label (which is a widget), let's create a frame
MainFrame = PanedWindow(orient = HORIZONTAL, width=700, height=450)
MainFrame.pack(fill=BOTH, expand=1)

LeftContainer = PanedWindow(MainFrame, orient= VERTICAL, width=184)
MainFrame.add(LeftContainer)

#right is a PanedWindow, it will go right as it is added second, all frames added to right will be added vertically
RightContainer = PanedWindow(MainFrame, orient=VERTICAL, background = 'grey')
MainFrame.add(RightContainer)


#------------- Frames --------------#
Analyse_title = PanedWindow(LeftContainer, height= 20, background='grey')
LeftContainer.add(Analyse_title)
 
Analyse = PanedWindow(LeftContainer, height= 80, background='white')
LeftContainer.add(Analyse)

Exploitation_title = PanedWindow(LeftContainer, height= 20, background='grey')
LeftContainer.add(Exploitation_title)

Exploitation = PanedWindow(LeftContainer, height= 300, width=250, background='white')
LeftContainer.add(Exploitation)

Filter_Year = PanedWindow(RightContainer, height=30, background = 'grey')
RightContainer.add(Filter_Year)


Main_W = PanedWindow(RightContainer, background = 'white')
RightContainer.add(Main_W)


#------------ Entry Containers  --------------#
#here should go the entry containers
#feet = StringVar()
#meters= StringVar()
#feet_entry = tk.Entry(RightContainer, width=40, text=feet)
#feet_entry.grid()

#------------ Widgets --------------#

#ANALYSE
label = Label(Analyse_title, text="Analyse", background='grey')
label.grid()

liste_A = Listbox(Analyse, background='white',borderwidth=0, selectmode = EXTENDED)
liste_A.insert(1, "    Acceuil")
liste_A.insert(2, "    Rapport")
liste_A.insert(3, "    Point de vue")
liste_A.grid()
liste_A.bind("<<ListboxSelect>>", onselect_exploitation)

#Exploitation
label = Label(Exploitation_title, text="Exploitation", background='grey')
label.grid()

liste_E = Listbox(Exploitation, background='white',borderwidth=0, selectmode = EXTENDED)
liste_E.insert(1, "    Foyer Fiscal")
liste_E.insert(2, "    Revenus")
liste_E.insert(3, "    Param")
liste_E.grid()
liste_E.bind("<<ListboxSelect>>", onselect_exploitation)

#------------ Mainloop --------------#
mainloop()