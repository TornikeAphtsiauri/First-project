# ლექსიკონის შექმნა
md = {}
dn=int(input("input number fo pairs in dictionary "))
i=0
while i<dn:
    md[i] = input("input value of dictionary ")
    i+=1
#ლექსიკონის ბეჭდვა
print("Dictionary", md)
#მინიმალური მაჩვენებელი
mv= min(md.values())
#შედეგის ბეჭდვა
print ("minimum value ", mv)