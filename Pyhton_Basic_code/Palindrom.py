x=input("Enter any String : ")
y = len(x)
a,b=0,2
m=0
#print("length of string =" , y)
for i in range(y):
  while b<=y:
    j=x[a:b]
    #print(j)
    k=j[::-1]
    #print(k)
    if j==k:
      m=m+1
    a=a+1
    b=b+1
  b=i+3
  a=0
print("palindrom count is : " , m+y)
    