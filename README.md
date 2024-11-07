# Ohjelmoinnin perusteet 5op TT00CD77-3013
- Jimi Heikkilä [AG0040]
- Harjoitustyö
- 7.11.2024


## Harjoitustehtävän ohje
- Tämä harjoitustehtävä sisältyy Jyväskylän ammattikorkeakoulun Ohjelmoinnin perusteet 5op TT00CD77 opintojaksolle.
- Harjoitustyön ideana on, että opiskelija oppii, soveltaa ja osoittaa opintojakson aihealueen hallintaa laajemmin ja syvemmin kuin pelkästään harjoitustehtävien avulla.
- Harjoitusyö on toteuttu käyttämällä Python ohjelmointikieltä.


## Mikä oli aiheeni?
- Aiheeni oli toteuttaa keilauspistelaskuri
- Keilaajia pitää olla vähintään 1
- Keilaajien määrän suhteen ei ole ylärajaa
- Kierroksia yhdessä keilauspelissä on 10
- Ohjelma kysyy jokaiselta pelaajalta kaadettujen keilojen määrän jokaikisen kierroksen jälkeen
- Ohjelma tunnistaa kaadon
- Ohjelma laskee jokaiselle pelaajalle yhteispisteet
- Lopuksi yhteispisteet ilmestyy konsoliin
- Lisäksi yhteispisteet tallentuu erilliseen tiedostoon (keilaustulos.txt)


## Linkki projektiin:
- Tähän linkki

## Käytännön toteutuksen selostus

### Sovelluksen toiminta:
- Aluksi ohjelma kysyy, että montako pelaajaa keilaukseen osallistuu
- Ohjelma kysyy pelaajien nimet
- Peli laskee jokaiselta kierrokselta pisteet:
    - Kaato = 10 pistettä yhdellä heitolla --> seuraavat heitot lisätään kaadon jälkeisiin pisteisiin
    - Jos ei tapahdu kaatoa niin pisteet lasketaan normaalina pluslaskuna. Eli ensimmäinen heitto + toinen heitto
- Kun peli loppuu niin ohjelma tulostaa lopputulokset konsoliin
- Lisäksi ohjelma laittaa lopputulokset ja keilaustulos.txt tiedostoon
    - Jos keilaustulos.txt tiedosto on jo olemassa niin ohjelma tallentaa lopputuloksen siihen
    - Mutta jos keilaustulos.txt tiedostoa ei ole olemassa niin ohjelma luo keilaustulos.txt tiedoston ja tallentaa lopputulokset sinne


### Funktiot:
- Funktio "pelaajamääräkysymys":
    - Ei parametreja
    - Kysyy pelaajamäärän ja kaikkien pelaajien nimet
    - Palauttaa listan kaikista pelaajista (nimi + pisteet)

- Funktio "yksittäinenkierros(pelaaja, kierros)":
    - Kaksi parametria:
        1. pelaaja = pelaajan nimi ja pisteet
        2. kierros = kierroksen numero
    - Kysyy pelaajalta jokaisen heiton pisteet 

- Funktio "pisteenlasku(pelaajat)":
    - Yksi parametri:
        1. pelaajat = lista pelaajista (listassa pelaajien nimet ja pisteet)
    - Laskee jokaisen pelaajan lopputuloksen
    - Palauttaa pelaajan nimen ja lopputuloksen

- Funktio "lopputulos(lopputulokset)":
    - Yksi parametri:
        1. lopputulokset = pelaajan nimi ja lopputulos 
    - Tulostaa lopputulokset konsoliin
    - Laittaa lopputulokset keilaustulos.txt tiedostoon

- Funktio "keilailupeli":
    - Ei parametreja
    - Tämä funktio on pääohjelma
    - Tän funktion avulla muut funktiot onnistuu ja ohjelma ylipäätään toimii oikein


### Tiedostot:
- Kun 10 kierrosta on mennyt niin ohjelma tallentaa lopputulokset (pelaajien nimet ja loppupisteet) keilaustulos.txt tiedostoon
- Ohjelman aikana kaikkien pelaajien nimet ja pisteet tallennetaan listoihin ja sanakirjoihin. Mutta nämä tiedot ei tallennu tietokantoihin tms.


### Ajan käyttö
- Harjoitustehtävän idean suunnittelu: 30min
- Harjoitustehtävän toteutus: 4h
- README.md tiedoston toteutus: 45min


