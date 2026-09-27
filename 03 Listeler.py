renkler=["Siyah","Gri","Eflatun","Beyaz","Bordo"]
print(renkler[ 1:]) 
print(renkler[::2])
print(renkler)
renkler.append("Mavi")
renkler.insert(0,"Yeşil")
renkler.remove("Beyaz")
print(renkler)
fb=["Sarı","Lacivert"]
renkler.append(fb)
print(renkler)
renkler.extend(fb)
print(renkler)
giden=renkler.pop()
print(giden)
renkler.remove(fb)
renkler.reverse()
print(renkler)
renkler.sort() 
print(renkler)
renkler.sort(reverse=True)
print(renkler)
renkler2=sorted(renkler)
print(renkler2)
print(renkler)

#Eklenme unutulmuş
list1=["Sarı","Siyah","Pembe"]
list1[2]="Truncu"
print(list1)


#Farklı şeyler
renkler1=["Beyaz","Gri","Siyah"]
sayı=[1,2,3,4]
print(max(renkler1))
print(min(sayı))
print(sum(sayı))

for renk in renkler1:
    print(renk) 
print(list(enumerate(renkler1)))
print("Sİyah" in renkler1)
stringrenkler1=",".join(renkler1)
print(stringrenkler1)
renkler2=stringrenkler1.split(",")
print(renkler2)
