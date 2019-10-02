import datetime
import sqlite3
import itertools


class Connection:
    """Connection to the db file."""
    def __init__(self):
        self.conn = sqlite3.connect("to_do_list.db")
        self.cursor = self.conn.cursor()

    def closing_db(self):
        self.conn.close()


class Note:
    """Initializing a note."""
    def __init__(self, name, text, date_of_inception, scheduled_date):
        self.name = name
        self.text = text
        self.date_of_inception = date_of_inception
        self.scheduled_date = scheduled_date


class Notebook(dict):
    """Notebook"""
    def __init__(self):
        """Notebook initialization."""
        self.conn = Connection()
        self.notes = list(self.conn.cursor.execute("""SELECT text, 
            date_of_inception, scheduled_date, name FROM notes"""))
        self.all_notes = {i[3]: [i[0], i[1], i[2]] for i in self.notes}
        self.conn.closing_db()

    def add_a_note(self):
        """Adding a new note to the notebook."""
        try:
            name = str(input("Please, enter a name of the new note: "))
            text = str(input("Please, enter a text of the new note: "))
            date_of_inception = str(datetime.date.today())
            scheduled_date = str(input("Please, enter a scheduled date of the"
            " new note. Use the format YYYY-MM-DD: "))
            if self.validate_date_format(scheduled_date) == False:
                return
            note = Note(name, text, date_of_inception, scheduled_date)
            self.all_notes[note.name] = [note.text, note.date_of_inception,
            note.scheduled_date]
            self.conn = Connection()
            inserted = [(note.text, note.date_of_inception, note.scheduled_date, 
                note.name)]
            self.conn.cursor.executemany("INSERT INTO notes VALUES (?,?,?,?)",\
             inserted)
            self.conn.conn.commit()
            self.conn.closing_db()
        except sqlite3.IntegrityError:
            print("\n")
            print ("************************   WARNING   *********************************")
            print ("A note with the same name already exists. Please enter different name.")
            print ("**********************************************************************")

    def delete_a_note(self):
        """Removal of a note."""
        try:
            name = str(input("Please, enter the name of the deleted note: "))
            self.conn = Connection()
            self.conn.cursor.execute("DELETE FROM notes WHERE name = ?", 
                (name,))
            self.conn.conn.commit()
            self.conn.closing_db()
            print ("\n")
            print("The Deleted note: | {:<5s} | Scheduled: {:<12s}"
                "||| Note name: {:<5s} | Created: {:<5s} "\
             .format( self.all_notes[name][0], self.all_notes[name][2], 
                name,self.all_notes[name][1]))
            del self.all_notes[name]
        except KeyError:
            print ("**********************   WARNING   *********************************")
            print ("Please, enter the correct name of the note you would like to delete.")
            print ("*******************************************************************")
        except:
            print ("**********************   WARNING   *****************")
            print ("Exception caused by wrong interaction with database.")
            print ("****************************************************")

    def validate_date_format(self, scheduled_date):
        """Date type validation."""
        try:
            datetime.datetime.strptime(scheduled_date, '%Y-%m-%d')
            return True
        except ValueError:
            print("\n")
            print ("*****************      WARNING   ************************")
            print ("The date format of the inserted note should be YYYY-MM-DD")
            print ("*********************************************************")
            return False

