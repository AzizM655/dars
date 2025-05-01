#Foydalanuvchidan juft son kiritishni so'rang. 
# Agar foydalanuvchi juft son kiritsa "Rahmat!", 
# agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

son = float(input("Juft son kiriting: "))
if son%2:
    print('Bu son juft emas.')
else:
    print("Rahmat!")



#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
    
    yosh = int(input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    narh = 0;
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")