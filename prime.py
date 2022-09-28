n=12
result=0
for x in range(2,n-1):
    if n%x==0:
        result=1
        break

if result==0:
    print("Prime No")

else:
    print("Non Prime")
