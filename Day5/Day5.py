file_input = open("Day5.txt")
lines = file_input.read()

# Separating the instructions from the stack diagram using the empty line
diagram,instructions = lines.split("\n\n")

# Removing the newline characters and creating a list of instructions
diagram,instructions = diagram.splitlines(),instructions.splitlines()


# Setting up a dictionary for each column by extracting the last line
stacks = {int(digit):[] for digit in diagram[-1].replace(" ", "")}
# print(stacks)
# Saving the indexes of the digits to extract each of the information
indexes = [index for index, char in enumerate(diagram[-1]) if char != " "]

def savingstacks():
    for strings in diagram[:-1]:
        stack_count = 1
        for index in indexes:
            if strings[index] != " ":
                stacks[stack_count].insert(0, strings[index])        
            stack_count +=1

savingstacks()

# Only keeping the digits from the instructions
instruct_digits = []
for i in range(len(instructions)):
    string = instructions[i].split()
    instruct_digits.append([int(string[1]),int(string[3]),int(string[5])])

    crates = instruct_digits[i][0]
    from_stack = instruct_digits[i][1]
    to_stack = instruct_digits[i][2]

    for crate in range(crates):
        crates_removed = stacks[from_stack].pop()
        stacks[to_stack].append(crates_removed)

def clearstacks():
    for stack in stacks:
        stacks[stack].clear()

def getendcrates():
    top_crates = ""
    for i in range(1,len(stacks)+1):
        top_crates += stacks[i][-1]
    print(top_crates)



# Part 1
getendcrates() 


# Part2
clearstacks()
savingstacks()

# Only keeping the digits from the instructions
instruct_digits = []
for i in range(len(instructions)):
    string = instructions[i].split()
    instruct_digits.append([int(string[1]),int(string[3]),int(string[5])])

    crates = instruct_digits[i][0]
    from_stack = instruct_digits[i][1]
    to_stack = instruct_digits[i][2]

    crates_to_remove = stacks[from_stack][-crates:]  # - starts from the end
    stacks[from_stack] = stacks[from_stack][:-crates] # remove the crates

    for crate in crates_to_remove:
        stacks[to_stack].append(crate)  # adding crates to the to_stack

getendcrates()


# a = [5,4,3,2,1]
# print(a[-3:])
# print(a[:-3])