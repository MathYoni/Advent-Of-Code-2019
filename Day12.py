### Used this exercise for practice with classes. Didn't end up being so helpful- dictionaries would have made things more clear. Left a lot of the code exceptionally clunky in this one. ###
from Day12_classes import Moon, Vector
f = open("day12.txt")
s = f.read().splitlines()
t = []
for i in s:
    r = []
    i = i.split()
    for j in i:
        j = int("".join([k for k in j if j.index(k) in range(j.index("=") + 1, len(j) - 1)]))
        r.append(j)
    t.append(r)

### Functions ###
def energy(moon):
    return (abs(moon.pos.x) + abs(moon.pos.y) + abs(moon.pos.z))*(abs(moon.vel.x) + abs(moon.vel.y) + abs(moon.vel.z))

def gravity(s,t):
    if s.pos.x > t.pos.x:
        s.vel.x -= 1
    elif s.pos.x < t.pos.x:
        s.vel.x += 1
    else:
        pass
    if s.pos.y > t.pos.y:
        s.vel.y -= 1
    elif s.pos.y < t.pos.y:
        s.vel.y += 1
    else:
        pass
    if s.pos.z > t.pos.z:
        s.vel.z -= 1
    elif s.pos.z < t.pos.z:
        s.vel.z += 1
    else:
        pass

### Code ###
Moons = []
Moons2 = []
for l in t:
    Moons.append(Moon(Vector(l[0], l[1], l[2]), Vector(0, 0, 0)))
    Moons2.append(Moon(Vector(l[0], l[1], l[2]), Vector(0, 0, 0)))
#for m in range(1000):
k=0
cycles = []
x_cyc = False
y_cyc = False
z_cyc = False

while len(cycles) < 3:
    k += 1
    for i in Moons:
        for j in Moons:
            gravity(i,j)
    for q in Moons:
        q.pos += q.vel
    if x_cyc == False and Moons[0].pos.x == Moons2[0].pos.x and Moons[1].pos.x == Moons2[1].pos.x and Moons[2].pos.x == Moons2[2].pos.x and Moons[3].pos.x == Moons2[3].pos.x and Moons[0].vel.x == Moons[1].vel.x == Moons[2].vel.x == Moons[3].vel.x == 0:
        cycles.append(k)
        x_cyc = True
    if y_cyc == False and Moons[0].pos.y == Moons2[0].pos.y and Moons[1].pos.y == Moons2[1].pos.y and Moons[2].pos.y   == Moons2[2].pos.y and Moons[3].pos.y == Moons2[3].pos.y and Moons[0].vel.y == Moons[1].vel.y == Moons[2].vel.y ==    Moons[3].vel.y == 0:
        cycles.append(k)
        y_cyc = True
    if z_cyc == False and Moons[0].pos.z == Moons2[0].pos.z and Moons[1].pos.z == Moons2[1].pos.z and Moons[2].pos.z   == Moons2[2].pos.z and Moons[3].pos.z == Moons2[3].pos.z and Moons[0].vel.z == Moons[1].vel.z == Moons[2].vel.z ==    Moons[3].vel.z == 0:
        cycles.append(k)
        z_cyc = True

print(cycles) ### plugged into an LCM calculator online ###

### Part 1 ###
#total = 0
#for Moon in Moons:
#    total += energy(Moon)
#print(total)
