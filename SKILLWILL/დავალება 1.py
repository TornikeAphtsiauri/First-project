# Dictionary
md = {}
dn=int(input("input number fo pairs in dictionary "))
i=0
# Adding the key value pair
while i<dn:
    md[i] = input("input value of dictionary ")
    i+=1

print("Dictionary", md)

mv= min(md.values())

print ("minimum value ", mv)