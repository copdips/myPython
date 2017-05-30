suffrages = "buffet 707268 bove 483008 voyne 576666"

suffragesTable = suffrages.split(" ")

suffragesLength = len(suffragesTable)

suffragesDictValue = dict( (suffragesTable[k], int(suffragesTable[k+1])) for k in range(0, suffragesLength, 2) )


print()
print("suffragesDictValue")
print(suffragesDictValue)


suffragesSum = sum(suffragesDictValue.values())
print()
print("suffragesSum")
print(suffragesSum)

suffragesDictPercentage = dict( (k,  '{:.2%}'.format(suffragesDictValue[k]/suffragesSum)) for k in suffragesDictValue.keys())
print()
print("suffragesDictPercentage")
print(suffragesDictPercentage)

def printStars(percentage) :
    res = "*"
    for i in range(percentage//0.006) :
        res += "*"
    return res

suffragesDictHistogramme = dict( (k + " " + suffragesDictPercentage[k] , printStars(suffragesDictPercentage[k])) for k in suffragesDictPercentage.keys())
print()
print("suffragesDictHistogramme")
print(suffragesDictHistogramme)