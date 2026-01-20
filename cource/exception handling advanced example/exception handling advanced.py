# exception handlin



# ------------------------
the_file=None
the_tries=3
while the_tries >0 :
  try: #try to oppen the file
    print("enter file name ")
    print(f"{the_tries} tries left")
    file_name_and_path=input("enter file name path : ").strip()
    the_file=open(file_name_and_path,"r",encoding="utf-8")
    print(the_file.read())
    break
  except FileNotFoundError:
    print("file not found")
    the_tries -=1
  except:
    print("error happen")
  finally:
    if the_file is not None:
      the_file.close()
else:
  print("all tries is done")
