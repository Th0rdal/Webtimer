import datetime

class TimeSlot():
    start = None
    end = None
    path = ""
    database = None

    def __init__(self, database):
        self.database = database

    def startTime(self, temp):
        self.start = temp
    def endTime(self, temp):
        self.end = temp
        self.makeEntry()

    def makeEntry(self):
        print("Time:")
        if (isinstance(self.start, datetime.datetime) and isinstance(self.end, datetime.datetime)):
            startDate = self.start.strftime("%d%m%Y")
            endDate = self.end.strftime("%d%m%Y")
            startTime = int(self.start.strftime("%H"))*60 + int(self.start.strftime("%M"))
            endTime = int(self.end.strftime("%H"))*60 + int(self.end.strftime("%M"))
            totalTime = endTime - startTime
            data = {"startDate": startDate,"endDate": endDate,"startTime": startTime, "endTime": endTime, "totalTime":totalTime}
            self.database.insert(data)