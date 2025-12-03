# file handling 
# ******************
# "a"=> append => to open file for appending values ,creat file if not existe
# "r"=> read   => [default value] open file for read and give error if it isn't excit
# "w"=> write  => open file for writing creat file if not exists
# "x"=> creat file ,give error if file exists
# -------------------------------------

# # import os
# # print (os.getcwd())
# # file =open(r"D:\elzero_python\salah.txt")
# # reading file=>
# file = open("salah.txt","r")
# # print(file)
# # print(file.read()) #read full file
# # print(file.read(2)) #give 2 index
# # print(file.readline(3)) #give 3 index
# # print(file.readlines(10)) #give 10 index
# print(file.readlines()) 
# print ("-"*9)
# with open("salah.txt","r") as file1 :
#   for line in file1:
#     t=(line)
#     print(t)
#     if line.startswith("4"): #print line 4
#       break



# --------------------------------

file2=open("salah2.txt","w") 
file2.write("hello from pytho file \nline 2")
file2.close()
file3=open("salah2.txt","r")
# print(file3.readline()) # hello from pytho file
# print(file3.readline()) # line 2
print(file3.readlines()) # ['hello from pytho file \n', 'line 2']



