import sqlite3

class AccountDB(object):
    def __init__(self):
        self.con = sqlite3.connect('data.db', isolation_level=None)
        self.cur = self.con.cursor()
        #self.cur.execute("CREATE TABLE Account(DiscordID text, Balance integer);")

    def register(self, DiscordID, Balance):
        self.cur.execute('INSERT INTO Account VALUES(:DiscordID, :Balance);', {"DiscordID":DiscordID, "Balance":Balance})

    def check(self, DiscordID):
        self.cur.execute('SELECT * FROM Account')
        ret=[]
        for row in self.cur:
            ret.append(row)
        ret = dict(ret)
        return ret
    def deposit(self, ctx, amount):
        data = self.cur.execute("SELECT * FROM Account")
        print(data)
        self.cur.execute("UPDATE Account SET Balance = :balance WHERE DiscordID = :discordid", {"balance": -amount, "discordid":ctx.user.id})
        
    def withdraw(self):
        ...
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