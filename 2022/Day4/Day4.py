import sys

def part1():
    conflicts = 0
    fd = open(sys.argv[1], 'r')

    while True:
        line = fd.readline()
        if not line:
            break

        t1, t2 = line.split(',')

        start1, end1 = t1.split('-')
        start2, end2 = t2.split('-')

        start1, start2 = int(start1), int(start2)
        end1, end2 = int(end1), int(end2)

        if start1 <= start2 and end2 <= end1:
            conflicts += 1

        elif start2 <= start1 and end1 <= end2:
            conflicts += 1

    return conflicts
            


def part2():
    conflicts = 0
    fd = open(sys.argv[1], 'r')

    while True:
        line = fd.readline()
        if not line:
            break

        t1, t2 = line.split(',')

        start1, end1 = t1.split('-')
        start2, end2 = t2.split('-')

        start1, start2 = int(start1), int(start2)
        end1, end2 = int(end1), int(end2)

        if start1 <= start2 and start2 <= end1:
            conflicts += 1

        elif start2 <= start1 and start1 <= end2:
            conflicts += 1
        
        elif start2 <= end1 and end1 <= end2:
            conflicts += 1

        elif start1 <= end2 and end2 <= end1:
            conflicts += 1

    return conflicts
    

conflicts = part1()
print(conflicts)

conflicts = part2()
print(conflicts)
