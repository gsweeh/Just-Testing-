n=int(input("enter a number"))
isFibonacci=False
a,b=0,1
while(b<=n):
    a,b=b,a+b
if a==n:
    isFibonacci=True
if isFibonacci:
    print(n,"is a Fibonacci number")
else:
    print(n,"is not a fibonacci number")
