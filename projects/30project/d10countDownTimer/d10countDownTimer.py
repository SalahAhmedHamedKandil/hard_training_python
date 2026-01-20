# counter down timer
print("\n== hello ==\n") 
print("."*50)
import time

def downTimer():
  second=input("enter the required number of seconds : ")
  while not second.isdigit():
    print("invlid number")
    second=input("enter the required number of seconds : ")
  second=int(second)
  while second > 0:
    min_=second//60
    secns=second%60
    timer=(f"{min_:02d} : {secns:02d}")
    print(timer,end="\r")
    time.sleep(1)
    second -=1


while True:
  downTimer()
  choose=input("enter 1 to other operation \nenter 0 to close \nenter your choice : ")
  if choose =="0":
    print("good bye")
    break
