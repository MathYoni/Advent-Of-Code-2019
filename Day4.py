def codecheck(bottom,top):
    goodcodes=[]
    for i in range(top-bottom+1):
        icopy = str(i+bottom)
        ilist = [int(j) for j in icopy]
        j = 0
        nondecr = True
        duplicate = False
        while j < len(ilist) - 1:
            if ilist[j] > ilist[j+1]:
                nondecr = False
            if ilist[j] == ilist[j+1]:
                if (j < len(ilist) - 2 and ilist[j+1] == ilist[j+2]) or (j > 0 and ilist[j-1] == ilist[j]):
                    pass
                else:
                    duplicate = True
            j+=1
        if nondecr == True and duplicate == True:
            goodcodes.append(i)

    return len(goodcodes)

print(codecheck(265275,781584))
