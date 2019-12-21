stri=input("Enter a string")
letter=[]
pos=[]
for i in range(len(stri)):
    if stri[i].isupper():
        letter.append(stri[i])
        pos.append(i)
for i in range(len(letter)):
    print(letter[i]," ",pos[i])