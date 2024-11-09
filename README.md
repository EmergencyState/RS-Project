# Sabiedriskā Transporta Datu Analīze

Šis projekts veic sabiedriskā transporta datu analīzi, pamatojoties uz Rīgas sabiedriskā transporta biļešu validācijas datiem oktobra mēnesī 2024. gada.
Analīzes mērķis ir noteikt populārākos maršrutus, noslogotākās stundas un veikt datu vizualizāciju. 

## Projekta struktūra

Projekts sastāv no šādām direktorijām un failiem:

* data/
  * 01_10_2024.txt
  * 02_10_2024.txt
  * .... līdz 31_10_2024.txt
* analysis.py  

## Datu avoti
Datus esam ieguvuši no Latvijas atvērto datu portāla. Datos ir apkopoti 2024. gada oktobra e-talona validacijas dati no Rīgas satiksmes. [Atvērtie Dati ](https://data.gov.lv/dati/lv/dataset/e-talonu-validaciju-dati-rigas-satiksme-sabiedriskajos-transportlidzeklos/resource/f6106b74-d4c0-4c57-b1eb-c8f38e628b8a?inner_span=True)

Dati sevī iekļauj tādus parametrus ka: 
* Ieraksta unikalo identifikacijas numuru ar lauka nosaukmu [Ier_ID]
* Transporta parks [Parks]
* Transporta veidu [TranspVeids]
* Transportlīdzekļa garo numuru [GarNr]
* Maršruta nosaukumu [MarsNos]
* Maršruta kodu [TMarsruts]
* Brauciena Virzienu [Virziens]
* Biļetes validācijas ID [ValidTalonaId]
* Laiku, kad biļete ir validēta [Laiks]


## Funkcionalitāte

Priekš funkcionalitātes tiks izmantots Pandas rīks, kas ļaus apstrādāt datus un veikt to primāro analīzi. [Pandas](https://pandas.pydata.org/)

Veiksim datu vizualizāciju ar [Scikit](https://scikit-learn.org/stable/)


## Lietošanas instrukcija
