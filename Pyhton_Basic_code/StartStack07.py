x=int(input("How many rows do you want? : "))
n=x
for i in range(1,x+2):
 j=" "*((i*2)-3)
 k="*"*n
 if i==1:
  print(k+"*"+k)
 else:
  print(k+"*"+j+"*"+k)
 n=n-1

"""
***************
******* *******
******   ******
*****     *****
****       ****
***         ***
**           **
*             *

"""