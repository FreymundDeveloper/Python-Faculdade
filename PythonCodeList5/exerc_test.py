t=[-10,-8,0,1,2,3,-2,-4]
me=-10
ma=3
md=0
c=0

while c < len(t):
    if t[c] > me:
        me=t[c]
    if t[c] < ma:
        ma=t[c]
    md=md+t[c]
    c+=1

print('me=', ma)
print('ma=',me)
print('med=', md/len(t))
