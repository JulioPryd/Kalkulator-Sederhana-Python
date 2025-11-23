def kalkulator():

    print("\n=== Simple Kalkulator ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = input("Masukan nomer untuk memilih metode [1/2/3/4]: ")
    nomer1 = float(input("Masukan angka pertama: "))
    nomer2 = float(input("Masukan angka kedua: "))

    if pilihan == "1":
        print(f"Hasil: {nomer1} + {nomer2} = {nomer1 + nomer2}")
    elif pilihan == "2":
        print(f"Hasil: {nomer1} - {nomer2} = {nomer1 - nomer2}")
    elif pilihan == "3":
        print(f"Hasil: {nomer1} * {nomer2} = {nomer1 * nomer2}")
        if nomer2 != 0:
            print("Pembagian 0 tidak diizinkan!")
    else:
        print(f"Hasil: {nomer1} / {nomer2} = {nomer1 / nomer2}")

kalkulator()            