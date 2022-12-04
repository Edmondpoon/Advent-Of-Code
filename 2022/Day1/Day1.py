import sys
import heapq

def part1():
    maxCalories = 0
    currentElf = 0

    inputFile = open(sys.argv[1], 'r')

    while True:
        line = inputFile.readline()
        if not line:
            break

        elif line == '\n':
            maxCalories = max(maxCalories, currentElf)
            currentElf = 0

        else:
            currentElf += int(line)
    
    return max(maxCalories, currentElf)

def part2():
    maxCalories = 0
    currentElf = 0

    inputFile = open(sys.argv[1], 'r')
    heap = []

    while True:
        line = inputFile.readline()
        if not line:
            break

        elif line == '\n':
            heapq.heappush(heap, -currentElf)
            currentElf = 0

        else:
            currentElf += int(line)
    
    return -heapq.heappop(heap) - heapq.heappop(heap) - heapq.heappop(heap)


maxCal = part1()
print(maxCal)

maxCal = part2()
print(maxCal)
