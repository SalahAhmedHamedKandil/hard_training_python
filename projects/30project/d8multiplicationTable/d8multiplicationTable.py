# multiplication table generator
print("Welcome")
print("This program will generate a multiplication table for any number you enter.")
print("-"*40)

while True:
  print("enter 1 to generate a multiplication tabl .")
  print("enter 0 to close .")
  choose=input("enter your choice : ").strip()
  while choose not in ("1","0"):
    print("unavalable choice.choose 1 or 0")
    choose=input("enter your choice :").strip()
  if choose =="1":
    while True:
      try:
        numb=float(input("enter number : ").strip())
        if numb<0:
          print("please enter positive number")
          continue
        break
      except ValueError:
        print("Please enter a valid numeric value.")
  if choose =="0":
    print("thank u for using our app")
    break
  multiplicationNumber=range(1,15) # last nunber is 14 not 15
  print("-- result --")
  for n in multiplicationNumber:
    print(f"{numb}*{n}={n*numb}")





    
      




