file = open("./day1/input.txt", "r")
lefts = []
occurrences = {}
for line in file.readlines():
    left, right = list(map(int, line.split("  ")))
    lefts.append(left)
    try:
        occurrences[right] += 1
    except Exception:
        occurrences[right] = 1

total = 0
for l in lefts:
    total += l * occurrences.get(l, 0)

print(total)