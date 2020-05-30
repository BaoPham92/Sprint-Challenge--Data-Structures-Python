class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None]*capacity
        self.current = 0

    def append(self, item):
        self.storage[self.current] = item
        self.current = (self.current + 1) % self.capacity

    def get(self):
        return [
            x for x in self.storage
            if x != True and x != None
        ]
