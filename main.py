import pandas as pd
import zipfile
import requests
import os


#Saite uz  zip arhīvu
zip_url_site = input("Ievadiet saiti: ")

# Mapes izveide un  definēšana, kur lejupieladesim datus
data_foler = "data"
os.makedirs(data_foler,exist_ok=True)

#Lejupielādējam datus
response = requests.get(zip_url_site)
if response.status_code == 200:
    print("Lejupielādē ZIP failu...")
    with open("./data/data.zip", "wb") as file:
        file.write(response.content)
        print("Fails lejupieladets")
else:
    print("Nesanaca lejupieladet")
# Definejam zip atrasanas 
zip_data_path= os.path.join(data_foler,"data.zip")

# Get data to dataframe
zf = zipfile.ZipFile(zip_data_path, 'r') 

df = pd.read_csv(zf.open('ValidDati01_10_24.txt'))
 
#Darbs ar data frame

data = df

data

data['Parks'] = pd.to_numeric(df['Parks'].str.split(' ', expand=True)[0])
data['Marsr_FROM'] = df['MarsrNos'].str.split('-', expand=True)[0]
data['Marsr_TO'] = df['MarsrNos'].str.split('-', expand=True)[1]
data['TMarsruts'] = df['TMarsruts'].str.split(' ', expand=True)[1]
data['Datums'] = pd.to_datetime(df['Laiks']).dt.date
data['Laiks'] = pd.to_datetime(df['Laiks']).dt.time
data['GarNr'] = pd.to_numeric(df['GarNr'])
data['TMarsruts'] = pd.to_numeric(df['TMarsruts'])
data['ValidTalonaId'] = pd.to_numeric(df['ValidTalonaId'])

df_filtered = df[(data['GarNr'] == 78637) & (data['Virziens'] == 'Back')  ]
df_filtered

print(data)

