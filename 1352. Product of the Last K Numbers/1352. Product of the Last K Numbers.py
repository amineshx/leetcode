class ProductOfNumbers:

    def __init__(self):
        self.res = []
        self.product=1

    def add(self, num: int) -> None:
        if num==0:
            self.product=1
            self.res=[]
        else:
            self.product*=num
            self.res.append(self.product)

    def getProduct(self, k: int) -> int:
        if len(self.res)<k:
            return 0
        elif len(self.res)==k:
            return self.res[-1]
        else:
            return int(self.res[-1]/self.res[-1*(1+k)])



obj = ProductOfNumbers()
commands = ["ProductOfNumbers", "add", "add", "add", "add", "add", "getProduct", "getProduct", "getProduct", "add", "getProduct"]
params = [[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]]

output = []
for i in range(len(commands)):
    command = commands[i]
    param = params[i]

    if command == "add":
        obj.add(param[0])
        output.append(None)  
    elif command == "getProduct":
        result = obj.getProduct(param[0])
        output.append(result)

print(output)