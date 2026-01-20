def temperature_convert():
  while True:
    print("-- temperature converter --")
    print("1-celsius to fehrenheit")
    print("2-fehrenheit to celsius")
    print("3-close the converter")
    
    choose=input('enter your choice 1 , 2 , 3 :')
    while choose not in ("1","2","3"):
        print("rong choice try again " )
        choose=input('enter your choice 1 , 2 ,3:')
      
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
    elif choose =="3":
       print("thank u for using our converter")
       break  
temperature_convert()