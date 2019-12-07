f=open("day1.txt")
s=f.read().splitlines()
t=[]
for i in s:
    t.append(int(i))

fuel = []
for i in t:
    j=i
    fuel_j = 0
    while j >= 0:
        j = (j//3) - 2
        if j>=0:
            fuel_j += j
    fuel.append(fuel_j)

sum = 0
for i in fuel:
    sum += i

print(sum)
