class Account:
    def __init__(self,accno,balance):
        self.__accno=accno
        self.__balance=balance
    def withdraw(self,bal):
        if(bal>self.__balance):
            print("Insufficient balance")
        else:
            self.__balance=self.__balance-bal
            print("balance withdawed")
    def deposit(self,bal):
        self.__balance=self.__balance+bal
        print("Deposited successfully")
    def getbalance(self):
        return (self.__balance)
    def getaccount(self):
        return self.__accno
def check(lst,accno):
    flag=0
    for i in lst:
        if(i.getaccount()==accno):
            flag=1
            break
    if flag==0:
        return None
    else:
        return i        
acc=[]

while(True):
    ch=int(input("enter your choice"))
    if ch==1:
        accno=int(input("enter the accno"))
        if check(acc,accno)!=None:
            print("Account already exists")
        else:
            bal=int(input("Enter the balance"))
            acc.append(Account(accno,bal))
       
    elif ch==2:
        accno=int(input("enter the accno2"))
        getacc=check(acc,accno)
        if getacc==None:
            print("Account doesnt exist")
        else:
            bal=int(input("Enter balance to be withdrawn"))
            getacc.withdraw(bal)
    elif ch==3:
        accno=input("enter the accno3")
        for i in acc:
            if(accno==i.getaccount()):
                bal=int(input("Enter balance to be deposited"))
                acc[i].deposit(bal)
            else:
                print("Account does not exists")
    elif ch==4:
        acc=sorted(acc,key=Account.getbalance,reverse=True)
        print("Account with highest balance is ",acc[0].getaccount()," with balance ",acc[0].getbalance())
    elif ch==5:
        exit()
