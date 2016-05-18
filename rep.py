from collections import deque

class Node:
    def __init__(self):
        self.children = []
        self.state = None
        self.o = None
        self.c = None
        
    def addChild(self, child):
        self.children.append(child)
        
    def __len__(self):
        return 1 + sum(len(c) for c in self.children)

    def louds(self, sep=''):
        print('10', end=sep)
        dq = deque((self,))
        while len(dq) > 0:
            v = dq.popleft()
            for c in v.children:
                print('1', end='')
                dq.append(c)
            print('0', end=sep)
        print()
            
    def bp(self, sep=''):
        dq = deque((self,))
        while len(dq) > 0:
            v = dq.pop()
            if v.state == None:
                print('(', end='')
                v.state = 'open'
                dq.append(v)
                for c in reversed(v.children):
                    dq.append(c)
            elif v.state == 'open':
                print(')', end=sep)
                v.state = None
        print()
                
    def dfuds(self, sep=''):
        dq = deque((self,))
        print('(', end=sep)
        while len(dq) > 0:
            v = dq.pop()
            for c in reversed(v.children):
                print('(', end='')
                dq.append(c)
            print(')', end=sep)
        print()
            
    def format(self):
        x = 0
        dq = deque((self,))
        while len(dq) > 0:
            v = dq.pop()
            if v.state == None:
                v.state = 'open'
                v.o = x
                x += 1
                dq.append(v)
                for c in reversed(v.children):
                    dq.append(c)
            elif v.state == 'open':
                v.state = None
                v.c = x
                x += 1
                
        def printW(v):
            print('(', end='')
            print(' ' * (v.c - v.o - 1), end='')
            print(')', end='')
        
        def printV(v):
            x = int((v.c + v.o) / 2) - v.o
            print(',' * x, end='')
            print('()', end='')
            print('.' * x, end='')
        
        cl = 0
        dq = deque((self,))
        while len(dq) > 0: 
            v = dq.popleft()
            if v.c < cl:
                print()
                cl = 0

            print(' ' * (v.o - cl), end='')
            printV(v)
            cl = v.c + 1
            
            for c in v.children:
                dq.append(c)
        print()

    @staticmethod
    def fromParens(parens):
        root = Node()
        for c in parens:
            root.addChild(Node.fromParens(c))
        return root
