import sys
a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
c=int(sys.stdin.readline())

if (a==60)and(b==60)and(c==60):
    print("Equilateral")
elif (a+b+c)!=180:
    print("Error")
else:
    if(a==b)or(b==c)or(c==a):
        print("Isosceles")
    else:
        print("Scalene")

