class Age:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.months=age*12
        self.days=round(age*365.25)
        self.hours=self.days*24

salah_age=Age("salah",11)    
print(salah_age.age,salah_age.months)