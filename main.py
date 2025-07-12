# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 20:51:53 2025

@author: Sasha Folloso
"""

# Libraries
import sqlite3

# Functions

# Main Program
if __name__ == '__main__':
    connection = sqlite3.connect('booklog.db')
    cur = connection.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS bookentry
                        (id TEXT, title TEXT, author TEXT, date_read TEXT, notes TEXT)''')
                        
    while(True):
        cur.execute('SELECT COUNT(*) FROM bookentry')
        num_entries = cur.fetchone()[0]
        menu_option = int(input("\nWhat would you like to do? \n 1: View booklog. \n 2: Add entry. \n 3: Edit entry. \n 4: Exit the application.\n>> "))
        
        if menu_option == 1:
            print("\nThis is the current booklog:")
            for row in cur.execute('''SELECT * FROM bookentry'''):
                print(row)
                
        elif menu_option == 2:
            entry_id:int = num_entries + 1
            entry_title:str = input("\nTitle of the work: ")
            entry_author:str = input("\nAuthor: ")
            entry_date:str = input("Date read (YYYY-MM-DD): ")
            entry_notes:str = input("\nThoughts?: ")
            cur.execute('''INSERT OR IGNORE INTO bookentry 
                       VALUES (?, ?, ?, ?, ?)''',
                       (str(entry_id), entry_title, entry_author, entry_date, entry_notes))
            connection.commit()
            
        elif menu_option == 3:
            print("\nThis is the current booklog:")
            for row in cur.execute('''SELECT * FROM bookentry'''):
                print(row)
            edit_id = input("Which entry would you like to edit?\n>> ")
            edit_option = int(input("What attribute do you want to change? \n 1: Title \n 2: Author \n 3: Date \n 4: Notes\n>> "))
            if edit_option == 1:
                new_title:str = input("\nNew title: ")
                cur.execute('''UPDATE bookentry SET title = ? WHERE id = ?''',
                            (new_title, edit_id))
                connection.commit()
            elif edit_option == 2:
                new_author:str = input("\nNew author: ")
                cur.execute('''UPDATE bookentry SET author = ? WHERE id = ?''',
                            (new_author, edit_id))
                connection.commit()
            elif edit_option == 3:
                new_date:str = input("\nNew date (YYYY-MM-DD): ")
                cur.execute('''UPDATE bookentry SET date_read = ? WHERE id = ?''',
                            (new_date, edit_id))
                connection.commit()
            elif edit_option == 4:
                new_notes:str = input("\nNew notes: ")
                cur.execute('''UPDATE bookentry SET notes = ? WHERE id = ?''',
                            (new_notes, edit_id))
                connection.commit()
            
        elif menu_option == 4:
            break
                
    cur.close()
    connection.close()
