# 1) otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 
# 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). 
# Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :
# Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan

otam = {'ismi': "Nig`matjon", 'tyil':1953,'shahar':'Toshkent'}
tyil = otam['tyil']
vil = otam['shahar']
print(f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} shahrida tug'ilgan")

# 2) Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
# Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

taomlar = {
    'Iymona':'osh',
    'Doniyor':'Lavash',
    'Azamat':"shashli",
    'Nazokat':"mastava",
    'Shaxnoza':"somsa"
    }

taom = taomlar['Azamat']
print(f"Azamatning sevimli taomi {taom}")