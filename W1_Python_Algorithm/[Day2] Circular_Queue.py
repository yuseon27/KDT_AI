class CircularQueue:

    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue full')
        self.rear = (self.rear + 1) % self.maxCount

        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.isEmpty() :
            raise IndexError('Queue empty')
        self.front = (self.front + 1) % self.maxCount

        x = self.data[self.front]

        self.count -= 1
        return x

    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[(self.front + 1) % self.maxCount]



def solution(x):
    return 0


cq = CircularQueue(3)

cq.enqueue(2)
print(cq.dequeue())
cq.enqueue(4)
cq.enqueue(6)
print(cq.dequeue())
cq.enqueue(8)
cq.enqueue(10)

print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())

