file_input = open('Day3.txt')
lines = file_input.read().splitlines()
score = 0

def part1():
    
    for line in lines:
        global score
        mid = len(line)//2
        first_half = line[0:mid]
        second_half = line[mid:len(line)]

        for char in first_half:
            for char2 in second_half:
                if char == char2:
                    common = char

        if ord(common) >= 97 and ord(common) <= 122:  
            score += ord(common) - 97 + 1
        elif ord(common) >= 65 and ord(common) <= 90:
            score += ord(common) - 65 + 27
        
    print(score)

def part2():
    while len(lines) > 0:
        global score
        first_r = set(lines.pop())
        second_r = set(lines.pop())
        third_r = set(lines.pop())

        common = ((first_r.intersection(second_r)).intersection(third_r)).pop()
       
        if ord(common) >= 97 and ord(common) <= 122:  
            score += ord(common) - 97 + 1
        elif ord(common) >= 65 and ord(common) <= 90:
            score += ord(common) - 65 + 27

    print(score)


part1()
part2()

file_input.close()

