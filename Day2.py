f=open("day2.txt")
r=f.read().split(",")
t=[]
for i in r:
    t.append(int(i))

def changecode(t,i,j):
    s = t[:]
    s[1] = i
    s[2] = j
    counter = 0
    while counter < len(s):
        opcode=[]
        for i in range(4):
            opcode.append(s[counter+i])

        if opcode[0] == 1:
            s[opcode[3]] = s[opcode[1]] + s[opcode[2]]
        elif opcode[0] == 2:
            s[opcode[3]] = s[opcode[1]] * s[opcode[2]]
        else:
            counter = len(s) + 1

        counter += 4

    return s[0]

for i in range(100):
    for j in range(100):
        if changecode(t,i,j) == 19690720:
            print( i, j, (i*100)+j)

