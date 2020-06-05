from math import ceil
f = open("day14.txt").read()
s = f.splitlines()
t = []
for i in s:
    t.append(i.split("=>"))
q = []
for i in t:
    q.append([i[0].split(","),i[1]])
r = []
for i in q:
    a = []
    for j in i[0]:
        k = j.split()
        k[0] = int(k[0])
        a.append(tuple(k))

    b = i[1].split()
    b[0] = int(b[0])
    r.append([a,tuple(b)])
Reactions = {}
for i in r:
    Reactions[i[1][1]] = [i[1][0], i[0], 0] #key is product, value is list where first thing is amount of product, second is list of reactants (with amounts), third is 0
Reactions['ORE'] = [1, [], 0]
Bases = {'A': [2,9,0], 'B': [3,8,0], 'C': [5,7,0]}
#Bases = {'CXRVG': [1, 144, 0], 'GMFW': [7, 100, 0], 'GXNL': [4, 140, 0]}

### FUNCTION ###
def OreCount(Product, Amount):
    if Product == 'ORE':
        return Amount
    else:
        total = 0
        ChemNew = max(0, Amount - Reactions[Product][2])
        Reactions[Product][2] = max(0, Reactions[Product][2] - Amount)
        multiplier = int(ceil(ChemNew / float(Reactions[Product][0])))
        Reactions[Product][2] += (multiplier * Reactions[Product][0]) - ChemNew
        for i in Reactions[Product][1]:
            total += OreCount(i[1], multiplier * i[0])
        return total

def FuelCount(Ore):
    orevals = {}
    fuelone = 0
    fueltwo = Ore
    fuelnew = Ore/2
    while fuelnew != fuelone and fuelnew != fueltwo:
        a = OreCount('FUEL', fuelnew)
        orevals[a] = fuelnew
        if a > Ore:
            fueltwo = fuelnew
            fuelnew = fuelone + ((fueltwo - fuelone) / 2)
        elif a < Ore:
            fuelone = fuelnew
            fuelnew = fuelone + ((fueltwo - fuelone) / 2)
        else:
            print("hello")
            print(fueltwo)
            break
        for i in Reactions:
            Reactions[i][2] = 0

    b = min([Ore - i for i in orevals if i < Ore])
    return Ore - b, orevals[Ore - b]

print(FuelCount(1000000000000))


