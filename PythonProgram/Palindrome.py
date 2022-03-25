s=input()
s=s.lower()
flag=0
for i in range(0,int(len(s)/2)):
    if(s[i]==s[len(s)-i-1]):
        flag=1
    else:
        flag=0
        break
if(flag==1):
    print('Palindrome')
else:
    print('Not Palindrome')