# we are goin to read information from "read.txt"

# open read.txt
import os

with open ("read.txt","r") as file:
  all_info=file.read()
  print(all_info) # print all file as one tring 
  print("-_"*9)

# ---------------------------------

with open ("read.txt","r") as file:
  for line in file :
    print(f"line {line.strip()}")
  print("-_"*9)

# ---------------------------------
with open ("read.txt","r") as file:
   for lines in file.readlines():
     print(lines)
   print("-_"*9)

#----------------------------------

with open ("read.txt","r") as file:
 for line in file :
  line = line.strip()
  if "=" in line:
    key,value=line.split("=",1)
    print(f"{key} = {value}")

   

