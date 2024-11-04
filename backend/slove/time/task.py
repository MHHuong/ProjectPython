from datetime import datetime, timedelta

class Task:
    def __init__(self, name, startTime, endTime=None, duration=None):
        self.taskName = name
        self.startTime = startTime
        if duration is not None and endTime is None:
            self.endTime = startTime + timedelta(minutes=duration)
        else:
            self.endTime = endTime
        if duration is None and endTime is not None:
            self.duration = (endTime - startTime).total_seconds() / 60 
        else:
            self.duration = duration
        
    def __lt__(self, other):
        return self.startTime < other.startTime
        
    def timeToString(self, time):
        return time.strftime("%H:%M")
    
    def getInfo(self):
        return {
            "name": self.taskName,
            "start": self.timeToString(self.startTime),
            "end": self.timeToString(self.endTime),
            "duration": self.duration
        }
    
    def description(self):
        return f'{self.taskName} - {self.timeToString(self.startTime)} -> {self.timeToString(self.endTime)} : {self.duration} minutes'
