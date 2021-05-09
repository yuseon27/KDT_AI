class Node:
    
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    def popAt(self, pos):  # {
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        if pos == 1:  # delete the first node
            curr = self.head
            self.head = curr.next
            if pos == self.nodeCount : self.tail = self.head  # delete the only one left node

        else:
            prev = self.getAt(pos-1)
            curr = prev.next
            prev.next = curr.next

            if pos == self.nodeCount:  ## delete the last none
                self.tail = prev

        self.nodeCount -= 1
        result = curr.data
        del(curr)
        return result
    #}

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

    def concat(self, L):
        last = self.tail.prev
        first = L.head.next
        last.next = first
        first.prev = last
        self.tail = L.tail
        self.nodeCount += L.nodeCount



def solution(x):
    return 0


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

L = LinkedList()
L.insertAt(1, a)
L.insertAt(2, b)
L.insertAt(3, c)
L.insertAt(4, d)

pop = L.popAt(3)
print(pop, L.traverse())

pop = L.popAt(3)
print(pop, L.traverse())

pop = L.popAt(1)
print(pop, L.traverse())

pop = L.popAt(1)
print(pop, L.traverse())

pop = L.popAt(1)
print(pop, L.traverse())
