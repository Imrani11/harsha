import string
def ispan(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True

str = 'aaaaaaaaaaaaaaaaaaaaaaaaaa'
print(len(str))
if(ispan(str) == True):
    print("yes")
else:
    print("No")
