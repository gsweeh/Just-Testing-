arr=[]
size=int(input("enter size"))
for x in  range(size):
    arr.append(int(input("enter element"+str(x+1)+".")))
n=int(input("enter a element to be searched"))
for i in range(size):
    if arr[i]==n:
        print(n,"found at index",i)
        break
else:
    print("element does not exist")