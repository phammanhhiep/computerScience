import introAlgorithms.queue as queueLib


class Stack:
    def __init__(self, n=10):
        self.top = -1
        self.n = n
        self.array = []

    def push(self):
        if len(self.array) < n:
            self.top += 1
        else:
            raise Exception("Stack overflow")
            

    def pop(self):
        if len(self.array) >= 0:
            self.top -= 1
        else:
            raise Exception("Stack underflow")


# Implement a stack using two queues
class Stack2:
    def __init__(self, n=10):
        self.array = []
        self.q1 = queueLib.Queue()
        self.q2 = queueLib.Queue()
        self.n = n


    def push(self, x):
        '''
        Steps:
        + dequeue each element in self.q1 and enqueue that element to the self.q2
        + enqueue the new element to self.q1
        + dequeue each element in self.q2 and enqueue that element to the self.q1
        '''


    def pop(self):
        # call dequeue from self.q1