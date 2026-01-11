# decorator -function with parameter
# -------------------------------------
def mydecorator(func):
  def nested_func(n1,n2):
    print("before")
    func(n1,n2)
    print("after")
  return nested_func
# @mydecorator
# def hello():
#   print("hello")
# @mydecorator
# def calculate(n1,n2):
#   print(n1+n2)
# calculate(10,100)
def mydecorator2(confirm):
  def nestedconfirm(n11,n22):
    while True:
      try:
        float(n11)
        float(n22)
        break
      except ValueError:
        print("invaled value")
    confirm(n11,n22)
    print("true value")
def mycalculator1(n1,n2):
  n1=input("number1 : ")
  n2=input("number2 : ")

@mydecorator2
mycalculator1(n1,n2)


