while True:
    print("1 - napisat 'lekosaci' 10 krat")
    print("2 - skonci program")
    volba = input("Zadaj volbu (1/2): ")

    if volba == "1":
        for i in range(10):
            print("lekosaci")
    elif volba == "2":
        print("Koniec programu.")
        break
    else:
        print("Neplatna volba, skus znova.")