
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
        width=float(input("1:enter the width : ").strip())
        if width < 0:
          print("enter positive number")
          continue
        length=float(input("2:enter the length : ").strip())
        if length < 0:
          print("enter positive number")
          continue
        break
      except ValueError:
        print("Please enter a valid numeric value.")
    print(f"\nthe area of the rectangle is : {width*length}\n")
    print("_-"*15)
  elif choose == "2":
    print("thank u for using our app")
    break