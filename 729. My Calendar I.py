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
    def __init__(self,start,end):
        self.left=None
        self.right= None
        self.start=start
        self.end=end

    def insertion(self, start, end):
        cur = self
        while True:
            if start >= cur.end:
                if not cur.right:
                    cur.right=Tree(start,end)
                    return True
                cur = cur.right
            elif end <= cur.start:
                if not cur.left:
                    cur.left = Tree(start,end)
                    return True
                cur=cur.left
            else:
                return False

class MyCalendar:

    def __init__(self):
        self.root=None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root=Tree(start,end)
            return Tree
        return self.root.insertion(start,end)
