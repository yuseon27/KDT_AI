class ArrayQueue:
    
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def bft(self):
        traversal = []
        queue = ArrayQueue()

        if not self.root : return []
        queue.enqueue(self.root)

        while(not queue.isEmpty()) : #{
            curr = queue.dequeue()
            traversal += curr.data
            if curr.left : queue.enqueue(curr.left)
            if curr.right : queue.enqueue(curr.right)   
        #}

        return traversal


def solution(x):
    return 0
