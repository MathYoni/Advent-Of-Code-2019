f=open("day8.txt")
s=f.read().split()
t=[]
for i in s[0]:
    t.append(int(i))

divider = 0
layers = []
grid = [ [] for i in range(150)]

while (divider+1) * 150 <= len(t):
    newlayer = []
    for j in range(150):
        current = divider * 150 + j
        newlayer.append(t[current])
        grid[j].append(t[current])
    layers.append(newlayer)
    divider += 1

image = []

for i in grid:
    for j in i:
        if j == 0:
            image.append(' ')
            break
        elif j == 1:
            image.append('x')
            break
        else:
            continue

for i in range(6):
    row = [image[j + (i * 25)] for j in range(25)]
    print(row)

### Part 1 ###
#zeroes = []
#for i in layers:
#    zeroes.append(i.count(0))
#
#print(layers[zeroes.index(min(zeroes))].count(1)*layers[zeroes.index(min(zeroes))].count(2))
