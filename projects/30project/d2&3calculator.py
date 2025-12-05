# we are going to make a simple calculator
print("welcome to our calvulator")
print("choose your operation")
print("1-add(+)\n2-subtract(-)\n3-miltiply(*)\n4-divide(/)")

while True:
  chooseoperation=input("whart is your operation 1,2,3 or 4 if u want to end enter 5 : ").strip()
  num1=int(input("enter first number : ").strip())
  num2=int(input("enter seconde number : ".strip()))
  if chooseoperation =="1":
    print(f"{num1}+{num2}={num1+num2}")

  elif chooseoperation =="2":
    print(f"{num1}-{num2}={num1-num2}")
  elif chooseoperation =="3":
    print(f"{num1}*{num2}={num1*num2}")
  elif chooseoperation =="4":
    print(f"{num1}/{num2}={num1/num2}")
  if chooseoperation =="5":
      break





  

