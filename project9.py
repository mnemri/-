x=int(input("Give me a number: "))
x=x*3+1
sum=0
while  x>=10 :
    while x >0:
        sum=sum+(x%10)
        x=x//10
    x=sum
    if x >= 10 :
        x=x*3+1
        sum=0
    else: break
print(x)