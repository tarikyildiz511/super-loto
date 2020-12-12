import random
sayi1 = random.randint(1,60)
sayi2 = random.randint(1,60)
sayi3 = random.randint(1,60)
sayi4 = random.randint(1,60)
sayi5 = random.randint(1,60)
sayi6 = random.randint(1,60)

kolon  = input("oynamak isterseniz evet yazın")

if kolon == "evet" or "Evet":
    print(sayi1,sayi2,sayi3,sayi4,sayi5,sayi6,"kolon oluşturuldu")
else:
    print("Tamam sonra oynarsın")