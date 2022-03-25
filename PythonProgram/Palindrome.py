s=input()
s=s.lower()
x=''
for i in range (len(s)-1,-1,-1):
    x+=s[i]
print(x)
if(x==s):
    print('Palindrome')
else:
    print('Not Palindrome')