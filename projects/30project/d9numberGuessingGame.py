#  day 9 - number guessing game 
import random
def guessing_game():
  print("\n-- number guissing game --\n")
  while True:
    print("enter 1 to play")
    print("enter 0 to close")
    attempts = 0
    max_attempts = 6
    choose=input("enter your choice '1 or 0' : ").strip()
    while choose not in ("1","0","play","close"):
      print("please choose from (1 - 0)'enter 1 to play or 0 to close'")
      choose=input("enter your choice '1 or 0' : ").strip()
    if choose in ("0","close" ):
      print("thank u for using our app")
      break
    elif choose in ("1","play"):
      selected_s=int(input("enter the starting number : "))
      selected_e=int(input("enter the end number : "))
      secret_number=random.randint(selected_s,selected_e)

      while attempts < max_attempts:
        # max_attempts -=1
        attempts +=1
        if attempts != max_attempts:
          print(f"you stile have {max_attempts-attempts} attemps")
          print(f"i selected a number between {selected_s} => {selected_e}.")
        else:
          print(f"the last attemp")
          print(f"i selected a number between {selected_s} => {selected_e}.") 
        while True:  
          try:     
            guess=int(input(f"{("-"*20)}\nenter the expected number ").strip())
            break
          except ValueError:
            print(f"please enter numbers")
        # if not guess.isdigit():
        #   print(f"'{guess}' invalid number")
        #   continue
        if guess > secret_number :
          print("Too high ⬆️")
        elif guess < secret_number:
          print("Too low ⬆️")
        else:
          print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
          break
    else:
            print(f"❌ You lost! The correct number was: {secret_number}")
        

      
      
      


guessing_game()