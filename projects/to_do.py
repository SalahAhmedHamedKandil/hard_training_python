import os


FILE_NAME="tasks.txt"
def load_tasks():
  tasks=[]
  if os.path.exists(FILE_NAME):
    with open(FILE_NAME,"r") as file:
      for line in file:
        tasks.append(line.strip())
        print(tasks)
  return tasks

def save_task(tasks):
  with open(FILE_NAME,"w",encoding="utf-8")as file:
    for task in tasks:
      file.write(task+"\n")

def show_tasks(tasks):
  if not tasks:
    print("\n no tasks")
  else:
    print("\n -- tasks --")
    for i,task in enumerate(tasks,start=1):
      print(f"{i} = {task}")

# main projram
def main():
  tasks=load_tasks()
  while True:
    print ("_-"*10)
    print("-- to do list --")
    print("1 - add task")
    print("2 - view tasks")
    print("3 - delete task")
    print("4 - edit task")
    print("5 - exit")
    choice =(input("coice an option : ")).strip()
    if choice =="1":
      task=input("enter task : ")
      tasks.append(task)
      save_task(tasks)
      print ("task is added")
    elif choice =="2":
      show_tasks(tasks)
    elif choice=="3":
      show_tasks(tasks)
      if tasks:
        num=int(input("what is the task number to delete?"))
        tasks.pop(num-1)
        save_task(tasks)
        print("task is deleted")
    elif choice == "4":
      show_tasks(tasks)
      if tasks:
        num=int(input("what is the task number to edit ? "))
        new_task=input("new task ?")
        tasks[num-1]=new_task
        save_task(tasks)
        print("task is updated")
    elif choice == "5":
      print("good bey")
      break
    else:
      print("invalid option .. try again")
    

 
  
main()









