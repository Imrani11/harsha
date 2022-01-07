#  remove an item from a tuple
num = [10,20,2,3,4,5,3]
for i in num:
    if i >= 5:
        i.remove()
    print(i)
