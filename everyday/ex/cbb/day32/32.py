# -*- coding: utf-8 -*-

class Stack():
    def __init__(self,size=20):
        self.stack  = []
        self.size = size
        self.top = -1

    def setsize(self,size):
        self.size = size

    def push(self,element):
        if self.isFull():
            raise "StackOverflow"
        else:
            self.stack.append(element)
            self.top  += 1

    def pop(self):
        if self.isEmpty():
            raise "StackUnderflow"
        else:
            element = self.stack[-1]
            self.top -= -1
            return element

    def Top(self):
        return self.top

    def empty(self):
        self.stack = []
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.top == self.size-1:
            return True
        else:
            return False

if __name__ == "__main__":
    stack = Stack()

    for i in range(10):
        stack.push(i)
        print stack.Top()



# 队列
#可以删除左边或者右边的元素 或者 在左边或者右边添加元素


class Queue():
    def __init__(self,size=20):
        self.queue = []
        self.size = size
        self.end = -1

    def setSize(self,size):
        self.size = size

    def leftIn(self,element):
        if self.end <self.size -1:
            self.queue = [element] + self.queue
            self.end = self.end + 1
        else:
            raise "QueueFull"
    def rightIn(self,element):
        if self.end < self.size -1:
            self.queue.append(element)
            self.end = self.end + 1
        else:
            raise "QueueFull"

    def leftOut(self):
        if self.end != -1:
            element = self.queue[0]
            self.queue = self.queue[1:]
            self.end = self.end - 1
            return element
        else:
            raise "QueueEmpty"
    def rightOut(self):
        if self.end != -1:
            element = self.queue[-1]
            self.queue = self.queue[0:len(self.queue)-2]
            self.end = self.end - 1
            return element
    def End(self):
        return self.end

    def empty(self):
        self.queue = []
        self.end = -1


#二叉树

class BTree():
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

    def insertLeft(self,value):
        self.left = BTree(value)
        return self.left

    def insertRight(self,value):
        self.right = BTree(value)
        return self.right

    def show(self):
        print self.data

def preorder(node):
    if node.data:
        node.show()
        if node.left:
            preorder(node.left)
        if node.right:
            preorder(node.right)

def inorder(node):
    if node.data:
        if node.left:
            inorder(node.left)
        if node.right:
            inorder(node.right)

def postorer(node):
    if node.data:
        if node.left:
            postorer(node.left)
        if node.right:
            postorer(node.right)
        node.show()

if __name__ == "__main__":
    Root = BTree("root")
    A = Root.insertLeft("A")
    C = A.insertLeft("C")
    D = C.insertRight("D")
    F = D.insertLeft("F")
    G = D.insertRight("G")
    B = Root.insertRight("B")
    E = B.insertRight("E")

    preorder(Root)
    print "="*30
    inorder(Root)
    print "+"*30
    postorer(Root)