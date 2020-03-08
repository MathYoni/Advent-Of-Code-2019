f = open('day6.txt')
s = f.read().split()
t = []
for i in s:
    t.append(i.split(')'))

orbits = {}
for i in t:
    if i[1] not in orbits:
        orbits[i[1]] = [-1,0,[]]
orbits['COM'] = [0,0,orbits.keys()]

neg = True
while neg == True:
    for i in t:
        if orbits[i[0]] >= 0:
            orbits[i[1]][0] = orbits[i[0]][0] + 1
            orbits[i[0]][2].append(i[1])
            orbits[i[1]][1] = i[0]
            t.remove(i)
    if len(t) == 0:
        neg = False

orbsanta = []
point = 'SAN'
while point != 0:
    orbsanta.append(orbits[point][1])
    point = orbits[point][1]

intersect = False
point = orbits['YOU'][1]
distance = 0
while intersect == False:
    if point in orbsanta:
        distance += orbsanta.index(point)
        print(distance)
        intersect = True
    else:
        point = orbits[point][1]
        distance += 1




