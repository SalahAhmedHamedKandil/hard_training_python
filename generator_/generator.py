# generator
# -----------------------
# 1 - generator is a function with 'yield' keyword insted of 'return'
# 2 - it suport   


salah=("salah ahmeh")
def myGenerator():
  yield 1
  yield 2
  yield 3
  yield 4
  yield 5
  yield 6
  yield salah
  yield ("salah")
print(myGenerator)
myGen=myGenerator()
print(next(myGen)) # => 1
print(next(myGen)) # => 2
print(next(myGen)) # => 3
print(next(myGen)) # => 4
print(next(myGen)) # => 5
print(next(myGen)) # => 6
print(next(myGen)) # => salah
print(next(myGen)) # => salah ahmed
