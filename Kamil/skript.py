def main():
    while True:
        print("1 - vypis Kamil 10x")
        print("2 - koniec")
        volba = input("Vyber moznost (1/2): ").strip()
        if volba == "1":
            for _ in range(10):
                print("Kamil")
        elif volba == "2":
            print("Koniec.")
            break
        else:
            print("Neplatna volba, skus znova.")


if __name__ == "__main__":
    main()
