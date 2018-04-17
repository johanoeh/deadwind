# event with format that suits the google calendar format
class Event :
    def __init__(
                 self,
                 subject,
                 startDate,
                 startTime,
                 endDate,
                 endTime,
                 isAllDayEvent,
                 description,
                 location,
                 isPrivate
                 ):
        self.subject = subject
        self.startDate=startDate;
        self.startTime=startTime
        self.endDate = endDate
        self.endTime =endTime
        self.isAllDayEvent = isAllDayEvent
        self.description = description
        self.location = location
        self.isPrivate = isPrivate

    def toCSV(self):
              return (
                         self.subject+","+
                         self.startDate+","+
                         self.startTime+","+
                         self.endDate+","+
                         self.endTime+","+
                         str(self.isAllDayEvent)+","+
                         self.description+","+
                         self.location+","+
                         str(self.isPrivate)
                     );
    def toICAL(self):
        print("to implement")
