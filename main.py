import os
import requests
import subprocess

def download_file(url, folder, file_name):
#Lejupielādē failu no norādītās saites un saglabā to mapē ar norādīto nosaukumu.

    file_path = os.path.join(folder, file_name)
    print(f"Lejupielādēju ZIP arhīvus no saites {url}...")
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Fails veiksmīgi saglabāts mapē:  {file_path}")
    else:
        print(f"Neizdevās lejupielādēt failu no {url}. Statusa kods: {response.status_code}")
    return file_path

# Galvenā programmas daļa
print("Programma, kas lejupielādē datus un startē Jupiter Lab")
etalons_url = input("Ievadiet E-Talona validācijas datu saiti: ")
marsruti_url = input("Ievadiet Maršrutu saraksta saiti: ")
month = input("Ievadiet mēnesi (piemēram, 01): ")
year = input("Ievadiet gadu (piemēram, 2024): ")

# Izveido mapi datu saglabāšanai
folder_name = f"{month}_{year}"
folder_path = os.path.join("data", folder_name)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Definē failu nosaukumus
validacija_file_name = "validacija.zip"
marsruti_file_name = "marsruti.zip"

# Lejupielādē failus ar fiksētiem nosaukumiem
etalons_zip = download_file(etalons_url, folder_path, validacija_file_name)
marsruti_zip = download_file(marsruti_url, folder_path, marsruti_file_name)

# Parāda, kur faili ir saglabāti
print(f"Visi faili ir veiksmīgi lejupielādēti un saglabāti mapē:")
print(f" - {etalons_zip}")
print(f" - {marsruti_zip}")

# Startē JupyterLab
print(f"Startē: JupyterLab...")
subprocess.Popen(["jupyter", "lab"], cwd=os.getcwd())
