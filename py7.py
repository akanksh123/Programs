dicto={'john':85,'mark':90,'smith':100}

for i in sorted(dicto,reverse=True)[:2]:
    print(i,dicto[i])
sum=0
for i in dicto:
    sum+=dicto[i]
print(sum)