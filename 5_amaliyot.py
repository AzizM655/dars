# 1) Quyidagi o`zgaruvchilarni yarating.
# kocha = "Bog`bon"
# mahalla = " Sog`bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# print(kocha + " ko`chasi," + mahalla + " \nmahallasi, " + tuman + " tumani,\n "+viloyat +" viloyati ")
# print(f"{kocha},{mahalla}, {tuman}, {viloyat}")

# # # 2) Yuqoridagi o`zgaruvchilarni (kocha? mahalla, tuman, viloyat) qiymatini foydalanuvchidan so`rang. va avvalgi mashqni takrorlang`
# a = input ("Ko'changiz nomini kiriting:\n>>")
# b = input ("mahallangiz nomini kiriting:\n>>")
# c = input ("Siz qaysi tumanda yashaysiz? Tumaningiz nomini kiriting:\n>>")
# d = input ("Viloyat nomini kiriting:\n>>")
# # print("Assalomu alaykum, Siz", d+ " viloyati" ',' , c + " Tumani" ',' , b + " mahallasi" ',' , a + " ko'chasida yashaysiz")

# print("Assalomu alaykum, Siz, \n ", d + " viloyati, \n" , c + " Tumani, \n" , b + " mahallasi,\n" , a + " ko'chasida yashaysiz")

# 3) f-string yordamida, yangi manzil deb nomlangan o`zgaruvchiga yuklang
# kocha = "Bog`bon"
# mahalla = " Sog`bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# manzil=f"{kocha} ko`chasi," f"{mahalla} mahallasi, "  f"{tuman} tumani", f"{viloyat} , viloyati"
# print(manzil)

# kocha = "Bog`bon"
# mahalla = " Sog`bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# manzil=f"{kocha} ko`chasi, {mahalla} mahallasi, {tuman} tumani {viloyat} viloyati"
# print(manzil)


# kocha = "Bog`bon"
# mahalla = " Sog`bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# manzil=f"{kocha}, {mahalla},  {tuman}, {viloyat}"

# # print(manzil)
# print(manzil.title())
# print(manzil.upper())
# print(manzil.lower())
# print(manzil.capitalize())