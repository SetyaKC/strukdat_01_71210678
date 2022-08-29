while True:
    print("Pilihan Menu: ")
    print("1. Penambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = input("Pilihan Menu: ")
    if pilihan == "Q":
        break
    a = int(input("Masukkan angka1: "))
    b = int(input("Masukkan angka2: "))

    if pilihan=="1":
        print(a+b)
    elif pilihan=="2":
        print(a-b)
    elif pilihan=="3":
        print(a*b)
    elif pilihan=="4":
        print(a/b)
    else :
        print ("ERROR")
