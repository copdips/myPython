import re

suffrages = "besancenot 1498581 buffet 707268 schivardi 123540 bayrou 6820119 bové 483008 voynet 576666 villiers 818407 royal 9500112 dominique de villepinfdgfdgdsfgdfsgfsd 0  nihous 420645 le-pen 3834530 laguiller 487857 sarkozy 11448663"

suffragesNew = re.sub(r"(\d)\s+(\D)", r'\1:\2', re.sub(r"(\D)\s+(\d)", r'\1:\2', suffrages))
print()
print("suffragesNew:")
print(suffragesNew)


suffragesTable = suffragesNew.split(":")

suffragesLength = len(suffragesTable)

suffragesDictValue = dict( (suffragesTable[k].strip(), int(suffragesTable[k+1])) for k in range(0, suffragesLength, 2) )


print()
print("suffragesDictValue :")
print(suffragesDictValue)


suffragesSum = sum(suffragesDictValue.values())
print()
print("suffragesSum :")
print(suffragesSum)

suffragesDictPercentage = dict( (k,  '{:.2%}'.format(suffragesDictValue[k]/suffragesSum)) for k in suffragesDictValue.keys())
print()
print("suffragesDictPercentage :")
print(suffragesDictPercentage)

def printStars(percentage) :
    res = "*" * int(float(percentage.strip("%"))//0.6)
    if percentage != '0.00%' and res == '' :
        res = "*"
    return res

suffragesDictHistogramme = dict( (k + ":" + suffragesDictPercentage[k] , printStars(suffragesDictPercentage[k])) for k in suffragesDictPercentage.keys())
print()
print("suffragesDictHistogramme :")
print(suffragesDictHistogramme)

print()
print("suffragesDictHistogramme view :")

nameList = list(len(l.split(":")[0]) for l in suffragesDictHistogramme.keys() )
maxString = max(nameList)
print()
print("maxString:")
print(maxString)
print()

shiftMaxStringFormat = '{:' + str(maxString) + '}'
print()
print("shiftMaxStringFormat:")
print(shiftMaxStringFormat)
print()

for i in suffragesDictHistogramme.keys() :
    suffragesDictNameAndPercentage = i.split(":")
    name = suffragesDictNameAndPercentage[0]
    percentage = suffragesDictNameAndPercentage[1]
    if len(percentage) == 5 : percentage = " " + percentage
    stars = suffragesDictHistogramme[i]

    print(shiftMaxStringFormat.format(name), "\t(", percentage, ") :\t", stars)

print()
print("END OF SCRIPT")