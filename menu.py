import bryly

def menu():
        print("Co bedzie obliczane?")
        print("-------------------------")
        print("1) Szescian: pole")
        print("-------------------------")
        print("2) Prostopadloscian: pole")
        print("-------------------------")
        print("3) Graniastoslup: pole")
        print("-------------------------")
        print("4) Walec: pole")
        print("-------------------------")
        print("5) Stozek: pole")
        print("-------------------------")
        print("6) Kula: pole")
        print("-------------------------")
        print("7) Koło: pole")
        print("-------------------------")
        print("8) Romb: pole")
        print("-------------------------")
        print("9) trójkąt równoramienny: wysokość")
        print("-------------------------")
        print("10) kwadrat: przekątna")
    
        opcja = input(print("Wybierz opcję 1-10: "))

        if opcja == '1':
            print(bryly.szescian())
        elif opcja == '2':
            print(bryly.prostopadloscian())
        elif opcja == '3':
            print(bryly.graniastoslup())
        elif opcja == '4':
            print(bryly.walec())
        elif opcja == '5':
            print(bryly.stozek())
        elif opcja == '6':
            print(bryly.kula())
        elif opcja == '7':
            print(bryly.kolo())
        elif opcja == '8':
            print(bryly.romb())
        elif opcja == '9':
            print(bryly.wysokosc_trojkata())
        elif opcja == '10':
            print(bryly.przekatna_kwadratu())
        else:
            print("nie ma takiej opcji")
print(menu())
