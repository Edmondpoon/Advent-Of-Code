import sys

def part1():
    values = {}
    for char in range(ord('a'), ord('z') + 1):
        values[chr(char)] = char - ord('a') + 1

    for char in range(ord('A'), ord('Z') + 1):
        values[chr(char)] = char - ord('A') + 27

    fd = open(sys.argv[1], 'r')
    sum = 0

    while True:
        sack = fd.readline()
        if not sack:
            break

        sack = sack.strip()
        
        middle = len(sack) // 2
        duplicate = set(sack[:middle]).intersection(set(sack[middle:]))
        sum += values[duplicate.pop()]

    return sum



def part2():
    values = {}
    for char in range(ord('a'), ord('z') + 1):
        values[chr(char)] = char - ord('a') + 1

    for char in range(ord('A'), ord('Z') + 1):
        values[chr(char)] = char - ord('A') + 27

    fd = open(sys.argv[1], 'r')
    sum = 0

    while True:
        duplicate = fd.readline()
        if not duplicate:
            break
            
        duplicate = set(duplicate.strip())
        for row in range(2):
            duplicate = duplicate.intersection(set(fd.readline().strip()))

        sum += values[duplicate.pop()]

    return sum
    

sum = part1()
print(sum)

sum = part2()
print(sum)
