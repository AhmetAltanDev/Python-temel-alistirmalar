kişi={"isim":"ali","yaş":18,"cinsiyet":"m"}
print(kişi["yaş"])
kişi["isim"]="Ahmet"
print(kişi["isim"])
kişi.update({"isim":"Mehmet","yaş":20})
print(kişi)
kişi["id"]=4444
print(kişi)
del kişi["cinsiyet"]
print(kişi)
for i in kişi:
    print(i)
for i in kişi:
    print(kişi[i])
print(kişi.keys())
print(kişi.values())
print(kişi.items())
for k,v in kişi.items():
    print(k,v)
print(kişi.get("cinsiyet"))
print(kişi.get("boy","Yok öyle birader"))