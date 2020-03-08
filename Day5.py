f = open("day5.txt")
t = f.read().rstrip()
s = [int(i) for i in t.split(',')]
#s=[3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
def codewrite(counter, s):
    code = [0,0,0,0]
    firstnum = [0,0,0,0,0]
    for i in range(4):
        firstnum[i] = (s[counter]/(10**(i))) % 10
    code[0] = firstnum[0]
    if code[0] == 3 or code[0] == 4:
        code[1] = s[counter + 1]
    elif code[0] == 9:
        pass
    else:
        for j in range(2):
            if firstnum[j+2] == 0:
                code[j+1] = s[s[counter + j + 1]]
            else:
                code[j+1] = s[counter + j + 1]
        code[3] = s[counter + 3]
    return code

counter = 0
while counter < len(s):
    opcode = codewrite(counter, s)
    if opcode[0] == 1:
        s[opcode[3]] = opcode[1] + opcode[2]
        counter += 4
    elif opcode[0] == 2:
        s[opcode[3]] = opcode[1] * opcode[2]
        counter += 4
    elif opcode[0] == 5:
        if opcode[1] != 0:
            counter = opcode[2]
        else:
            counter += 3
    elif opcode[0] == 6:
        if opcode[1] == 0:
            counter = opcode[2]
        else:
            counter += 3
    elif opcode[0] == 7:
        if opcode[1] < opcode[2]:
            s[opcode[3]] = 1
        else:
            s[opcode[3]] = 0
        counter += 4
    elif opcode[0] == 8:
        if opcode[1] == opcode[2]:
            s[opcode[3]] = 1
        else:
            s[opcode[3]] = 0
        counter += 4
    elif opcode[0] == 9:
        break
    elif opcode[0] == 3:
        s[opcode[1]] = 5
        counter += 2
    elif opcode[0] == 4:
        print(s[opcode[1]])
        counter += 2
