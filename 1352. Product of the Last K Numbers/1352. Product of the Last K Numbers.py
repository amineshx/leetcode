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


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)