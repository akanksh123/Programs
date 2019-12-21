class country:
    def __init__(self,count,cap,population):
        self.count=count
        self.cap=cap
        self.population=population
    def getcap(self):
        return self.cap
    def getpop(self):
        return self.population
    def getcount(self):
        return self.count
lst=[]
def getcapital(co):
    flag=0
    for i in lst:
        
        if(i.getcount()==co):
            flag=1
            break
        
    if(flag==1):
        return i
    else:
        return False
while(True):
    ch=int(input("enter your choice"))
    if ch==1:
        count=input("Enter the country")
        if not getcapital(count):
            lst.append(country(count,input("enter capital"),int(input("enter population"))))
        else:
            print("Country already exists")
    elif ch==2:
        count=input("Enter the country")
        val=getcapital(count)
        if not val :
            print("Country doesnt exist")
        else:
            print("capital is ",val.getcap()," population is ",val.getpop())
    elif ch==3:
        lst=sorted(lst,key=country.getpop,reverse=True)
        print("max pop country is ",lst[0].getcount()," population is ",lst[0].getpop())
    elif ch==4:
        exit()


