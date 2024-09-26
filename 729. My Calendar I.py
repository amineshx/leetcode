class MyCalendar:

    def __init__(self):
        self.events=[]

    def book(self, start: int, end: int) -> bool:
        for i,j in self.events:
            if not (j<= start or end<=i):
                return False
        
        self.events.append((start,end))
        return True