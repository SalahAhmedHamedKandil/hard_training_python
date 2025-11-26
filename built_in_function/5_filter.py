# built in function => filter
# -------------------
# 1-filter takes a function + iterator
# 2-filter run a function on every element
# 3-the function can be pre-defined function or lambda fuction 
# 4-filter out all elements for which the function return true
# 5-the fuction need to return boolean value
# --------------------
def formaeText(text):
  return f"- {text} -"

myText=["salah","ahmed","hamed"]
myFormatedData=filter(formaeText,myText)
print(myFormatedData)
for name in myFormatedData:
  print(name)
print("-_"*10)



