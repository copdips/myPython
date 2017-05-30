from gnuText import gnu as texte

# nb of chars
print()
print("nb of chars : ", len(texte))

# nb of symboles
print()
print("nb of symboles : ", len(set(texte)) )

# occurence of each symbole
print()
print("occurence of each symbole : ")
mySet = set(texte)

print("Method 1")
myDict = dict((d,0) for d in mySet)
for i in texte :
        myDict[i] += 1

print("myDict len :" , len(myDict))
print(myDict)

print()
print("Method 2")
myDict = dict((d,texte.count(d)) for d in mySet)

print()
print("myDict len :" , len(myDict))
print(myDict)

# for i in myDict :
#     print(i, " : ", myDict[i])

print()
print("occurence of each symbole in order : ")
myList = list(myDict.items())
# myList = list( (k, myDict[k]) for k in myDict.keys())

print("myList in ascending order by symboles in ascii")
myList.sort()
print(myList)

print()
print("myList in descending order by symboles in ascii")
myList.sort(reverse=True)
print(myList)

print()
print("myList in descending order by occurences of symbole")
myList.sort(key=lambda b : b[1], reverse=True)
print(myList)
