import sys
num=int(sys.stdin.readline())
for i in range(num):
    a,b=map(int,sys.stdin.readline().split())
    print("Case #"+str(i+1)+": "+str(a+b))