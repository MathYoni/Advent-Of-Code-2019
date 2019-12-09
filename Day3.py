f = open("day3.txt")
s = f.read().split()
sfirst = s[0]
stwo = s[1]
sfirst = sfirst.split(",")
stwo = stwo.split(",")
path1 = []
path2 = []
for i in sfirst:
    j =  int(i[1:])
    path1.append([i[0],j])
for i in stwo:
    j = int(i[1:])
    path2.append([i[0],j])

path1points = [(0,0)]
counter = 0
for i in path1:
    if i[0] == "U":
        for j in range(i[1]):
            path1points.append((path1points[counter][0],path1points[counter][1]+j+1))
        counter += i[1]
    if i[0] == "D":
        for j in range(i[1]):
            path1points.append((path1points[counter][0], path1points[counter][1]-j-1))
        counter += i[1]
    if i[0] == "L":
        for j in range(i[1]):
            path1points.append((path1points[counter][0] - j - 1,path1points[counter][1]))
        counter += i[1]
    if i[0] == "R":
        for j in range(i[1]):
            path1points.append((path1points[counter][0]+j+1,path1points[counter][1]))
        counter += i[1]

counter = 0
path2points= [(0,0)]
for i in path2:
     if i[0] == "U":
         for j in range(i[1]):
             path2points.append((path2points[counter][0],                        path2points[counter][1]+j+1))
         counter += i[1]
     if i[0] == "D":
         for j in range(i[1]):
             path2points.append((path2points[counter][0],     path2points[counter][1]-j-1))
         counter += i[1]
     if i[0] == "L":
         for j in range(i[1]):
             path2points.append((path2points[counter][0] - j - 1,                path2points[counter][1]))
         counter += i[1]
     if i[0] == "R":
         for j in range(i[1]):
             path2points.append((path2points[counter][0]+j+1,  path2points[counter][1]))
         counter += i[1]

path2pointset = set(path2points)
path1pointset = set(path1points)
crossings = path1pointset.intersection(path2pointset)
crossings.remove((0,0))
crossingsum = []
for i in crossings:
    crossingsum.append(path2points.index(i) + path1points.index(i))

print(min(crossingsum))
#norms = []
#for i in crossings:
#    norms.append(abs(i[0])+abs(i[1]))

#print(min(norms))
