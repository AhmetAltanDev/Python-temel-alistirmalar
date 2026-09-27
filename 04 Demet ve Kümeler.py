demet=("Sarı","Mavi","Yeşil")
for i in demet:
    print(i)



#Kümeler
küme={"Sarı","lacivert","Kırmızı"}
for i in küme:
    print(i)
küme.add("Siyah")
küme.discard("Turuncu")
#Kümeler Kesişim,Birleşim,Fark
küme1={"Sarı","Mavi","Pembe"}
küme2={"Pembe","Gri","Siyah"}
print(küme1.intersection(küme2))
print(küme1.union(küme2))
print(küme1.difference(küme2))
print("Beyaz" in küme1)
print("Gri" in küme1.union(küme2))



#Farklı
boşliste1=[]
boşdemet=()
boşküme={} 
boşliste2=list()
boşdemet2=tuple()
boşküme2=set()
print(type(boşliste1))
print(type(boşdemet))
print(type(boşküme)) #Demekki sonra bakılacak
py=set("Python")
print(py)
py=set("Merhaba")
print(py)