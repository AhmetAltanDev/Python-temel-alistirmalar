#İlk 10 Bin asal sayı kaçı 5 ile başlar 3 ila bitar
asalsayılar=list()
asalsayılar.append(2)
sayı=3
while True:
    prime=True
    for i in range(2,sayı):
        if sayı%i==0:
            prime=False
            break
    if prime:
        asalsayılar.append(sayı)
        if len(asalsayılar)==100:
            break
    sayı+=1
liste2=[]
for i in asalsayılar:
    strprime=str(i)
    if strprime.startswith("5") and strprime.endswith("3"):
        liste2.append(i)
print(liste2)
#3 basamaklı sayıların kaç tanesi küplerinin toplamına eşittir
liste = []
for i in range(100, 1000):
    toplam = 0
    geçici = i
    while geçici != 0:      # DÜZELTME: "geçici" kontrol edilmeli, "i" değil
        basamak = geçici % 10
        toplam += basamak**3
        geçici //= 10
    if toplam == i:
        liste.append(i)
print(liste)
#Fİbonacci
fibocacilist=[]
fibocacilist.append(1)
fibocacilist.append(1)
ind=2
while True:
    fibocacilist.append(fibocacilist[ind-2]+fibocacilist[ind-1])
    ind+=1
    if len(fibocacilist)==100:
        break
print(fibocacilist)
#100 basamaklı Fibonacci
fibolist=[1,1]
index=2
while True:
    fibolist.append(fibolist[index-2]+fibolist[index-1])
    terim=fibolist.append(fibolist[index-2]+fibolist[index-1])
    if len(str(terim))==100:
        print(terim)
        break
    index+=1