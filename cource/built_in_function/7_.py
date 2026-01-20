# bbuilt in function 
# enumerate()
# help()
# reversed()
# --------------------

# enumerate(iterable,start=0)
my_skills=["html","Css","Js","PHP"]
mySkillWithCounter=enumerate(my_skills,1)
# print(type(mySkillWithCounter)) => 'enumerate'
# print(mySkillWithCounter) => <enumerate object at 0x000002572D911F30>
# print(list(mySkillWithCounter)) =>[(1, 'html'), (2, 'Css'), (3, 'Js'), (4, 'PHP')]
for skill in mySkillWithCounter:
  print(skill)
# output
# (1, 'html')
# (2, 'Css')
# (3, 'Js')
# (4, 'PHP')
# ----------------------------------------


# help
# print(help(max)) # it explains the function


# --------------------------------------------

# reversed(iterable)

mystring='salah'
print(reversed(mystring)) # => <reversed object at 0x000001487527B010>
print(list(reversed(mystring))) #=> ['h', 'a', 'l', 'a', 's']
a=(list(reversed(mystring))) #=> ['h', 'a', 'l', 'a', 's']
print(list(reversed(a))) # => ['s', 'a', 'l', 'a', 'h']
word=''.join((reversed(a)))
print(word)

