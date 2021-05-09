class Node:
    
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail


    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        if prev.next == None : return None
        curr = prev.next
        prev.next = curr.next
        if prev.next == None : self.tail = prev

        self.nodeCount -= 1
        result = curr.data
        del(curr)
        return result


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount : 
            raise IndexError

        prev = self.getAt(pos-1)

        return self.popAfter(prev)

    def concat(self, L):
        self.tail.next = L.head.next
        if L.tail:
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

L.insertAt(1, a)
print(L.traverse())

L.insertAt(1, b)
print(L.traverse())

L.insertAt(2, c)
print(L.traverse())

L.insertAt(4, d)
print(L.traverse())

pop = L.popAt(1)
print(pop, L.traverse())
