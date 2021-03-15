x=int(input("How many rows do you want? : "))
l=x+1
a=1
for i in range(1,l):
 j="*"*a
 k=" "*(l-i)
 print(k+""+j)
 a=a+2
 
#     *
#    ***
#   *****
#  *******
# *********