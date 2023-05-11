def sam(da,a,b):
    for i in range(a):
        la=[]
        for j in range(b):
            sa=da[j][i]
            la.append(sa)
        print(la)
a,b=map(int,input().split())
da=[]
for i in range(a):
    c=list(map(int,input().split()))
    da.append(c)
haa=sam(da,a,b)