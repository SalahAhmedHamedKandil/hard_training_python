class Member:
    not_allowed_name=["hell","shit"]
    user_num=0
    def __init__(self,first_name,midle_name,last_name,gender):
        self.first_mane=first_name
        self.midle_name=midle_name
        self.last_name=last_name
        self.gender=gender
        Member.user_num +=1
    def full_name(self):
        if self.first_mane in Member.not_allowed_name:
            raise ValueError("name not allowed")
        else:
            return f"{self.first_mane} {self.midle_name} {self.last_name}"
    def title_name(self):
        return (f"  hello {self.full_name()}").strip()
    

print(Member.user_num)
member1=Member("salah","ahmed","hamed","male")     
print(member1.full_name())
print(member1.title_name())
print(Member.user_num)
