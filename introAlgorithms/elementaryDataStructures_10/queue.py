class Queue:
    def __init__(self, n=10):
        self.array = []
        self.n = n
        self.head = -1
        self.tail = 0


    def dequeue(self):
        if self.head < 0:
            raise Exception("Queue underflows")
        elif self.head < self.n - 1:
            self.head += 1
        elif self.head == self.n - 1:
            self.head = 0


    def enqueue(self, i):
        if self.head == self.tail + 1 or (self.tail == self.n-1 and self.head == 0):
            raise Exception("Queue overflows")
        if self.tail < self.head or (self.tail > self.head and self.tail < self.n-1):
            self.tail += 1
            self.array[self.tail-1] = i


# Implement queue using 2 stack
class Queue2:
    pass