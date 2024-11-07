def pelaajamääräkysymys(): # tää funktio kysyy pelaajien määrän
    pelaajienmäärä = int(input("Syötä pelaajien määrä: ")) # pelaajienmäärä muuttujaan tallennetaan käyttäjän kertoma luku
    pelaajat = [] # aluksi on tyhjä lista
    for i in range(pelaajienmäärä): # rivit 5 ja 6 toteutaan niin monta kertaa kun pelaajienmäärä on
        nimi = input(f"Kirjoita {i + 1} pelaajan nimi: ")
        pelaajat.append({"nimi": nimi, "pisteet": []}) # "pelaajat" listaan tallentuu pelaajan nimi ja pisteet
    return pelaajat # palauttaa listan johon on luotu pelaajat 

def yksittäinenkierros(pelaaja, kierros): # tämä funktio on keilauksen yksi kierros
    # print(f"\nKierros {kierros + 1} - {pelaaja['nimi']}")
    print(f"\n{pelaaja['nimi']} vuoro ja kierros on {kierros + 1}")
    heitto1 = int(input("Ekan heiton pisteet: "))
    if heitto1 == 10: # jos pelaaja tekee täyskaadon eli kaataa 10 keilaa ja siitä käytetään nimitystä "kaato""
        print("Kaadoit kaikki 10 keilaa eli KAATO") # niin tämä tulostuu konsoliin
        pelaaja["pisteet"].append((heitto1, 0))  # Kaato merkitään merkitään listaan
        return

    heitto2 = int(input("Toka heitto: "))
    while heitto1 + heitto2 > 10: # jos molempien heittojen summa on yli 10 niin tokan heiton pistemäärä kysytään uuestaan
        print("Voit kaataa kierroksen aikana maksimissaan 10 keilaa") # sanotaan käyttäjälle että yhellä kierroksella ei voi saada yli 10 pistettä
        heitto2 = int(input("Toka heitto: ")) # kysytään tokan heiton pisteet

    pelaaja["pisteet"].append((heitto1, heitto2)) # pisteet lisätään listaan

def pisteenlasku(pelaajat):
    tulokset = {} # tuloksien tallennus
    for pelaaja in pelaajat: # kaikki pelaajat käydään läpi
        pisteet = 0 # kaikkien pelaajien pisteet laitetaan aluksi nollaan
        kierrospisteet = pelaaja["pisteet"] 
        for i in range(len(kierrospisteet)):
            heitto1, heitto2 = kierrospisteet[i] 

            
            if heitto1 == 10: # jos ekalla heitolla saa 10 pistettä eli KAATO
                pisteet += 10 # niin pisteisiin lisätään 10
                if i + 1 < len(kierrospisteet): # 
                    pisteet += kierrospisteet[i + 1][0] + (kierrospisteet[i + 1][1] if kierrospisteet[i + 1][0] != 10 else kierrospisteet[i + 2][0] if i + 2 < len(kierrospisteet) else 0) # lisätään seuraavan kierroksen ensimmäisen heiton pisteet, ja jos seuraavalla kierroksella oli kaato, lisätään myös toisen heiton pisteet

            else:
                pisteet += heitto1 + heitto2 # jos ekalla heitolla kaatuu alle 10 keilaa niin pisteet on molempien heittojen summa

        tulokset[pelaaja["nimi"]] = pisteet
    return tulokset

def lopputulos(lopputulokset):
    print("\nTulokset:")
   
    with open("keilaustulos.txt", "w") as tiedosto:  # Tulosten tulostus erilliseen "keilaustulos.txt" tiedostoon jos tiedosto on olemassa niin tulokset tallentuu valmiina olevaan tiedostoon, mutta jos tiedostoa ei ole olemassa niin ohjelma luo uuden tiedoston ja tallentaa tiedot siihen
        tiedosto.write("Lopputulos\n") # tiedoston ekalle riville laitetaan otsikoksi "Lopputulos"
        for nimi, pisteet in lopputulokset.items(): # Jokaisen pelaajan nimi ja pisteet kirjoitetaan omalle riville
            tulos = f"{nimi}: {pisteet} pistettä\n"
            print(tulos.strip())
            tiedosto.write(tulos)

def keilailupeli():
    pelaajat = pelaajamääräkysymys()  # Pelaajat saadaan tietoon "pelaajamääräkysymys" funktion avulla
    for kierros in range(10):
        for pelaaja in pelaajat:
            yksittäinenkierros(pelaaja, kierros)
    
    lopputulokset = pisteenlasku(pelaajat)
    lopputulos(lopputulokset)

keilailupeli()  # Ohjelma alkaa

