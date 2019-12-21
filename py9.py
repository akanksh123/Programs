vow={'a':0,'e':0,'i':0,'o':0,'u':0}
stri=input("Enter a string")
for i in stri.lower():
    if i in 'aeiou':
        vow[i]=vow[i]+1

for i in vow:
    print(i," ",vow[i])

