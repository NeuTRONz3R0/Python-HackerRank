#GIVEN A LIST OF INTEGERS
#FIND THE MID ELEMENT AMONG ALL THE POSITIVE INTEGERS
n = list(map(int, input("Type number with space: ").split()))
b = [i for i in n if i>= 0]
print(b)

mid = float(len(b)-1)/2
if mid%2 !=0:
  print(b[int(mid-.5)])
else:
  print(b[int(mid)],b[int(mid-1)])
