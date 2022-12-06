import sys

def part1():
    l = 0

    fd = open(sys.argv[1], 'r')
    communication = fd.readline()

    seen = {}
    for r in range(len(communication)):
        present = seen.get(communication[r], -1)
        if present > -1 and present >= l:
            l = present + 1

        if r - l + 1 == 4:
            break
        seen[communication[r]] = r

    return r + 1


    

def part2():
    l = 0
    fd = open(sys.argv[1], 'r')
    communication = fd.readline()

    seen = {}
    for r in range(len(communication)):
        present = seen.get(communication[r], -1)
        if present > -1 and present >= l:
            l = present + 1

        if r - l + 1 == 14:
            break
        seen[communication[r]] = r

    return r + 1



start = part1()
print(start)

start = part2()
print(start)
