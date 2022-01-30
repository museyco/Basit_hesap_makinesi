class Hesap_Makinesi:

    def __init__(self, sayi=int(), sayilistesi=None, ceviri=None):
        self.list = None
        if ceviri is None:
            ceviri = []
        if sayilistesi is None:
            sayilistesi = []
        self.sayilistesi = sayilistesi
        self.ceviri = ceviri
        self.sayi = sayi

# İŞLEMİ ÖNCE STR OLARAK ALIYORUM #
    def sayi_ekle(self, sayi):
        self.sayilistesi.append(sayi)

# STR İÇİNDEN İNT DEĞERLERİNİ ÇEKTİĞİM YER: #
    def cevirme(self):
        self.list = list
        for i in self.sayilistesi:
            try:
                self.ceviri.append(int(i))
            except ValueError:
                pass

# iŞLEMLER: #
    def toplama(self):
        sonuc = self.ceviri[0]
        for i in self.ceviri[1:]:
            sonuc = sonuc + i
        return sonuc

    def cikarma(self, ):
        sonuc = self.ceviri[0]
        for i in self.ceviri[1:]:
            sonuc = sonuc - i
        return sonuc

    def carpma(self):
        sonuc = self.ceviri[0]
        for i in self.ceviri[1:]:
            sonuc = sonuc * i
            break
        return sonuc

    def bolme(self):
        sonuc = self.ceviri[0]
        for i in self.ceviri[1:]:
            sonuc = sonuc / i
        return sonuc


hesap = Hesap_Makinesi()

print("""
------------------------------------------
          HESAP MAKİNESİ
          ~~~~~~~~~~~~~~
!Her Girdiden Sonra Bir Boşluk Bırakınız!
Çıkmak için: Q' ya basınız....
------------------------------------------
""")

print("İşleminizi Yazınız")
while True:
    sayilar = input(">")
    degisim = sayilar.split(" ")

    for i in degisim:
        hesap.sayi_ekle(i)

    if sayilar == "q":
        print("Program Kapatılıyor...")
        break

    for i in sayilar:

        if "+" in degisim:
            hesap.cevirme()
            print(f"Sonuç: {hesap.toplama()}")

        elif "-" in degisim:
            hesap.cevirme()
            print(f"Sonuç: {hesap.cikarma()}")

        elif "*" in degisim:
            hesap.cevirme()
            print(f"Sonuç: {hesap.carpma()}")

        elif "/" in degisim:
            hesap.cevirme()
            print(f"Sonuç: {hesap.bolme()}")
        else:
            "Tanımlanamayan bir işlem girdiniz!"

# DÖNGÜNÜN SORUNSUZ ÇALIŞMASI İÇİN AYARLAR#
        hesap.sayilistesi.clear()
        hesap.ceviri.clear()
        degisim.clear()
        sayilar = ()
    continue
