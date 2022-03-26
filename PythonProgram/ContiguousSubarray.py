arr=[-2,1,-3,4,-1,2,1,-5,4]
subarr=[]
s=0
x=max(arr)
lst=[]
for i in range(0,len(arr)+1):
    for j in range(i):
        lst.append(arr[j:i])
print(lst)

for i in lst:
    s=sum(i)
    if(s>x):
        x=s
        subarr=i
    else:
        pass
print(x,subarr)