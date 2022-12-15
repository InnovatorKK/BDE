import sqlite3

class DB(object):
    def __init__(self, con):
        self.cur = con.cursor()

    def insert(self, DiscordID, Balance):
        self.cur.execute('INSERT INTO Account VALUES(:DiscordID, :Balance);', {"DiscordID":DiscordID, "Balance":Balance})
    
    
    """
    cur.execute("CREATE TABLE Account(DiscordID text, Balance text);")
    cur = con.cursor()

    

    name = 'SangJung'
    phoneNumber = '010-5670-2343'
    cur = con.cursor()
    

    cur.execute('SELECT * FROM Account')
    for row in cur:
        print(row)
    """