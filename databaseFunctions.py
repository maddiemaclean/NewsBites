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

def addEmail(emailIn):
    conn = sqlite3.connect('newsletter.db')
    cursor = conn.cursor()
    
    # Using parameterized query to avoid SQL injection
    cursor.execute('INSERT INTO emails (emailAddress) VALUES (?)', (emailIn,))
    
    conn.commit()
    conn.close()

def searchEmails(emailIn):
    conn = sqlite3.connect('newsletter.db')
    cursor = conn.cursor()
    
    # Using parameterized query
    cursor.execute('SELECT 1 FROM emails WHERE emailAddress = ?', (emailIn,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return True
    else:
        return False

def removeEmail(emailIn):
    if not searchEmails(emailIn):
        return False  # email cannot be found in the database.
    else:
        conn = sqlite3.connect('newsletter.db')
        cursor = conn.cursor()
        
        # Using parameterized query
        cursor.execute('DELETE FROM emails WHERE emailAddress = ?', (emailIn,))
        
        conn.commit()
        conn.close()
        return True  # email successfully removed

# -------- MAIN --------
email = "pidgepurr@gmail.com"
getEmailList()
addEmail(email)
getEmailList()
removeEmail(email)
getEmailList()
