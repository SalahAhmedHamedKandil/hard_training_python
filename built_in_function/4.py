# built in function => map
# ?--------------------
# 1 - map take a function + iterator
# 2 - the function van be pre-defined function or lambda function
# ------------------------------------

# def formaeText(text):
#   return f"- {text} -"

# myText=["salah","ahmed","hamed"]
# myFormatedData=map(formaeText,myText)
# print(myFormatedData)
# for name in myFormatedData:
#   print(name)
# print("-_"*10)
# # # output
# # - salah -
# # - ahmed -
# # - hamed -
# -------------------------
myText=["salah","ahmed","hamed"]
for name in map(lambda text:  f"- {text.strip().capitalize()} -",myText):
  print(name)
# output
# - Salah -
# - Ahmed -
# - Hamed -