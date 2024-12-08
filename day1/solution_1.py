def quicksort(array):
    if len(array)< 2:
        return array
    p = array[0]
    l = [i for i in array[1:] if i<=p]
    g = [i for i in array[1:] if i>p]
    return quicksort(l) + [p] + quicksort(g)

file = open("./day1/test.txt", "r")
lefts = []
rights = []
for line in file.readlines():
    left, rigth = list(map(int, line.split("  ")))
    lefts.append(left)
    rights.append(rigth)

lefts = quicksort(lefts)
rights = quicksort(rights)

distance = sum([abs(lefts[i]-rights[i]) for i in range(len(lefts))])
print(distance)