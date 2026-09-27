# Basit print örnekleri
print("Birinci satır:", "Hello World")
print("Hello World")
print("Kayra'nın Oyuncağı")

# Çok satırlı string
print("""Merhaba
Dünya""")

# Özel karakterler: \t ve \n
print("Ahmet\tÖğrenci")
print("Ahmet\nÖğrenci")

# Değişkenler
selam = "Merhaba"
dunya = "Dünya"

print(selam)
print(selam + " " + dunya)

# String indeksleme
print(selam[0])      # İlk harf
print(selam[-2])     # Sondan ikinci harf
print(selam[3:5])    # 3. ve 4. harf
print(selam[::2])    # İkili adımla
print(selam[::-1])   # Ters çevirme

# String metodları
print(selam.upper())
selam = selam.upper()
print(selam)
selam = selam.lower()
print(selam)
selam = selam.capitalize()
print(selam)

# Başlangıç ve bitiş kontrolü
print(selam.startswith("Me"))
print(selam.endswith("Ba"))

# Uzunluk
print(len(selam))

# Çarpma operatörü ile tekrar
print("Çalışkan Öğrenci " * 5)

# Formatlama
print("{}, {}".format(selam, dunya))
print(f"{selam}, {dunya}")
