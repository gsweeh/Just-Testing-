print("enter a value of a,b,c")
a,b,c=int(input()),int(input()),int(input())
x=(-b+(b-4*a*c)**0.5)/2*a
y=(-b-(b-4*a*c)**0.5)/2*a
print("roots are:",x,"and",y)