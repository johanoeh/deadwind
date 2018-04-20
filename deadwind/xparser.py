from events import Event
import re

class TimeParser:

    def __init__(self, event):
        self.event = event
        self.timeRe = "[0-2]\d:[0-5]\d-[0-2]\d:[0-5]\d"
        self.dateRe = "20\d\d-[0-1][1-9]-[0-3][0-9]"

    def parse(self, timeStr, events):
        timeStr = timeStr.replace('\n',' ')
        timeStr = timeStr.strip()
        tokens = timeStr.split(' ')
        startMatch = re.match(self.dateRe, tokens[0])
        if not startMatch:
            return
        startDate = startMatch.group();
        for i in range(1,len(tokens)):
            match = re.match(self.timeRe,tokens[i]);
            if match:
                timeTokens = match.group().split('-');
                event = Event(
                                 self.event.subject,
                                 startDate,
                                 timeTokens[0],
                                 startDate,
                                 timeTokens[1],
                                 self.event.isAllDayEvent,
                                 self.event.description,
                                 self.event.location,
                                 self.event.isPrivate
                                 )
                events.append(event);
