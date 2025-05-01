#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, 
# ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. 
# GM uchun ikkala harfni katta qiling.

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for moshina in cars:
    if moshina == 'gm':
        print(moshina.upper())
    else:
        print(moshina.title())

# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 

for moshina in cars:
      if moshina!='gm':
        print(moshina.title())
else:
        print(cars.upper()) 