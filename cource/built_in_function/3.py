# built in function
# -----------------
# abs()
# pow()
# min()
# max()
# slice()
# -----------------

# abs() abs = absolute value of the enter number
# abs() the distance between the number and zwero
print(abs(100))       # => 100
print(abs(-100))      # => 100
print(abs(10.90))     # => 10.90
print(abs(-10.90))    # => 10.90

print("-_"*20) 
# ------------------------------
# pow(base,exp,mod)   pow => power of the number
print(pow(2,5))     # => 32
print(pow(2,5,10))  # => 2

print("-_"*20) 
# ----------------------------
#  min(item,item,item,or iterator)
print(min(1,2,3,4,5,6,0))   # => 0
print(min("ahmed","salah","aa"))   # => aa

print("-_"*20) 
# ------------------------
#  max(item,item,item,or iterator)
print(max(1,2,3,4,5,6,0))   # => 6
print(max("ahmed","salah","aa"))   # => salah
print("-_"*20) 
# -------------------------
# slice()
a=["a","b","c","d","e","f"]
print(a[:5])            # => ['a', 'b', 'c', 'd', 'e']
print(a[slice(5)])      # => ['a', 'b', 'c', 'd', 'e']
print(a[:5:2])          # => ['a', 'c', 'e']
print(a[slice(0,5,2)])  # => ['a', 'c', 'e']
print(a[slice(2,5)])    # => ['c', 'd', 'e']



