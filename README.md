# Sabiedriskā Transporta Datu Analīze

Šis projekts veic sabiedriskā transporta datu analīzi, pamatojoties uz Rīgas sabiedriskā transporta biļešu validācijas datiem pēc lietotāja izvēles.

Programma nodrošina datu vizualizāciju izvēlētajam maršrutam un izveido grafisku vizualizāciju, kas parāda, kurā katra mēneša dienā un stundā ir visvairāk veiktas validācijas.

## Projekta struktūra

Projekts sastāv no šādām direktorijām un failiem:

* src/
 * main.py
   * src/funkc
      * map.py
 
## Datu avoti
Datus lietotājs izvēlās no atvērto datu mājas lapas. 

Validācijas pieejamas šeit: [Validācija](https://data.gov.lv/dati/lv/dataset/e-talonu-validaciju-dati-rigas-satiksme-sabiedriskajos-transportlidzeklos)

Marsruti pieejami šeit: [Maršruti](https://data.gov.lv/dati/lv/dataset/marsrutu-saraksti-rigas-satiksme-sabiedriskajam-transportam)


## Funkcionalitāte
Programmas funkcionalitāte ir aplūkojama šeit: [Blokshēma](https://github.com/EmergencyState/Kursa-darbs/blob/Main/blokshema.png )


## Lietošanas instrukcija

Lai startētu programmu, izmantojot Python interpretatoru, jāizpilda komanda šādā veidā: python src/main.py.


Lietotājs tiek aicināts izvēlēties darbību no trīs opcijām:
1. darbība: Lejupielādēt jaunus datus:

Lietotājs tiek lūgts ievadīt E-Talona un Maršrutu datu URL, kā arī mēnesi un gadu.
Programma  izveido jaunu mapi data direktorijā ar nosaukumu month_year.
Dati tiek lejupielādēti attiecīgajās zip failu arhīvās un saglabāti izveidotajā mapē

2. darbība: Izmantot esošos datus

Programmā tiek izveidots esošo datu mapju saraksts.
Ja nav pieejamas datu mapes, lietotājs tiek informēts un var izvēlēties citu darbību.
Lietotājs izvēlas esošo mapi, ievadot tās numuru.

3. darbība: Iziet no programmas
Ja lietotājs izvēlas iziet no programmas, programma izdrukā atvadu ziņojumu un izbeidz izpildi.
