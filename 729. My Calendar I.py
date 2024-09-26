# first sol
class MyCalendar:

    def __init__(self):
        self.events=[]

    def book(self, start: int, end: int) -> bool:
        for i,j in self.events:
            if not (j<= start or end<=i):
                return False
        
        self.events.append((start,end))
        return True



#second sol
class Tree:
    def __init__(self, start, end):
        self.left = None
        self.right = None
        self.start = start
        self.end = end

    def insertion(self, start, end):
        if start >= self.end:  
            if not self.right: 
                self.right = Tree(start, end)
                return True
            return self.right.insertion(start, end) 
        elif end <= self.start:  
            if not self.left:  
                self.left = Tree(start, end)
                return True
            return self.left.insertion(start, end)  
        else:
            return False  


class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:  
            self.root = Tree(start, end)
            return True  
        return self.root.insertion(start, end)


def simulate_my_calendar(commands, inputs):
    output = []
    myCalendar = None

    for i, command in enumerate(commands):
        if command == "MyCalendar":
            myCalendar = MyCalendar()
            output.append(None)  
        elif command == "book":
            start, end = inputs[i]
            result = myCalendar.book(start, end)
            output.append(result)  

    return output


commands = ["MyCalendar", "book", "book", "book"]
inputs = [[], [10, 20], [15, 25], [20, 30]]
output = simulate_my_calendar(commands, inputs)
print(output)
