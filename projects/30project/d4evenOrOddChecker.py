# Day 4: Even or Odd Checker
def check_even_odd():
  try:
    number=int(input("enter the number please : "))
  except ValueError:
    print("invalid input \nplease enter a valid integer .")
    return
  if number % 2==0:
    