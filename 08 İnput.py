sayı=input("Bir sayı giriniz: ")
print(type(sayı))
#For döngüsü ile faktöriyel
sayı=int(input("Bir sayı giriniz: "))
faktoriyel=1
for i in range(1,sayı+1):
    faktoriyel*=i
print(f"{sayı}! ={faktoriyel}")
#While Döngüsü ile Faktöriyel
sayı=int(input("Bir sayı giriniz: "))
faktoriyel=1
i=2
while i<=sayı:
    faktoriyel*=i
    i+=1
print(f"{sayı}! ={faktoriyel}")
#Asal Sayı Kontrolü
sayı=int(input("Bir sayı giriniz: "))
asalmı=True
for i in  range(2,sayı):
    if sayı %i==0:
        asalmı=False
        break
if asalmı== True:
    print(f"{sayı} bir asal sayıdır")
else:
    print(f"{sayı} asal sayı değil")
#Kaç bölen bulma
sayı=int(input("Bir sayı giriniz: "))
bölen=0
for i in range(1,sayı+1):
    if sayı %i==0:
        bölen+=1
    else:
        continue
print(f"{bölen} böleni var birader")
#Rakamları Toplamı Hesapla
sayı=int(input("Bir sayı giriniz: "))
strsayı=str(sayı)
toplam=0
for i in strsayı:
    toplam+=int(i)
print(toplam) #Veya
sayı=int(input("Bir sayı giriniz: "))
toplam=0
geçici=sayı
while geçici!=0:
    basamak=geçici%10
    toplam+=basamak
    geçici//=10
print(toplam)
#ekrandan 5 sayı en küçük en büyük 
liste=[] 
for i in range(5):
    sayı=int(input("Bir sayı giriniz: "))
    liste.append(sayı)
print(f"{max(liste)} en büyüğü bu birader")
print(min(liste))
#Tam karemi değilmi
sayı=int(input("Bir sayı giriniz: "))
karekök=sayı**0.5
if karekök==int(karekök):
    print("Tamkaredir")
else:
    print("Tamkare değil")
#Harf kaç kere kullanılmış
metin=input("Bir metin giriniz: ")
sozluk=dict()
for i in metin:
    if i in sozluk:
        sozluk[i]+=1
    else:
        sozluk[i]=1
for i,adet in sozluk.items():
    print(i,adet)
#Ekranda A ları büyük yazdırma
metin=input("Bir metin giriniz: ")
metin2=""
for i in metin:
    if i=="a":
        metin2+="A"
    else:
        metin2+=i
print(metin2)









