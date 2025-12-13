

def myGenerator():
  yield 1
  yield 2
  yield 3
  yield 4
  yield 5
  yield 6
print(myGenerator)
myGen=myGenerator()
print(next(myGen))
print(next(myGen))
print(next(myGen))
print(next(myGen))
print(next(myGen))
print(next(myGen))
