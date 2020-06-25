class MoneyBox:

    def __init__(self, capacity):
        self.capacity = capacity

    def add(self, n=1):
        self.capacity -= n

    def can_add(self, n=1):
        return self.capacity >= n


x = MoneyBox(5)
print(x.capacity)
print(x.can_add(1))
x.add(1)
print(x.capacity)
