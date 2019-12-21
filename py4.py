m1=open("./marks.txt","r")
m2=open("./keys.txt","r")
ans=[]
maxi=0
for key in m2:
    ans=key.split()
for mark in m1.readlines():
    count=0
    mark=mark.split()
    name=mark[0]
    for i in range(1,len(mark)):
        if(mark[i]==ans[i]):
            count=count+1
    print("name is ",name," score is ",count)
    if count>maxi:
        maxi=count
        maxname=name
print("name is ",maxname," score is ",maxi)