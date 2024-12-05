import random


def ruletka():
   waluta = str(input("jaką chcesz walute?"))
   balans = 1000
   while balans > 0:
        print("\033[32mmasz", balans, waluta, "\033[39m")
        zaklad = float(input("ile obstawiasz?"))
        if zaklad < 0:
            print("\033[31mnie da sie grac na minusie stary\033[39m")
            break
        elif zaklad > balans:
            print("\033[31mnie stać cie na tyle stary\033[39m")
            break
        elif zaklad == 0:
            print("\033[31mserio chcesz grać o NIC? no dobra\033[39m")
        balans = balans - zaklad
        print("co obstawiasz")
        print("1 - liczba")
        print("2 - kolor")
        print("3 - parzystosc")
        print("4 - zakres")
        print("5 - niska/wysoka")
        x = int(input())
        liczba = random.randint(0, 36)
        k = random.randint(1, 2)
        if x == 1:
            print("\033[36mpodaj liczbe (od 0 do 36)\033[39m")
            a = int(input())
            if a > 36:
                print("\033[31mod 0 do 36 geniuszu\033[39m")
            if a == liczba:
                print("\033[35mHuge Jackpot!!! \033[39m")
                if zaklad == 0:
                    print("\033[32mbrawo! masz swoje darmowe 0", waluta, "\033[39m")
                zaklad = zaklad * 15
                balans = balans + zaklad
                print("\033[33mwygrywasz!\033[39m")
                print("\033[32mmasz teraz", balans, waluta, "\033[39m")
                print("\033[34mwylosowana liczba to", liczba, "\033[39m")
            else:
                print("\033[31mcala kasa przegrana \033[39m")
                print("\033[34mwylosowana liczba to", liczba, "\033[39m")
        elif x == 2:
            print("1 - \033[31mczerwony \033[39m")
            print("2 - \033[30mczarny \033[39m")
            print("3 - \033[32mzielony \033[39m")
            a = int(input())
            if a == 1 or a == 2:
                if a == k:
                    print("\033[35mJackpot! \033[39m")
                    if zaklad == 0:
                        print("\033[32mbrawo! masz swoje darmowe 0", waluta, "\033[39m")
                    zaklad = zaklad * 2
                    balans = balans + zaklad
                    print("\033[33mwygrywasz!\033[39m")
                    print("\033[32mmasz teraz", balans, waluta, "\033[39m")
                    if k == 1:
                        print("wylosowany kolor to czerwony")
                    else:
                        print("wylosowanu kolor to czarny")
                else:
                    print("\033[31mi po majatku, przegrana \033[39m")
            elif a == 3:
                if liczba == 0:
                    print("\033[35mMEGA HUGE BIG JACKPOT!!!!!\033[39m")
                    if zaklad == 0:
                        print("\033[32mbrawo! masz swoje darmowe 0", waluta, "\033[39m")
                    zaklad = zaklad * 25
                    balans = balans + zaklad
                    print("\033[35mwygrywasz!\033[39m")
                    print("\033[35mmasz teraz", balans, waluta, "\033[39m")
                else:
                    print("\033[31mdobra robota! znowu kasa przewalona\033[39m")
            else:
                print("\033[31mod 1 do 3 prosze następnym razem\033[39m")
                exit()
        elif x == 3:
            print("1 - nieparzysta")
            print("2 - parzysta")
            a = int(input())
            if a == k:
                print("\033[35mJackpot!!!\033[39m")
                if zaklad == 0:
                        print("\033[32mbrawo! masz swoje darmowe 0", waluta, "\033[39m")
                zaklad = zaklad * 2
                balans = balans + zaklad
                print("\033[33mwygrywasz!\033[39m")
                print("\033[32mmasz teraz", balans, waluta, "\033[39m")
            else:
                print("\033[31mprzegrana, tata nie jest dumny\033[39m")
        elif x == 4:
            print("1 - od 1 do 12")
            print("2 - od 13 do 24")
            print("3 - od 25 do 36")
            a = int(input())
            if a == 1:
                if liczba > 0 and liczba < 13:
                    print("\033[35mJackpot!\033[39m")
                    if zaklad == 0:
                        print("\033[32mbrawo! masz swoje darmowe 0", waluta, "\033[39m")
                    zaklad = zaklad * 3
                    balans = balans + zaklad
                    print("\033[33mwygrywasz!\033[39m")
                    print("\033[32mmasz teraz", balans, waluta, "\033[39m")
                    print("\033[34mwylosowana liczba to", liczba, "\033[39m")
                else:
                    print("\033[31mprzegrana znowu, kto wogule na to stawia?\033[39m")
                    print("\033[34mwylosowana liczba to", liczba, "\033[39m")
            elif a == 2:
                if liczba > 12 and liczba < 25:
                    print("\033[35mJackpot!\033[39m")
                    if zaklad == 0:
                        print("\033[32mbrawo! masz swoje darmowe 0", waluta, "\033[39m")
                    zaklad = zaklad * 3
                    balans = balans + zaklad
                    print("\033[33mwygrywasz!\033[39m")
                    print("\033[32mmasz teraz", balans, waluta, "\033[39m")
                    print("\033[34mwylosowana liczba to", liczba, "\033[39m")
                else:
                    print("\033[31mprzegrana znowu, kto wogule na to stawia?\033[39m")
                    print("wylosowana liczba to", liczba)
            elif a == 3:
                if liczba > 24 and liczba < 37:
                    print("\033[35mJackpot!\033[39m")
                    if zaklad == 0:
                        print("\033[32mbrawo! masz swoje darmowe 0", waluta, "\033[39m")
                    zaklad = zaklad * 3
                    balans = balans + zaklad
                    print("\033[33mwygrywasz\033[39m")
                    print("\033[32mmasz teraz", balans, waluta, "\033[39m")
                    print("\033[34mwylosowana liczba to", liczba, "\033[39m")
                else:
                    print("przegrana znowu,")
                    print("\033[34mwylosowana liczba to", liczba, "\033[39m")
        elif x == 5:
            print("1 - niska (1 - 18")
            print("2 - wysoka (19 - 36")
            a = int(input())
            if a == 1:
                if liczba > 0 and liczba < 19:
                    print("\033[35mJackpot! \033[39m")
                    if zaklad == 0:
                        print("\033[34mbrawo! masz swoje darmowe 0", waluta, "\033[39m")
                    zaklad = zaklad * 2
                    balans = balans + zaklad
                    print("\033[33mwygrywasz!\033[39m")
                    print("\033[32mmasz teraz", balans, waluta, " \033[39m")
                else:
                    print("\033[31mprzegrana kaska\033[39m")
            elif a == 2:
                if liczba > 18 and liczba < 37:
                    print("\033[35mJackpot! \033[39m")
                    if zaklad == 0:
                        print("\033[34mbrawo! masz swoje darmowe 0", waluta, "\033[39m")
                    zaklad = zaklad * 2
                    balans = balans + zaklad
                    print("\033[33mwygrywasz!\033[39m")
                    print("\033[32mmasz teraz", balans, waluta, " \033[39m")
                else:
                    print("\033[31mprzegrana kaska\033[39m")


        else:
            print("nastepnym razem podaj liczbe od 1 do 5")
            break
        ponownie = input("grasz jeszcze raz?? \033[32m(T/N)\033[39m: ").upper()

        if ponownie != 'T':
            print("wychodzisz z kasyna z liczbą\033[32m", balans, "$\033[39m")
            break
        elif balans <= 0:
            print("nie ma kasy, nie ma rozgrywki")
            break
if __name__ == '__main__':
    ruletka()

# Wiele inspiracji zostało zaciągniętych od Jana Zdanowskiego (dzieki ziomus kc)
# Od kolegi Szymona Miązko nic nie brałem ale i tak kc

# kolory:
# BLACK    \033[30m
# RED      \033[31m
# GREEN    \033[32m
# YELLOW   \033[33m
# BLUE     \033[34m
# MAGENTA  \033[35m
# CYAN     \033[36m
# WHITE    \033[37m
# RESET    \033[39m
