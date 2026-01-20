# Exception handling
# try => except -else -finaly
# ===========================
# try => test the code for error
# except => dandle the error
# ------------------------------
# else  => no error 
# finaly => run the code 
# --------------------------------
try :
  age=int(input("what is your age ?"))

except ValueError:
  print("invalid number 1")
except:
  print("invalid number")
else : # if is not erroe
  print("valid number")
finally:
  print("hello from finally")