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

Moons = []
for l in t:
    Moons.append(Moon(Vector(l[0], l[1], l[2]), Vector(0, 0, 0)))

for m in range(1000):
    for n in Moons:
        for p in Moons:
            gravity(n,p)
    for q in Moons:
        q.pos += q.vel

total = 0
for Moon in Moons:
    total += energy(Moon)

print(total)
