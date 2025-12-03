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

