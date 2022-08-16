import squareroot
print("importing module")
a=int(input('given value of a='))
b=int(input('given value of b='))
c=int(input('given value of c='))
#find the two resuts of square root
x=-b-squareroot.square_root(a,b,c)/(2*a)
y=-b+squareroot.square_root(a,b,c)/(2*a)
print("The quadratic equation of solution 1=",x)
print("The quadratic equation of solution 2=",y)      
