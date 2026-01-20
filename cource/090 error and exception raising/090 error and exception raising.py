# 090 error and exception raising
x=10
if x <0:
  print(f"the number {x} is less than 0 ")
else:
  print(f"the {x} is more than 0")
print(" message after if condition")
# --------------------------------

# raise exception
b=-10
if b <0:
  raise Exception (f"the number {b} is less than 0 ") #program will not continue to operate and stop here 

else:
  print(f"the {b} is more than 0")
print(" message after if condition")
# output
#   File "d:\elzero_python\cource\090 error and exception raising\090 error and exception raising.py", line 12, in <module>
#     raise Exception (f"the number {b} is less than 0 ")
# Exception: the number -10 is less than 0 
# -----------------------------------------------------------