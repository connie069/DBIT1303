import sqlite3
import datetime
import sys
from Booking import *

def prepareDB():
    try:
        conn=sqlite3.connect("database.db")
        c = conn.cursor()
        print("Database connection is successfull.")

        c.execute('''CREATE TABLE IF NOT EXISTS dates
         (id INTEGER PRIMARY KEY AUTOINCREMENT,
         owner TEXT NOT NULL,
         howmanypeople INT NOT NULL,
         dateof DATE NOT NULL,
         timeof INT NOT NULL);''')

        print("Table checking is ok.")
        print("\n---\n")
        conn.commit()
        conn.close()
    except:
        print("Hata")
        raise


def whishChoosing():
    print("\nPLEAE MAKE A CHOICE:")
    print("[1] New booking\n[2] Delete booking\n[3] Check the status for a day\n[4] Exit")
    try:
        choice = int(input("YOUR CHOICE: "))
        return choice
    except:
        print("Please, just type a number from 1 to 3.")
        whishChoosing()

def processChoosing(choosingParameter):
    if choosingParameter==1:
        newBooking()
    elif choosingParameter==2:
        deleteBooking()
    elif choosingParameter==3:
        bookingStatus()
    elif choosingParameter==4:
        sys.exit()
