# decorators => intro
# -------------------------
# 1-sometimes called meta programing
# 2-every thing in python is object even function
# 3-decorator take a function and add some functionality and return it
# 4-decorateor wrao other functin and enhance their behaviour 
# 5-decorator is higher order function (function accept function as parameter)  
# -------------------------------------
def mydecorator(func):
  def nested_func():
    print("before")
    func()
    print("after")
  return nested_func



@mydecorator
def hello():
  print("hello")
# mydecorator_=mydecorator(hello)
# mydecorator_() # == @mydecorator
hello()
# --------------------------------------------
