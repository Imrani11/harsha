# Create set difference
set1 = set(['green','blue'])
set2 = set(['blue','yellow'])
print("Original sets")
print(set1)
print(set2)
res1 = set1.difference(set2)
print("Difference of set1-set2",res1)
res2 = set2.difference(set1)
print("Difference of set2-set1",res2)