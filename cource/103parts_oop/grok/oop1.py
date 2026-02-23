# # 1. نعمل Class (المخطط)
# class Car:                  # اسم الكلاس دايمًا بحرف كبير
#     def init(self, اللون, الماركة, السنة):   # ده الكونستركتور
#         self.اللون = اللون           # صفة (attribute) خاصة بالعربية دي
#         self.الماركة = الماركة
#         self.السنة = السنة
#         self.السرعة = 0              # صفة افتراضية

#     # 2. تصرف (method)
#     def كلمني(self):
#         print(f"أنا عربية {self.الماركة} لونها {self.اللون} سنة {self.السنة}")

#     def زوّد_السرعة(self, كام):
#         self.السرعة += كام
#         print(f"السرعة دلوقتي: {self.السرعة} كم/س")


# # 3. نعمل كائنات (objects) من المخطط
# عربية1 = Car("أحمر", "تويوتا", 2023)
# عربية2 = Car("أسود", "مرسيدس", 2025)

# # 4. نستخدمهم
# عربية1.كلمني()
# عربية2.كلمني()

# عربية1.زوّد_السرعة(30)
# عربية1.زوّد_السرعة(50)
# # =====================================

class Car:
    def __init__(self,color,model,year,max_speed):
        self.color=color
        self.model=model
        self.year=year
        self.speed=0
        self.max_speed=max_speed
    def data(self):
        return print(f"car's color is {self.color}\ncar's model is {self.model}\nmodel's year is {self.year}")
    def accelerate(self):
        if self.speed + 20 <= self.max_speed:
            print(f"{self.model}:- speed now : {self.speed}")
            self.speed +=20
            return True
        else:
            print(f"{self.model}: Max speed reached ({self.max_speed})")
            return False


car1=Car("yellow","toyta",2011,200)
car2=Car("reed","kia",2010,230)
car1.data()
car2.data()
# for r in range(100):
#     if car1.speed < car1.max_speed and car2.speed < car2.max_speed :
#         f"{car1.accelerate()} {car2.accelerate()} "
#     else:
#         print("we arrived to max speed")
#         break
print("Race starts...\n")

for _ in range(20):           # عدد كافي
    if not car1.accelerate() or not car2.accelerate():
        break

print("\n--- الوضع النهائي ---")
car1.data()
car2.data()    