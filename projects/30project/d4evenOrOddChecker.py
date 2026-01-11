# Day 4: Even or Odd Checker
def check_even_odd():
  while True :
    try:
      number=int(input("enter the number please : "))
      break
    except ValueError:
      print("invalid input \nplease enter a valid integer .")
    
  if number % 2==0:
    print(f"the number ({number}) is even .")
  else:
    print(f"the number ({number}) is odd .")
check_even_odd()