
def add_item():
  item=input("name item : ").strip()
  with open ("d20SortaListProgram.txt","a") as file:
    file.write(f"{item}\n")
    print("new item is added")
def show_items():
  with open ("d20SortaListProgram.txt","r") as file:
    items=file.readlines()
    item_list=[]
    for item in items:
      if item.strip():
        item_list.append(item.strip())
    if not item_list:
      print("No items")
      return
    item_list.sort()
    # print(item_list)
    for n,item in enumerate(item_list,1):
      
      print(f"{n} - {item}")

def delete_items():
  show_items()
  with open ("d20SortaListProgram.txt","r") as file:
    items=file.readlines()
    item_list=[]
    for item in items:
      if item.strip():
        item_list.append(item.strip())
    while True:
      try:
        index=int(input("enter item number to delete :").strip())-1
        if index < 0 or index >= len(item_list):
          print(f"invalid number choose from 1 to {len(item_list)}")
          continue
        break
      except ValueError:
        print(f"invalid number choose from 1 to {len(item_list)},just number")
    deleted_item=item_list.pop(index)
    with open ("d20SortaListProgram.txt","w") as file:
      for i in item_list:
        file.write(i+"\n")
    print(f"Item '{deleted_item}' deleted successfully ✅")
    



while True:
  print("~"*40)
  print("please choose following options")
  print("enter 0 to close ")
  print("enter 1 to add item ")
  print("enter 2 to show item ")
  print("enter 3 to delete item")

  print("~"*40)
  choice=input("what is your choice ? ").strip()
  while choice not in ("0","1","2","3"):
    choice=input("what is your choice ? ").strip()
  if choice == "0" :
    break
  elif choice == "1" :
    print("~"*40)
    add_item()
  elif choice == "2":
    show_items()
  elif choice == "3":
    delete_items()