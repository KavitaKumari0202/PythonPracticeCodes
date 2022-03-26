arr=[-2,1,-3,4,-1,2,1,-5,4]
lst=[]
max_sum=0
start,end=0,0
s=0
for i in range(len(arr)):
    s+=arr[i]
    if s<0:
        s=0
        #lst=[]
    elif s>max_sum:
        max_sum=s
        #lst.append(arr[i])
print(max_sum)
#print(lst)