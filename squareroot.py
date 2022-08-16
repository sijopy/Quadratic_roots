def square_root(a,b,c):
    d=b**2-4*a*c
    print(d)
    return d
a=int(input("a value is ="))
b=int(input('b value is ='))
c=int(input('c value is ='))
print("b^2-4ac =",square_root(a,b,c))
