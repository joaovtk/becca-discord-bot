import sqlite3

class BaseDatabase():
    def __init__(self, databaseName):
        self.databaseName = databaseName

class AchievementsCount(BaseDatabase):
    def __init__(self):
        super().__init__(databaseName="db/achievementsCount.db")
        self.con = sqlite3.connect(self.databaseName)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users(userid VARCHAR(30))")
        self.cur.execute("CREATE TABLE IF NOT EXISTS commands (commandName VARCHAR(30))")
        self.cur.execute("CREATE TABLE IF NOT EXISTS commandsUser(commandName VARCHAR(30), userid VARCHAR(30),count INTEGER)")
    def open(self):
        self.con = sqlite3.connect(self.databaseName)
        self.cur = self.con.cursor()
    def addUser(self, userid: str):
        self.open()
        response = self.cur.execute("SELECT * FROM users WHERE userid = ?", ([userid])).fetchone()

        if not response:
            self.cur.execute("INSERT INTO users VALUES(?)", ([userid]))
            self.con.commit()
    def addCommand(self, commandName: str):
        self.open()
        response = self.cur.execute("SELECT * FROM commands WHERE commandName = ?", ([commandName])).fetchone()
        if not response:
            self.cur.execute("INSERT INTO commands VALUES(?)", ([commandName]))
            self.con.commit()
        self.con.close()
    def incCount(self, commandName: str, userId: str) -> str:
        self.open()
        responseUsers = self.cur.execute("SELECT * FROM users WHERE userid = ?", ([userId])).fetchone()
        responseCommands = self.cur.execute("SELECT * FROM commands WHERE commandName = ?", ([commandName])).fetchone()
        
        if not responseUsers and not responseCommands:
            self.addUser(userId)
            self.addCommand(commandName)
        response = self.cur.execute("SELECT * FROM commandsUser WHERE userid = ? AND commandName = ?",  ([userId, commandName])).fetchone()
        if response:
            print(response)
            val = response[2] + 1
            
            self.cur.execute("UPDATE commandsUser SET count = ?", ([val]))
        else:
            print()
            self.cur.execute("INSERT INTO commandsUser VALUES(?, ?, ?)", ([responseCommands[0], responseUsers[0], 1]))

        self.con.commit()
            
        self.con.close()
    def getCount(self, commandName: str, userId: str):
        self.open()
        response = self.cur.execute("SELECT * FROM commandsUser WHERE userid = ? AND commandName = ?", ([userId, commandName])).fetchone()
        print(response)
        if response:
            return response[2]
        else:
            self.addCommand(commandName)
            self.addUser(userId)
            self.incCount(commandName, userId)
            return 1
        