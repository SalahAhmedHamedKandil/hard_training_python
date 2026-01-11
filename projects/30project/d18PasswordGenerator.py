import random
import string
def deco_(funtion_):
  def wrapper():
    while True:
        try:
            length=int(input("what is the passwords' length ? it have been moor than 6 :").strip())
            if length<6:
                print("it have been moor than 6 ")
                continue
            break
        except ValueError:
            print("invalid number")
    funtion_(length)
  return wrapper
@deco_
def generate_password(length):
    password_container=(string.ascii_lowercase+
                        string.ascii_uppercase+
                        string.digits+
                        string.punctuation)
    password="".join(
        random.choice(password_container)
        for _ in range(length)
    )
    print("\n✅ Generated Password:")  
    print(password)    
generate_password()
                  

    
