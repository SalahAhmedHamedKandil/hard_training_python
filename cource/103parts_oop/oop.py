# ------------- oop ------------------
# class Member:
#     def __init__(self):
#         pass

# ================================
class Member:
    def __init__(self,first_name,midle_name,last_name):
        self.f_name=first_name
        self.m_name=midle_name
        self.l_name=last_name
        # pass
Member_one=Member("salah","ahmed","hamed")
Member_two=Member("ahmed","hamed","mohamed")
Member_three=Member("hamed","ahmed","hamed")
# print(dir(Member_one))
print(Member_one.f_name,Member_one.m_name,Member_one.l_name)
print(Member_two.f_name,Member_two.m_name,Member_two.l_name)
print(Member_three.f_name,Member_three.m_name,Member_three.l_name)