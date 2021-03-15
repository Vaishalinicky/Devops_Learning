x=int(input("How many rows do you want? : "))
l=x+1
for i in range(1,l):
 j="*"*i
 k=" "*((l-i)*2)
 print(j+""+k+""+j)
 
"""
*            *
**          **
***        ***
****      ****
*****    *****
******  ******