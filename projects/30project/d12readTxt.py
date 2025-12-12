import os
with open("write.txt","r")as f:
  read=f.readlines()
  for l in read:
    print(l)
print(read)