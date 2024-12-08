file = open("./day2/input.txt", "r")

total = 0

for line in file.readlines():
    numbers = list(map(int, line.strip().split(" ")))
    is_increasing = numbers[0] < numbers[1]
    valid_line = 1
    for i in range(1, len(numbers)):
        if (numbers[i-1] < numbers[i]) is not is_increasing:
            valid_line = 0
            break
        if not (1 <= abs(numbers[i-1] - numbers[i]) <= 3):
            valid_line = 0
            break
    total += valid_line

print(total)
    