# date and time => intoduction
# ---------------------------------
import datetime
# print(dir(datetime))
# print(dir(datetime.datetime))



# go print the current date and time
print(datetime.datetime.now())
print("-_-"*20)
# go print the current year , month and day
year=(datetime.datetime.now().year)
month=(datetime.datetime.now().month)
day=(datetime.datetime.now().day)
print(year)
print(month)
print(day)
print("-_-"*20)
# ---------------------------------------------
print(datetime.datetime.min)
print(datetime.datetime.max)
