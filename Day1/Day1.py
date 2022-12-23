file_input = open("Day1.txt")


lines = file_input.read().splitlines()
total = 0
totals_list = []

for i in range(len(lines)):
    if lines[i] == '':
        totals_list.append(total)
        total = 0
    else:
        total = total + int(lines[i])


totals_list_sorted = sorted(totals_list, reverse=True)
print(totals_list_sorted[0])            # maximum (part 1)
print(sum(totals_list_sorted[0:3]))     # sum of the first 3 entries  (part 2)
file_input.close()