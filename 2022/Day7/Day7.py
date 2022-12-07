import sys

def search(fd):
    sum = 0
    
    directories = 0
    
    # grab ls command
    line = fd.readline()

    while True:
        line = fd.readline()
        if line and line.strip() == "$ cd ..":
            continue

        elif not line or line[:4] == "$ cd":
            break
        
        if line[0] == 'd':
            directories += 1

        else:
            sum += int(line.split(' ')[0])


    valid = 0
    for direc in range(directories):
        totalSum, val = search(fd)
        sum += totalSum
        valid += val

    if sum <= 100000:
        valid += sum
    
    return (sum, valid)


def part1():
    fd = open(sys.argv[1], 'r')
    
    # grab root directory
    line = fd.readline()

    return search(fd)[1]


# Search but it keeps track of the sizes rather than just the sum
def search2(fd):
    sums = []
    sum = 0
    directories = 0
    
    # grab ls command
    line = fd.readline()

    while True:
        line = fd.readline()
        if line and line.strip() == "$ cd ..":
            continue

        elif not line or line[:4] == "$ cd":
            break
        
        if line[0] == 'd':
            directories += 1

        else:
            sum += int(line.split(' ')[0])


    for direc in range(directories):
        totalSum = search2(fd)
        sums.extend(totalSum[0])
        sum += totalSum[1]

    return (sums + [sum], sum)


def part2():
    fd = open(sys.argv[1], 'r')
    
    # grab root directory
    line = fd.readline()

    sums, total = search2(fd)
    needed = 30000000 - (70000000 - total)
    sums.sort()

    for num in sums:
        if num >= needed:
            return num

    return -1
    

sum = part1()
print(sum)

removed = part2()
print(removed)
