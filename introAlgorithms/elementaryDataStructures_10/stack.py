import logging

import elementaryDataStructures_10.queue as queueLib


logging.basicConfig(filename='log/stack.log',level=logging.DEBUG)


class Stack:
    def __init__(self, n=10):
        self.top = -1
        self.n = n
        self.array = [None for i in range(n)]

    def push(self, obj):
        self.top += 1
        if self.top <= self.n-1:
            self.array[self.top] = obj
        else:
            raise Exception("Stack overflow")
            

    def pop(self):
        if self.top >= 0:
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
        '''
        call dequeue from self.q1
        '''
