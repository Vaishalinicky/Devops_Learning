x=int(input("How many rows do you want? : "))
n=x
for i in range(1,x+1):
 j=" "*(i*2)
 k="*"*n
 print(k+""+j+""+k)
 n=n-1
 
"""
******  ******
*****    *****
****      ****
***        ***
**          **
*            *

"""