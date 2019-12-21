fib1=0
fib2=1
n=int(input("Enter n"))
if n==0:
    print("enter valid value")
elif(n==1):
    print(fib1,end=" ")
elif(n==2):
    print(fib1," ",fib2)
else:
    

    print(fib1," ",fib2,end=" ")
    i=2
    while(i<n):
        fib3=fib1+fib2
        print(fib3,end=" ")
        fib1=fib2
        fib2=fib3
        i=i+1
    
