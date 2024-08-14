# -------- DATABASE FUNCTIONS --------

import sqlite3

def getEmailList():
    # Connect to the database
    conn = sqlite3.connect('newsletter.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Query to select all data from the table
    cursor.execute('SELECT * FROM emails')
    rows = cursor.fetchall()

    # Iterate through the rows and print them
    for row in rows:
        print(row)

    conn.close()

def AddEmail(emailIn):
    conn = sqlite3.connect('newsletter.db')
    cursor = conn.cursor()
    cursor.execute('insert into emails (emailAddress) VALUES ('+ emailIn +');')
    conn.commit()
    conn.close()

def searchEmails(emailIn):
    conn = sqlite3.connect('newsletter.db')
    cursor = conn.cursor()
    cursor.excute('SELECT 1 FROM emails WHERE emailAddress = '+ emailIn + '')
    result = cursor.fetchone()
    conn.commit()
    conn.close()
    if result:
        return True
    else:
        return False


def removeEmail(emailIn):
    if searchEmails(emailIn) == False:
        return False # email cannot be found in the database. We cannot remove something that doesn't exist.
    else:
        conn = sqlite3.connect('newsletter.db')
        cursor = conn.cursor()
        cursor.excute('DELETE FROM emails WHERE emailAddress = '+emailIn +'')
        conn.commit()
        conn.close()
        return True # email successfully removed