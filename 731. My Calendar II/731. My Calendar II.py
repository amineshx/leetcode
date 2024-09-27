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


def simulate_my_calendar(commands, inputs):
    output = []
    myCalendar = None

    for i, command in enumerate(commands):
        if command == "MyCalendarTwo":
            myCalendar = MyCalendarTwo()
            output.append(None)  
        elif command == "book":
            start, end = inputs[i]
            result = myCalendar.book(start, end)
            output.append(result)  

    return output


commands = ["MyCalendarTwo","book","book","book","book","book","book"]
inputs = [[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
output = simulate_my_calendar(commands, inputs)
print(output)
