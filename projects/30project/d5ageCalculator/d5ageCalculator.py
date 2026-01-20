from datetime import datetime
def calcukate_age():  
  while True:
    try:
      birth_year=int(input("enter your birth year (e.g.,1999) : ".strip()))
      if  birth_year >datetime.now().year:
        print('try again the birth year in the future')
        continue
      break
    except ValueError:
      print('invalid input , please enter a valid year.')

  current_year=datetime.now().year
  age=current_year-birth_year
  print(f"you are {age} years")
  
  


calcukate_age()