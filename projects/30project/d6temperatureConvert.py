def temperature_convert():

  print("-- temperature converter --")
  print("1-celsius to fehrenheit")
  print("2-fehrenheit to celsius")
  choose=input('enter your choice 1 or 2 :')
  while choose not in ("1","2"):
      print("rong choice try again " )
      choose=input('enter your choice 1 or 2 :')
  while choose in ("1","2"و"0"):
    
    if choose == "1":
        while True:  
          try:
            temp=int(input("enter the temperature value : "))
            break
          except ValueError:
            print("please enter int number,try again")

        print(f"{(temp*9/5)+32} fehrenheit")
      
    elif choose == "2":
        while True:  
          try:
            temp=int(input("enter the temperature value : "))
            break
          except ValueError:
            print("please enter int number,try again")
        print(f"{(temp-32)*5/9} celsius")
    
temperature_convert()