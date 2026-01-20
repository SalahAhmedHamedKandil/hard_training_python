

list1=[11,"22",33]
tuple1=(1,2,3)
for item1,item2 in zip(list1,tuple1):
  print(item1,item2)
# output
# 11 1
# 22 2
# 33 3
# # ------------------------------------
list1=[11,"22",33]
tuple1=(1,2,3)
dict_={"salah":28,"ahmed":63}
for item1,item2,item3 in zip(list1,tuple1,dict_):
  print(item1,item2,item3,dict_[item3])
# output
# 11 1 salah 28
# 22 2 ahmed 63
# ------------------------------------
