t=int(input())
c=0
while t:
    t=t-1
    s=str(input())
    z=len(s)
    a=(s.count("1",0,z))
    if a%2==1:
        print("WIN")
    else:
        print("LOSE")
    
