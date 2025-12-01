# built in function => filter
# -------------------
# 1-filter takes a function + iterator
# 2-filter run a function on every element
# 3-the function can be pre-defined function or lambda fuction 
# 4-filter out all elements for which the function return true
# 5-the fuction need to return boolean value
# --------------------
mynames=["salah","ahmed","hamed","amer","samy"]
def formate_name(name):
  return name.startswith("a") 
my_formate_name=filter(formate_name,mynames)
print(my_formate_name)
for name in my_formate_name:
  print(name)
print("-_"*10)

# --- output ----
    # ahmed
    # amer



for name in filter(lambda name : name.startswith("a") or ("s")  ,mynames):
  print (name.capitalize())  #we used or
# # # output
#   # Salah
#   # Ahmed
#   # Hamed
#   # Amer
#   # Samy
# ---------------------
students=[("salah",40),
          ("ahmed",50),
          ("hamed",60)]
passed=list(filter(lambda x:x[1]>=50,students))
print(passed)
# output
# [('ahmed', 50), ('hamed', 60)]
for p in list(filter(lambda x:x[1]>=50,students)):
  print(f"-- {p} --")
  # output
  # -- ('ahmed', 50) --
  # -- ('hamed', 60) --
print("_-"*10)
# ----------------------
products=[{"name":"mouse","price":90},
          {"name":"keyboard","price":100},
          {"name":"monitor","price":101}
          ]


moreexpensive99=list(filter(lambda p:p["price"]>99,products))
print (moreexpensive99)
# output
# [{'name': 'keyboard', 'price': 100}, {'name': 'monitor', 'price': 101}]
for p in list(filter(lambda p:p["price"]>99,products)):
  for k,v in p.items():
    print(f"{k},{v}")
