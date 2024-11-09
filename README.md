# Sabiedriskā Transporta Datu Analīze

Šis projekts veic sabiedriskā transporta datu analīzi, pamatojoties uz Rīgas sabiedriskā transporta biļešu validācijas datiem oktobra mēnesī 2024. gada.
Analīzes mērķis ir noteikt populārākos maršrutus, noslogotākās stundas u.t.t.

## Projekta struktūra

Projekts sastāv no šādām direktorijām un failiem:

data/                    # Sākotnējie dati (31 .txt fails, katrs pārstāv vienu dienu)
*01_10_2024.txt
*02_10_2024.txt
*līdz 31_10_2024.txt
analysis.py  

## Datu avoti
Datus esam ieguvuši no Latvijas atvērto datu portāla. Dators ir apkopoti 2024. gada oktobra e-talona validacijas dati no Rīgas satiksmes. 

https://data.gov.lv/dati/lv/dataset/e-talonu-validaciju-dati-rigas-satiksme-sabiedriskajos-transportlidzeklos/resource/f6106b74-d4c0-4c57-b1eb-c8f38e628b8a?inner_span=True


## Funkcionalitāte

Priekš funkcionalitātes tiks izmantots Pandas rīks, kas ļaus apstrādāt datus un veikt to primāro analīzi. https://pandas.pydata.org/

Veiksim datu vizualizāciju ar https://scikit-learn.org/stable/

## Lietošanas instrukcija
