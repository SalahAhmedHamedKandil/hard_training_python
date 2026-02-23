# oop
# ------------
class Member():
    not_allowed_name=["hell","shit","baloot"]
    user_num=0
    @classmethod
    def show_user_count(cls):
        print(f"we have {cls.user_num} users")
    def __init__(self,f_name,m_name):
        self.ff_name=f_name
        self.mm_name=m_name
        Member.user_num +=1
    def full_name(self):
        if self.ff_name in Member.not_allowed_name:
            raise ValueError("name not allowed")
        f_name=(f"{self.ff_name} {self.mm_name}")
        return f_name
    def delete_user(self):
        Member.user_num -=1
        return (f"user {self.ff_name} is deleted")
    def name_with_title(self):
        return f" hello MR {self.ff_name} {self.mm_name}"

    pass


# print(Member.user_num)
# member1=Member("salah","ahmed")
# member2=Member("ahmed","hamed")
# member3=Member("hamed","mohamed")
# print(member1.ff_name,member1.mm_name) # == print(member1.full_name())
# print(member2.ff_name,member2.mm_name)
# print(member3.ff_name,member3.mm_name)
# print("~"*20)
# print(member1.full_name())
# print(member2.full_name())
# print(member3.full_name())
# print(Member.user_num)
# print("~"*20)
# print(member3.delete_user())
# print("~"*20)
# Member.show_user_count()
Member11=Member("salah","ahmed")
print(Member11.name_with_title())




# print(dir(Member))