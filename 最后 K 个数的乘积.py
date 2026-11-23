class ProductOfNumbers:

    def __init__(self):
        self.stream: list[int] = [1]

    def add(self, num: int) -> None:
        if num:
            self.stream.append(self.stream[-1]*num)
        else:
            self.stream = [1]

    def getProduct(self, k: int) -> int:
        if len(self.stream) <= k:
            return 0
        return self.stream[-1]//self.stream[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
