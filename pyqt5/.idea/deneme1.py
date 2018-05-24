
print("""


------------------------------------------------------
1-) topla
2-) cıkar
3-) carp
4-) böl
5-) cıkmak için 

""")
while True:
    anahtar = int(input("lütfen yapmak istediğiniz işlemi giriniz:"))
    if(anahtar == 1):
        sayi1 = int(input("Lütfen sayi1 i giriniz.."))
        sayi2 = int(input("Lütfen sayi2 i giriniz..."))
        sonuc = sayi1 + sayi2
        print(sonuc)

    elif(anahtar == 2 ):
        sayi1 = int(input("Lütfen sayi1 i giriniz.."))
        sayi2 = int(input("Lütfen sayi2 i giriniz..."))
        sonuc = sayi1 - sayi2
        print(sonuc)


    elif(anahtar == 3):
        sayi1 = int(input("Lütfen sayi1 i giriniz.."))
        sayi2 = int(input("Lütfen sayi2 i giriniz..."))
        sonuc = sayi1 * sayi2
        print(sonuc)

    elif(anahtar == 4):
        sayi1 = int(input("Lütfen sayi1 i giriniz.."))
        sayi2 = int(input("Lütfen sayi2 i giriniz..."))
        sonuc = sayi1 / sayi2
        print(sonuc)

    elif(anahtar == 5):
        break

    else:
        print("Geçersiz işlem yaptınız..")
        break