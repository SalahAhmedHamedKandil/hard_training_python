# --- multi choice quistions -----
# 1  load (quistions' data)
# 2 save data (quistions)
# 3 add quistion 
# 4 asking
# ================================
import json
FILE_NAME=r"D:\elzero_python\projects\30project\d22multiple choice quize\22_multiple_choice_quiz.json"
def load():
    try:
        with open(FILE_NAME,"r",encoding="utf-8")as file:
            return json.load(file)
    except FileNotFoundError:
        print("file not found")
# --------------------------------------------------
def save_quistion(data):
    with open(FILE_NAME,"w",encoding="utf-8") as file :
        json.dump(data,file,indent=4)
# ============================================
def exit_()
    print("input exit to exit")
# =======================================================
def add_quistion():
    while True:
        exit_()
        quistion=input("input new quistion : ").strip().lower()
        if quistion=="exit":
            print("bye")
            return
        if not quistion:
            print("please enter quistion .")
            continue
        break
    while True:
        exit_()
        choice_1=input("enter choice 1 ").strip().lower()
        if choice_1 == "exit":
            print("bye")
            return
        if not choice_1:
            print("please enter choice")
        break
    while True:
        choice_2=input("enter choice 2 ").strip().lower()
        if choice_2 == "exit":
            print("bye")
            return
        if not choice_2:
            print("please enter choice")        
        break
    while True:
        choice_3=input("enter choice 3 ").strip().lower()
        if choice_3 == "exit":
            print("bye")
            return
        if not choice_3:
            print("please enter choice")   
        break


    