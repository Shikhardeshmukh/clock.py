#factorial:
a = int(input("enter a no.:"))
fact = 1
for i in range(a,0,-1):
  fact =fact*i
print("result=",fact)