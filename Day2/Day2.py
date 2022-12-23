# A, X = rock (1)
# B, Y = paper (2)
# C, Z = scissors (3)

# 0 = lose
# 3 = draw
# 6 = win

# X = lose, Y = draw, Z = win

file_input = open("Day2.txt")
lines = file_input.read().splitlines()



points_dict = {'X': 1, 'Y': 2, 'Z': 3, "rock" : 1, "paper": 2, "scissor": 3}
outcomes = {"lose": 0, "draw": 3, "win": 6}

score = 0
outcome = ''

def part1():
    global score
    for round in lines:
        round_split = round.split()
        
        # draw conditions
        if round_split[0] == 'A' and round_split[1] == 'X':
            outcome = "draw"
        elif round_split[0] == 'B' and round_split[1] == 'Y':
            outcome = "draw"
        elif round_split[0] == 'C' and round_split[1] == 'Z':
            outcome = "draw"

        # win conditions
        elif round_split[0] == 'A' and round_split[1] == 'Y':
            outcome = "win"
        elif round_split[0] == 'B' and round_split[1] == 'Z':
            outcome = "win"
        elif round_split[0] == "C" and round_split[1] == 'X':
            outcome = "win"

        # lose conditions
        else:
            outcome = "lose"
        score += outcomes[outcome] + points_dict[round_split[1]]

    print(score)



end = {'X': "lose", 'Y': "draw", 'Z' : "win"}
paper = {"win" : "scissor", "draw" : "paper", "lose" : "rock"}
rock = {"win" : "paper", "draw" : "rock", "lose" : "scissor"}
scissor = {"win": "rock", "draw": "scissor", "lose": "paper"}

def part2():
    global score
    for round in lines:
        round_split = round.split()
        
        if round_split[0] == 'A':
            outcome = end[round_split[1]]
            score += points_dict[rock[outcome]] + outcomes[outcome]
        elif round_split[0] == 'B':
            outcome = end[round_split[1]]
            score += points_dict[paper[outcome]] + outcomes[outcome]
        elif round_split[0] == 'C':
            outcome = end[round_split[1]]
            score += points_dict[scissor[outcome]] + outcomes[outcome]
    print(score)


part1()
part2()

file_input.close()