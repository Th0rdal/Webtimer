import sqlite3
import sqlite3 as sl
import json

class Database:

    def __init__(self): #initialize database
        self.conn = sl.connect("timeTable.db", check_same_thread=False)
        self.c = self.conn.cursor()



    def insert(self, data): #insert data into database
        executionText = "INSERT INTO timeTable VALUES (:startDate, :endDate, :startTime, :endTime, :totalTime)"
        with self.conn:
            try:
                self.c.execute(executionText, data)
            except sqlite3.OperationalError:
                self.c.execute("""CREATE TABLE timeTable (
                    startDate integer,
                    endDate integer,
                    startTime integer,
                    endTime integer,
                    totalTime integer
                    )""")
                self.c.execute(executionText, data)

    def delete(self, table, data):
        print("not implemented")

    def get(self, value):
        executionText = "SELECT * FROM account WHERE"
        for key in value:
            executionText = executionText + " " + key + " = :" + key

        with self.conn:
            self.c.execute(executionText, value)
        return self.c.fetchall()

    def printTable(self):
        executionText = "SELECT * FROM timeTable"
        self.c.execute(executionText)
        print(self.c.fetchall())

    def getTableAsJson(self):
        executionText = "SELECT * FROM timeTable"
        data = self.c.execute(executionText).fetchall()
        data_dict = {}
        print("")
        print(self.c.description)
        for index, col in enumerate(data):
            data_dict[index] = dict()
            for index2, row in enumerate(self.c.description):
                print(str(row[0]))
                data_dict[index][str(row[0])] = col[index2]
        f = open("output/output.json", "w")
        f.write(json.dumps(data_dict))
        f.close()
