import sys

class node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        

class list:
    def __init__(self):
        self.dummy = node()
        self.tailDummy = node(prev=self.dummy)
        self.dummy.next = self.tailDummy
        self.size = 0

    def getSize(self):
        return self.size

    # inserts to the bottom of the stack
    def insert(self, val):
        new = node(val, next=self.dummy.next, prev=self.dummy)
        self.dummy.next.prev = new
        self.dummy.next = new
        self.size += 1

    # regular push operation
    def push(self, val):
        new = node(val, next=self.tailDummy, prev=self.tailDummy.prev)
        self.tailDummy.prev.next = new
        self.tailDummy.prev = new
        self.size += 1

    # regular pop operation
    def pop(self):
        if self.getSize() < 1:
            return None

        self.size -= 1
        remove = self.tailDummy.prev
        remove.prev.next = self.tailDummy
        self.tailDummy.prev = remove.prev
        return remove.val



def part1():
    inputFile = open(sys.argv[1], 'r')
    stacks = []

    # read grid
    while True:
        line = inputFile.readline()
        if len(line) == 1 :
            break
        
        if not stacks:
            for stack in range(len(line) // 4):
                stacks.append(list())

        stack = 0
        for ind in range(len(line) // 4):
            item = line[ind * 4: ((ind + 1) * 4) - 1]
            if item[0] == '[':
                stacks[stack].insert(item[1])
            stack += 1


    # read instructions
    while True:
        line = inputFile.readline()
        if not line:
            break
        
        splits = line.split(' ')
        num, fromStack, toStack = int(splits[1]), int(splits[3]) - 1, int(splits[5]) - 1

        for i in range(num):
            removed = stacks[fromStack].pop()
            stacks[toStack].push(removed)

    crates = ''
    for stack in range(len(stacks)):
        crates += stacks[stack].pop()


    return crates



def part2():
    inputFile = open(sys.argv[1], 'r')
    stacks = []

    # read grid
    while True:
        line = inputFile.readline()
        if len(line) == 1 :
            break
        
        if not stacks:
            for stack in range(len(line) // 4):
                stacks.append(list())

        stack = 0
        for ind in range(len(line) // 4):
            item = line[ind * 4: ((ind + 1) * 4) - 1]
            if item[0] == '[':
                stacks[stack].insert(item[1])
            stack += 1


    # read instructions
    while True:
        line = inputFile.readline()
        if not line:
            break
        
        splits = line.split(' ')
        num, fromStack, toStack = int(splits[1]), int(splits[3]) - 1, int(splits[5]) - 1

        values = []
        for i in range(num):
            values.append(stacks[fromStack].pop())
    
        for i in range(num):
            stacks[toStack].push(values.pop())

    crates = ''
    for stack in range(len(stacks)):
        crates += stacks[stack].pop()


    return crates



crate = part1()
print(crate)

crate = part2()
print(crate)
