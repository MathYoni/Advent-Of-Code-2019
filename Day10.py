from fractions import Fraction
f = open("day10.txt")
r = f.read().split()

asteroids = {}
for i in range(len(r)):
    for j in range(len(r[0])):
        if r[i][j] == '#':
            asteroids[(j, i)] = []

for i in asteroids:
    for j in asteroids:
        if j != i:
            if len(asteroids[i]) == 0:
                asteroids[i].append(j)
            else:
                count = 0
                for k in asteroids[i]:
                    if j[0] == i[0]:
                        if k[0] == i[0] and abs(j[1]-k[1]) <= max(abs(j[1]-i[1]), abs(k[1]-i[1])):
                            break
                    elif j[1] == i[1]:
                        if k[1] == i[1] and abs(j[0]-k[0]) <= max(abs(j[0]-i[0]), abs(k[0]-i[0])):
                            break
                    elif (j[0]-i[0])*(k[1]-i[1]) == (j[1]-i[1])*(k[0]-i[0]):
                        if abs(j[1]-k[1]) <= max(abs(j[1]-i[1]), abs(k[1]-i[1])):
                            break
                    count += 1
                if count == len(asteroids[i]):
                    asteroids[i].append(j)

### Part Two ###
targets = asteroids.keys()
targets.remove((14,17))
slopes = {}

for i in targets:
    a = i[1] - 17
    b = i[0] - 14
    if i[0] == 14:
        if a > 0:
            if -99 in slopes:
                slopes[-99].append([i, abs(a)+abs(b),1])
            else:
                slopes[-99] = [[i,abs(a) + abs(b),1]]
        else:
            if -99 in slopes:
                slopes[-99].append([i,abs(a)+abs(b),0])
            else:
                slopes[-99] = [[i,abs(a) + abs(b),0]]
    else:
        slope = Fraction(a,b)
        if b > 0:
            if slope in slopes:
                slopes[slope].append([i,abs(a)+abs(b),0])
            else:
                slopes[slope] = [[i,abs(a) + abs(b),0]]
        else:
            if slope in slopes:
                slopes[slope].append([i,abs(a)+abs(b),1])
            else:
                slopes[slope] = [[i,abs(a) + abs(b),1]]

vaporized = []
ordslope = sorted(slopes.keys())
orient = 0
f=0
h=0
while f < 200:
    while h < len(ordslope) and f < 200:
        j = ordslope[h]
        if [i[2] for i in slopes[j]].count(orient) > 0:
            s = [i[1] for i in slopes[j] if i[2] == orient]
            k = min(s)
            for l in slopes[j]:
                if l[1] == k and l[2] == orient:
                    vaporized.append(l[0])
                    slopes[j].remove(l)
                    f += 1
                    break
        h += 1
    h = 0
    orient = (orient + 1) % 2

print(vaporized)
print(len(vaporized))
### Come up with a way to refer to all of the slopes. Currently you are counting integers, but need to do all rational slopes ###

### Part One ###
#asteroids2 = {}
#for i in asteroids:
#    asteroids2[len(asteroids[i])] = i
#
#plant = max(asteroids2.keys())
#print(plant, asteroids2[plant])
### Answer (260, (14, 17)) ###
