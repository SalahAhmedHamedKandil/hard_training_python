#  اختار المطلوب  
# دالة ادخال المهام 
# دالة قرائة المهام 


import os
# -----------------------------------------
def add_tasks():
  n_task=str(input("enter new task : ").lower().strip())
  with open("ToDo.txt","a")as f:
    f.write(n_task+"\n")
    print("the task have been add")
# --------------------------------------------
def read_task():

  with open("ToDo.txt","r")as f:
    tasks=f.readlines()
    for n,l in enumerate(tasks,start=1):
      print(f"{n}-{l.strip()} ")
# ----------------------------------------

def delete_task():
    if not os.path.exists("ToDo.txt") or os.path.getsize("ToDo.txt") == 0:
        print("No tasks to delete.")
        return

    read_task()  
    while True:
      try:
          task_num = int(input("\nEnter task number to delete: "))
          break
      except ValueError:
          print("Invalid number!")
        

    with open("ToDo.txt", "r") as f:
        tasks = f.readlines()

    while  task_num < 1 or task_num > len(tasks):
        print("Task number out of range!")
        while True:
          try:
              task_num = int(input("\nEnter task number to delete: "))
              break
          except ValueError:
              print("Invalid number!")
            

    deleted = tasks.pop(task_num - 1)  # حذف المهمة

    with open("ToDo.txt", "w") as f:
        f.writelines(tasks)

    print(f"Task '{deleted.strip()}' has been deleted.")

print ("--- welcome ---")

# -------------------------------------------------
while True:
  print("``"*20)
  choose=input("1-to add task\n2-to read task\n3-to delete task\n4-to close\nenter your choice : ")
  if choose =="1":
    add_tasks()
  elif choose =="2":
    read_task()
  elif choose =="3":
    delete_task()
  elif choose =="4":
    print("bye")
    break
  else:
      print("Invalid choice, please enter 1, 2, or 3.")
