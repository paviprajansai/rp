y11=input()
z11=0
for i in range(0,len(y11)):
  if y11[i].isalnum()==False and y11[i]!=" ":
    z11=z11+1
print(z11)
