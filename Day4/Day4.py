file_input = open("Day4.txt")
lines = file_input.read().splitlines()

def in_range(elf_a, elf_b):
    elf_a_start, elf_a_end = int(elf_a.split("-")[0]), int(elf_a.split("-")[1])
    elf_b_start, elf_b_end = int(elf_b.split("-")[0]), int(elf_b.split("-")[1])
    
    return elf_b_start <= elf_a_start and elf_a_end <= elf_b_end

def overlap(elf_a, elf_b):
    elf_a_end = int(elf_a.split("-")[1])
    elf_b_start= int(elf_b.split("-")[0])
    return elf_a_end < elf_b_start 


count_a = 0
count_b = 0

for line in lines:
    elf_1, elf_2 = line.split(",")
    if in_range(elf_1, elf_2) or in_range(elf_2, elf_1):
        count_a +=1
    if overlap(elf_1, elf_2) or overlap(elf_2, elf_1):
        count_b +=1
    

print(count_a) #part 1
print(len(lines) - count_b) #part 1