# -- built in function reduce --



from functools import reduce


def sum_all(num1,num2):
  return num1 + num2
mynumbers=[1,2,100,6,33]
result=reduce(sum_all,mynumbers)
print(result) # => ((((1+2)+100)+6)+33)=142

print("_-"*10)
result=reduce(lambda num1,num2:num1+num2,mynumbers)
print(result) # => ((((1+2)+100)+6)+33)=142
