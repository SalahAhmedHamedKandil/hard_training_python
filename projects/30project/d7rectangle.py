
print("-- rectangle area calcultor --")
while True:
  print("\n1 : to calculate and continue")
  print("2 : to close")
  choose=input("please enter your choice : ")
  while choose not in ("1","2"):
    print("please choose from 1 , 2 :")
    choose=input("please enter your choice : ")

  if choose =="1":
    while True:
      try:
        width=float(input("1:enter the width : ").lower())
        if width < 0:
          print("enter positive number")
          continue
        lenth=float(input("2:enter the lenth : ").lower())
        if lenth < 0:
          print("enter positive number")
          continue
        break
      except ValueError:
        print("please enter integer or float number")
    print(f"\nthe result is {width*lenth}\n")
    print("_-"*15)
  elif choose == "2":
    print("thank u for using our app")
    break