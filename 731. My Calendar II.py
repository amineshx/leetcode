class MyCalendarTwo:

    def __init__(self):
        self.intersection=[]
        self.non_intersecton=[]

    def book(self, start: int, end: int) -> bool:
        for i,j in self.intersection:
            if end > i and start < j :
                return False
        
        for i,j in self.non_intersecton:
            if end > i and start < j :
                interval = (max(i,start), min(j,end))
                self.intersection.append(interval)
        self.non_intersecton.append((start,end))
        return True