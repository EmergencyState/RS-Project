import os  # Modulis darbam ar failu sistēmu. 
import requests  # Modulis HTTP pieprasījumu veikšanai. https://pypi.org/project/requests/

from funkc.map import funkc_map as map


# Funkcija download_file : Lejupielādē failu no norādītās interneta adreses un saglabā to norādītajā mapē ar konkrētu nosaukumu. https://oxylabs.io/blog/python-requests
def download_file(url, folder, file_name):
    file_path = os.path.join(folder, file_name)  # Izveido pilno faila ceļu, apvienojot mapi un faila nosaukumu.
    print("Lejupielādēju failu no:", url)  # Izdrukā informāciju par lejupielādējamo failu.
    response = requests.get(url)  # Veic HTTP GET pieprasījumu uz norādīto URL, lai lejupielādētu failu.
    if response.status_code == 200:  # Pārbauda, vai pieprasījums bija veiksmīgs (statusa kods 200).
        with open(file_path, "wb") as file:  # Atver failu rakstīšanai binārajā režīmā.
            file.write(response.content)  # Ieraksta lejupielādēto saturu failā.
        print("Fails saglabāts:", file_path)  # Paziņo, ka fails ir veiksmīgi saglabāts un norāda kur.
    else:
        print("Kļūda! Neizdevās lejupielādēt failu. Statusa kods:", response.status_code)  # Izdrukā kļūdas paziņojumu, ja response code nav 200 .
    return file_path  # Atgriež ceļu uz lejupielādēto failu.

# Funkcija get_existing_data_folders: Atgriež sarakstu ar mapēm, kas atrodas "data" direktorijā. https://builtin.com/data-science/python-list-files-in-directory
def get_existing_data_folders():
    # Funkcija: Atgriež sarakstu ar mapēm, kas atrodas "data" direktorijā.
    data_folder = os.path.join("data")  # Norāda direktorijas nosaukumu, kurā jāglabā dati.

    if not os.path.exists(data_folder):  # Pārbauda, vai "data" direktorija eksistē.
        os.makedirs(data_folder)  # Ja direktorija neeksistē, to izveido.

    folders = []  # Izveido sarakstu, kurā tiks saglabātas mapes.
    for folder in os.listdir(data_folder):  # Iterē caur visiem failiem un mapēm "data" direktorijā.
        if os.path.isdir(os.path.join(data_folder, folder)):  # Pārbauda, vai ir kāds elements mape.
            folders.append(folder)  # Pievieno mapi sarakstam.
    return folders  # Atgriež sarakstu ar mapēm.


print("Laipni lūdzam programmā!") 

while True:  # Cikls: Ļauj lietotājam atkārtoti izvēlēties darbību, līdz programma tiek aizvērta.
    print("Izvēlieties darbību:")
    print("1 - Lejupielādēt jaunus datus") 
    print("2 - Izmantot esošos datus") 
    print("3 - Iziet no programmas")  

    choice = input("Ievadiet darbības numuru: ")  # Saņem lietotāja izvēlēto numuru/darbibu.

    if choice == "1":
        # Ja lietotājs izvēlas lejupielādēt datus:
        etalons_url = input("Ievadiet E-Talona datu saiti: ")  # Pieprasa lietotājam ievadīt datu URL.
        marsruti_url = input("Ievadiet Maršrutu datu saiti: ")  # Pieprasa ievadīt otru datu URL.
        month = input("Ievadiet mēnesi (piem., 01): ")  # Pieprasa norādīt mēnesi.
        year = input("Ievadiet gadu (piem., 2024): ")  # Pieprasa norādīt gadu.

        # Izveido datu mapi:
        folder_name = f"{month}_{year}"  # Izveido mapes nosaukumu, izmantojot ievadīto mēnesi un gadu.
        data_folder = os.path.join("data", folder_name)  # Izveido pilno ceļu uz datu mapi.

        if not os.path.exists(data_folder):  # Pārbauda, vai mape eksistē.
                os.makedirs(data_folder)  # Ja mape neeksistē, to izveido.

        # Lejupielādē failus:
        download_file(etalons_url, data_folder, "validacija.zip")  # Lejupielādē pirmo failu.
        download_file(marsruti_url, data_folder, "marsruti.zip")  # Lejupielādē otro failu.

        print("Dati veiksmīgi lejupielādēti un saglabāti mapē:", data_folder)  # Informē lietotāju par veiksmīgu lejupielādi.
        map(data_folder) 
        break  # Pārtrauc ciklu pēc datu lejupielādes.


    elif choice == "2":
        # Ja lietotājs izvēlas izmantot jau esošos datus:
        existing_folders = get_existing_data_folders()  # Saņem esošo datu mapju sarakstu.

        if not existing_folders:  # Pārbauda, vai ir pieejamas datu mapes.
                print("Nav atrastas saglabātas datu mapes. Lūdzu, lejupielādējiet jaunus datus.")  # Informē par datu mapju trūkumu.
                continue  # Atgriežas pie izvēlnes, lai lietotājs varētu izvēlēties citu darbību.

        print("Pieejamās datu mapes:")  # Izdrukā pieejamo mapju sarakstu.
        for g, folder in enumerate(existing_folders, start=1):  # Iterācija: izdrukā katru pieejamo mapi.
                print(f"{g}. {folder}")

        folder_choice = input("Izvēlieties mapi (ievadiet numuru): ")  # Pieprasa lietotājam izvēlēties mapi.

        if folder_choice.isdigit() and 1 <= int(folder_choice) <= len(existing_folders):  # Pārbauda, vai ievadītā izvēle ir derīga.
                data_folder = os.path.join("data", existing_folders[int(folder_choice) - 1])  # Saņem izvēlētās mapes ceļu.
                print("Izvēlētā mape:", data_folder)  # Informē lietotāju par izvēlēto mapi.
                map(data_folder)
                #break  # Pārtrauc ciklu pēc mapes izvēles.
        else:
            print("Nederīga izvēle. Lūdzu, mēģiniet vēlreiz.")  # Informē par nederīgu ievadi.

    elif choice == "3":
    # Ja lietotājs izvēlas iziet no programmas:
        print("Uzredzēšanos!")  # Izdrukā atvadu ziņojumu.
        break # Izbeidz programmas izpildi.
    else:
        print("Nederīga izvēle. Lūdzu, mēģiniet vēlreiz.")  # Informē par nederīgu izvēli.
