h=int(input())
while(h>0):
  d=[]
  c=[]
  ai=[]
  a,b=map(int,input().split())
  d=list(map(int,input().split()))
  nd=list([x for x in range(1,a+1)])
  nd=[i for i in nd if i not in d]
  for j in range(0,len(nd),2):
    c.append(nd[j])
  ai=[j for j in nd if j not in c]
  h-=1
  print(*c,sep=" ")
  print(*ai,sep=" ")
  
  
