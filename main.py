import os  # Modulis darbam ar failu sistēmu. 
import shutil  # Modulis failu un direktoriju kopēšanai. https://docs.python.org/3/library/shutil.html
import subprocess  # Modulis ārējo programmu palaišanai. https://docs.python.org/3/library/subprocess.html
import requests  # Modulis HTTP pieprasījumu veikšanai. https://pypi.org/project/requests/

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
    data_folder = "data"  # Norāda direktorijas nosaukumu, kurā jāglabā dati.

    if not os.path.exists(data_folder):  # Pārbauda, vai "data" direktorija eksistē.
        os.makedirs(data_folder)  # Ja direktorija neeksistē, to izveido.

    folders = []  # Izveido sarakstu, kurā tiks saglabātas mapes.
    for folder in os.listdir(data_folder):  # Iterē caur visiem failiem un mapēm "data" direktorijā.
        if os.path.isdir(os.path.join(data_folder, folder)):  # Pārbauda, vai ir kāds elements mape.
            folders.append(folder)  # Pievieno mapi sarakstam.
    return folders  # Atgriež sarakstu ar mapēm.


 # Funkcija: Pārbauda, vai "analysis.ipynb" eksistē, un, ja tas neatrodas galamērķa mapē, to kopē no saknes direktorijas. https://www.geeksforgeeks.org/python-shutil-copyfile-method/ https://stackabuse.com/how-to-copy-files-in-python/
def check_and_copy_notebook(destination_folder):
    notebook_file = "analysis.ipynb"  # Norāda faila nosaukumu, kas jāpārbauda.
    destination_path = os.path.join(destination_folder, notebook_file)  # Izveido pilno ceļu galamērķa mapē.

    if not os.path.exists(notebook_file):  # Pārbauda, vai "analysis.ipynb" eksistē saknes direktorijā.
        print("Nav atrasts faila 'analysis.ipynb' oriģināls. Pārbaudiet, vai tas eksistē saknes direktorijā.")
        return None  # Atgriež None, ja fails neeksistē.

    if not os.path.exists(destination_path):  # Pārbauda, vai fails jau eksistē galamērķa mapē.
        print("Kopēju 'analysis.ipynb' uz datu mapi...")  # Informē lietotāju par kopēšanas procesu.
        shutil.copy(notebook_file, destination_path)  # Kopē failu uz galamērķa mapi. https://stackoverflow.com/questions/123198/how-to-copy-files

    return destination_path  # Atgriež ceļu uz nokopēto failu.

# Galvenā funkcija: Pārvalda programmas loģiku un lietotāja izvēles. https://www.geeksforgeeks.org/python-main-function/
def main():
    print("Laipni līdz programmas darbībā!") 

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
            break  # Pārtrauc ciklu pēc datu lejupielādes.

        elif choice == "2":
            # Ja lietotājs izvēlas izmantot jau esošos datus:
            existing_folders = get_existing_data_folders()  # Saņem esošo datu mapju sarakstu.

            if not existing_folders:  # Pārbauda, vai ir pieejamas datu mapes.
                print("Nav atrastas saglabātas datu mapes. Lūdzu, lejupielādējiet jaunus datus.")  # Informē par datu mapju trūkumu.
                continue  # Atgriežas pie izvēlnes, lai lietotājs varētu izvēlēties citu darbību.

            print("Pieejamās datu mapes:")  # Izdrukā pieejamo mapju sarakstu.
            for idx, folder in enumerate(existing_folders, start=1):  # Iterācija: izdrukā katru pieejamo mapi.
                print(f"{idx}. {folder}")

            folder_choice = input("Izvēlieties mapi (ievadiet numuru): ")  # Pieprasa lietotājam izvēlēties mapi.

            if folder_choice.isdigit() and 1 <= int(folder_choice) <= len(existing_folders):  # Pārbauda, vai ievadītā izvēle ir derīga.
                data_folder = os.path.join("data", existing_folders[int(folder_choice) - 1])  # Saņem izvēlētās mapes ceļu.
                print("Izvēlētā mape:", data_folder)  # Informē lietotāju par izvēlēto mapi.
                break  # Pārtrauc ciklu pēc mapes izvēles.
            else:
                print("Nederīga izvēle. Lūdzu, mēģiniet vēlreiz.")  # Informē par nederīgu ievadi.

        elif choice == "3":
            # Ja lietotājs izvēlas iziet no programmas:
            print("Uzredzēšanos!")  # Izdrukā atvadu ziņojumu.
            return  # Izbeidz programmas izpildi.

        else:
            print("Nederīga izvēle. Lūdzu, mēģiniet vēlreiz.")  # Informē par nederīgu izvēli.

    # Pārbauda un kopē notebook failu, ja nepieciešams:
    notebook_path = check_and_copy_notebook(data_folder)  # Pārbauda, vai "analysis.ipynb" ir pieejams galamērķa mapē.

    if notebook_path is None:  # Pārbauda, vai fails tika veiksmīgi nokopēts.
        print("Nevar turpināt. Nav pieejams 'analysis.ipynb'.")  # Informē par kļūmi.
        return  # Izbeidz programmas izpildi.

    # Atzīmē notebook kā uzticamu un startē Jupyter Lab:
    subprocess.run(["jupyter", "trust", notebook_path])  # Palaiž komandu, lai atzīmētu notebook kā uzticamu.
    print("Startēju Jupyter Lab...")  # Informē, ka tiek startēts Jupyter Lab.
    subprocess.run(["jupyter", "lab", notebook_path])  # Palaiž Jupyter Lab ar konkrēto notebook failu.

if __name__ == "__main__":
    main()  # Izsauc galveno funkciju, lai uzsāktu programmas darbību.
