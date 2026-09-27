if True:
    print("Naciş Cancıktır")
if False:
    ("Naciş Cancık Değil")
a=5
b=7
if a==b:
    print("Naciş Ebcik Kafadır")
else:
    print("Naciş Cancık Elebaşı")
renk="Mavi"
if renk=="Beyaz":
    print("Renk Beyaz")
if renk=="Sarı":
    print("Sarı")
elif renk=="Siyah":
    print("Siyah")
else:
    print("Mavi")
a=5
b=8
c=10
if a<b or c==a:
    print("Doğru")
else:
    print("Yanlış")
if a>b and c!=a:
    print("Doğru")
else:
    print("Yanlış")
renk=["Sarı","Mavi","Siyah"]
a="Sarı"
if a in renk:
    print("Var Kardeş")
else:
    print("Yok Birader")
isim="Ahmet"
a="a"
if a in isim:
    print("Var Kardeş")
else:
    print("Yok Birader")
if not a in isim:
    print("Tabiiki")
else:
    print("Asla")
a="python"
b="pytho"
b+="n"
if a==b:
    print("Evet")
else:
    print("Hayır")
if a is b:
    print("Evet")
else:
    print("Hayır")