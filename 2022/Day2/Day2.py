import sys

def part1():
    score = 0
    inputFile = open(sys.argv[1], 'r')

    points = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    
    outcomes = {
        'AX': 3,
        'BY': 3,
        'CZ': 3,
        'AY': 6,
        'BZ': 6,
        'CX': 6,
        'AZ': 0,
        'CY': 0,
        'BX': 0,
    }

    while True:
        line = inputFile.readline()
        if not line:
            break

        else:
            p1, p2 = line.strip().split(' ')
            score += points[p2] + outcomes[p1 + p2]

    
    return score


def part2():
    score = 0
    inputFile = open(sys.argv[1], 'r')

    points = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }
    
    outcomes = {
        'AX': 3,
        'BX': 1,
        'CX': 2,
        'AY': 1,
        'BY': 2,
        'CY': 3,
        'AZ': 2,
        'BZ': 3,
        'CZ': 1,
    }


    while True:
        line = inputFile.readline()
        if not line:
            break

        else:
            p1, p2 = line.strip().split(' ')
            score += points[p2] + outcomes[p1 + p2]

    
    return score
    

score = part1()
print(score)

score = part2()
print(score)
