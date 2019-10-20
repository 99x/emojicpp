for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    count=1
    for i in range(n-1):
        if(a[i]>a[i+1]):
            count+=1
        else:
            a[i+1]=a[i]
    
    print(count)
    
