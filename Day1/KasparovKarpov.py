KasparovKarpov = "1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 O-O 9. h3 Bb7 10. d4 Re8 11. Nbd2 Bf8 12. a4 h6 13. Bc2 ed4 14. cd4 Nb4 15. Bb1 c5 16. d5 Nd7 17. Ra3 c4 18. Nd4 Qf6 19. N2f3 Nc5 20. ab5 ab5 21. Nb5 Ra3 22. Na3 Ba6 23. Re3 Rb8 24. e5 de5 25. Ne5 Nbd3 26. Ng4 Qb6 27. Rg3 g6 28. Bh6 Qb2 29. Qf3 Nd7 30. Bf8 Kf8 31. Kh2 Rb3 32. Bd3 cd3 33. Qf4 Qa3 34. Nh6 Qe7 35. Rg6 Qe5 36. Rg8 Ke7 37. d6 Ke6 38. Re8 Kd5 39. Re5 Ne5 40. d7 Rb8 41. Nf7"

KasparovKarpovTable =  KasparovKarpov.split(" ")
kLength = len(KasparovKarpovTable)
r=""
for i in range(1, kLength+1, 3):
    r = r + " " + KasparovKarpovTable[i]

print("Kasparov only")
print(r.strip())
print("")

# method 2
print("Kasparov only")
print(KasparovKarpovTable[1::3])
print("")

print("Karpov only")
print(KasparovKarpovTable[2::3])
print("")

# liste inversée des déplacements : Nf7, Rb8 ... e5 e4
print("Reverse")
tableWithoutSeqMethod1 = [KasparovKarpovTable[i] for i in range(kLength) if i%3 != 0]
tableWithoutSeqMethod2 = [ i for i in KasparovKarpovTable if not i[:-1].isdigit() ]
tableWithoutSeqMethod3 = [ i for i in KasparovKarpovTable if not i.strip(".").isdigit() ]
tableWithoutSeqMethod4 = [ i for i in KasparovKarpovTable if not "." in i ]


tableWithoutSeqMethod1.reverse()
# tableWithoutSeqMethod1[::-1]

tableWithoutSeqMethod2.reverse()
tableWithoutSeqMethod3.reverse()
tableWithoutSeqMethod4.reverse()

print("Method 1")
print(tableWithoutSeqMethod1)

print("Method 2")
print(tableWithoutSeqMethod2)

print("Method 3")
print(tableWithoutSeqMethod3)

print("Method 4")
print(tableWithoutSeqMethod4)

print("")

print(tableWithoutSeqMethod1 == tableWithoutSeqMethod2)
print(tableWithoutSeqMethod1 == tableWithoutSeqMethod3)
print(tableWithoutSeqMethod1 == tableWithoutSeqMethod4)

print("")
