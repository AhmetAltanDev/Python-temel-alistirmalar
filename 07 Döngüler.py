for i in range(0,10,2):
    print(i)
sonuç=1
for i in range(0,10):
    sonuç*=2
print(sonuç)
liste1=["a","b","c"]
liste2=[1,2,3]
for harf in liste1:
    for rakam in liste2:
        print(harf,rakam)
liste=[1,2,3,4,5,6]
for i in liste:
    if i==3:
        print("Atla seri kardeş")
        continue
    print(i)
liste1 = range(100)
for i in liste1:
    if i %3!=0:
        continue
    elif i==81:
        break
    print(i)    
x=2
while x<10:
    print(x)
    x+=1
print("x=" , x)
x=5
y=7
while x*y <1000:
    print(x,y)
    x*=2
    y*=2

i = 1

while True:
    i += 1
    if i % 2 == 0:
        print(i)
    if i == 600:
        break



    



