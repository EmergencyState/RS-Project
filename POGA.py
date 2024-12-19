from tkinter import *
from tkinter import ttk
import os  # Modulis darbam ar failu sistēmu. 
import shutil  # Modulis failu un direktoriju kopēšanai. https://docs.python.org/3/library/shutil.html
import subprocess  # Modulis ārējo programmu palaišanai. https://docs.python.org/3/library/subprocess.html
import requests  # Modulis HTTP pieprasījumu veikšanai. https://pypi.org/project/requests/
import pandas as pd
import zipfile
#from funkc.map import funkc_map


def next_step_1():
    show_action["text"] = "Izvēlēta darbība: " + combo.get()
    action_key["text"] =[x for x in combo_list.keys() if combo_list[x] == combo.get()]  # vajag datiu importam
    combo.grid_forget()  # pec apstiprinajuma paslept lauku
    btn.grid_forget()    # pec apstiprinajuma paslept lauku
    show_action.grid(row=1, column=0)
    btn2.grid(row=1, column=4)    # poga Turpināt  -> next_step_3
    btn3.grid(row=1, column=5)    # poga pārtraukt


# Funkcija download_file : Lejupielādē failu no norādītās interneta adreses un saglabā to norādītajā mapē ar konkrētu nosaukumu. https://oxylabs.io/blog/python-requests
def download_file(url, folder, file_name):
    file_path = os.path.join(folder, file_name)  # Izveido pilno faila ceļu, apvienojot mapi un faila nosaukumu.
    #print("Lejupielādēju failu no:", url)  # Izdrukā informāciju par lejupielādējamo failu.
    response = requests.get(url)  # Veic HTTP GET pieprasījumu uz norādīto URL, lai lejupielādētu failu.
    if response.status_code == 200:  # Pārbauda, vai pieprasījums bija veiksmīgs (statusa kods 200).
        with open(file_path, "wb") as file:  # Atver failu rakstīšanai binārajā režīmā.
            file.write(response.content)  # Ieraksta lejupielādēto saturu failā.
        dwnl_1 = Label(text = (f"Faili saglabāti: {folder}"), font=('Times New Roman', 12) ).grid(row=18, column=1)    # Paziņo, ka fails ir veiksmīgi saglabāts un norāda kur.
    else:
        dwnl_2 = Label(text = (f"Kļūda! Neizdevās lejupielādēt failu. Statusa kods: ", response.status_code), font=('Times New Roman', 12), fg="red" ).grid(row=19, column=1)  # Izdrukā kļūdas paziņojumu, ja response code nav 200 .
    #return file_path  # Atgriež ceļu uz lejupielādēto failu.

def data_to_download_file():
    btn6.grid_forget()
    btn3.grid_forget() 
    folder_name = month_input["text"] + '_' + year_input["text"]        # Izveido mapes nosaukumu, izmantojot ievadīto mēnesi un gadu.
    data_folder = os.path.join("data", folder_name)                     # Izveido pilno ceļu uz datu mapi.
    if not os.path.exists(data_folder):                                 # Pārbauda, vai mape eksistē.
        os.makedirs(data_folder)                                        # Ja mape neeksistē, to izveido.
    download_file(etalons_url.get() , data_folder, "validacija.zip")    # Lejupielādē pirmo failu.
    download_file(marsruti_url.get(), data_folder, "marsruti.zip")      # Lejupielādē otro failu.
    
    etalons_url.grid_forget()    # pec apstiprinajuma paslept lauku
    marsruti_url.grid_forget()   # pec apstiprinajuma paslept lauku
    month.grid_forget()          # pec apstiprinajuma paslept lauku
    year.grid_forget()           # pec apstiprinajuma paslept lauku
    btn5.grid_forget()           # pec apstiprinajuma paslept lauku
    return folder_name


 
def next_step_2(): 
    btn5.grid_forget() 
    etalons_url.grid_forget() 
    marsruti_url.grid_forget() 
    month.grid_forget() 
    year.grid_forget() 

    etalon_input["text"] = etalons_url.get()
    etalon_input.grid(row=7, column=1)
    marsruti_input["text"] = marsruti_url.get()
    marsruti_input.grid(row=8, column=1)
    month_input["text"] = month.get()
    month_input.grid(row=9, column=1)
    year_input["text"] = year.get()
    year_input.grid(row=10, column=1)
    btn6.grid(row=12, column=4)        # Poga Turpināt  - > command=download_file
    btn3.grid(row=12, column=5)        # Poga Pārtraukt - > command=stop

def exit():
    for widget in window.winfo_children():
        widget.destroy()
    title_by = Label(text = "Uzredzēšanos!", width=30, height=5, justify="left", font=('Times New Roman', 15)).grid(row=0, column=0)
    btn4 = ttk.Button(text = "Iziet no programmas" , command=click_to_close)
    btn4.configure(width=25)
    btn4.grid(row=0, column=10)

def stop():
    text_stop["text"] = "Progrāmma apstādināta!"
    btn2.grid_forget()
    btn3.grid_forget()
    btn6.grid_forget()
    text_stop.grid(row=20, column=4)

def click_to_close():
    window.destroy()

def next_step_3():
    choice["text"] = action_key["text"] 
    if choice["text"] == '3':                          # Ja lietotājs izvēlas iziet no programmas:
        exit()
    elif choice["text"] == '1':                        # Ja lietotājs izvēlas lejupielādēt datus:
        btn2.grid_forget()
        btn3.grid_forget()
        title_etalons_url.grid(row=7, column=0)
        etalons_url.grid(row=7, column=1)
        title_marsruti_url.grid(row=8, column=0)
        marsruti_url.grid(row=8, column=1)
        title_month.grid(row=9, column=0)
        month.grid(row=9, column=1)
        title_year.grid(row=10, column=0)
        year.grid(row=10, column=1)
        btn5.grid(row=12, column=10)            # Apstiprināt ievadi  ->  command=next_step_2
    
    elif choice["text"] == '2':                                        # Ja lietotājs izvēlas izmantot jau esošos datus:
        btn2.grid_forget()
        btn3.grid_forget() 
        data_folder = "data"                                        # Norāda direktorijas nosaukumu, kurā jāglabā dati.
        if not os.path.exists(data_folder):                         # Pārbauda, vai "data" direktorija eksistē.
            os.makedirs(data_folder)                                # Ja direktorija neeksistē, to izveido.
        folders = []                                                # Izveido sarakstu, kurā tiks saglabātas mapes.
        for folder in os.listdir(data_folder):                      # Iterē caur visiem failiem un mapēm "data" direktorijā.
            if os.path.isdir(os.path.join(data_folder, folder)):    # Pārbauda, vai ir kāds elements mape.
                folders.append(folder)                              # Pievieno mapi sarakstam.
  
        folder_list.set('Pieejamās datu mapes (lūdzu izvēlies vienu): ')
        folder_list.configure(width=45, state="readonly", values= folders)
        folder_list.grid(row=7, column=0)
        btn7.configure(width=25)
        btn7.grid(row=7, column=2)
        
    else:
        title_error = Label(text = "Nederīga izvēle. Lūdzu, mēģiniet vēlreiz!", width=30, height=5, justify="left", font=('Times New Roman', 15), fg="red").grid(row=5, column=1)
        btn3.grid_forget()
        btn2.grid_forget()

def next_step_4():
    btn7.grid_forget()
    folder_list.grid_forget()
    dir2 =  os.path.join("data", folder_list.get())
    dir_input2["text"] = "Izvēlēta mape: " + dir2
    dir_input2.grid(row=4, column=0)
    btn8.grid(row=4, column=4)     #poga Turpināt   command= xxx
    btn3.grid(row=4, column=5)


def xxx ():  # ja izvele ir no savas mapes
    btn8.grid_forget()
    btn3.grid_forget()
    title_by = Label(text = "Datu ielase", width=16, height=5, justify="left", font=('Times New Roman', 12)).grid(row=6, column=0)
    btn9.grid(row=6, column=1)


def read_data():
    btn9.grid_forget()
    dict1 = {3:'Autobuss', 900:'Tramvajs', 800:'Trolejbuss'}
    combo2= ttk.Combobox(state="readonly", values=list(dict1.values())) 
    combo2.set(value = 'Ievadiet transporta veidu: ')   # teksts pēc noklusējuma
    combo2.configure(width=45)
    combo2.grid(row=7, column=0)
    tr_num = ttk.Combobox(state="normal")
    title_nr = Label(text = "Ievadiet maršruta numuru (cipari):", width=25, height=5, justify="left", font=('Times New Roman', 12))
    title_nr.grid(row=7, column=1)
    tr_num.grid(row=7, column=2)
       
    full_dir = os.path.abspath(dir_input2["text"].replace("Izvēlēta mape: ", "")) 
    dir_to_data = os.path.join(full_dir,"marsruti.zip") 

    # Atbildes pieņemšanas poga un talako darbibu defiēšana   
    #funkc_map(dir_to_data, title_nr, combo2):
    def xxxx():
        btn10.grid_forget()
        print(dir_to_data)
        print(title_nr)
        print(title_nr)
        print(combo2.cget())
        print(combo2)

    btn10 = ttk.Button(text = "Apstiprnāt ievadi", command=xxxx )
    btn10.configure(width=25)
    btn10.grid(row=9, column=3)



# Definejam jauno logu (izmers, nosauums utt)
window = Tk()
window.title('Datu pieņemšana no lietotāja')
#window.geometry('1200x600')                           # loga izmērs mainas katu reizi
window.maxsize(1900, 600), window.minsize(1900, 600)   #definējam max un min lai loga izmers paliek nemainīgs

# Virsraksts
title = Label(text = "Laipni lūgti programmas darbībā!", width=30, height=5, justify="left", font=('Times New Roman', 15, 'bold')).grid(row=0, column=0)

# Darbību saraksts (dropdown list)
combo_list = {1:"1 - Lejupielādēt jaunus datus", 2: '2 - Izmantot esošos datus', 3 : '3 - Iziet no programmas'}
combo = ttk.Combobox(state="readonly", values=list(combo_list.values()))    # values = ["1 - Lejupielādēt jaunus datus", "2 - Izmantot esošos datus", "3 - Iziet no programmas"] 
combo.set('Izvēlieties darbību no saraksta')   # teksts pēc noklusējuma
combo.configure(width=45)
combo.grid(row=1, column=0)

# Atbildes pieņemšanas poga un talako darbibu defiēšana   
btn = ttk.Button(text = "Apstiprnāt ievadi", command=next_step_1 )
btn.configure(width=25)
btn.grid(row=1, column=1)

btn4 = ttk.Button(text = "Iziet no programmas" , command=click_to_close)
btn4.configure(width=25)
btn4.grid(row=0, column=10)

btn5 = ttk.Button(text = "Apstiprnāt ievadi" , command=next_step_2)
btn5.configure(width=25)

btn6 = ttk.Button(text = "Turpināt!", command = data_to_download_file)
btn6.configure(width=25)

show_action = ttk.Label(font=('Times New Roman', 12))
action_key = ttk.Label()

btn2 = ttk.Button(text = "Turpināt!" , command=next_step_3)
btn2.configure(width=25)
btn3 = ttk.Button(text = "Pārtraukt!" , command=stop)   # ka palais no sakuma ??
btn3.configure(width=35)

btn8 = ttk.Button(text = "Turpināt!", command= xxx)
btn8.configure(width=25)

choice = ttk.Label(font=('Times New Roman', 12))
text_stop = ttk.Label(font=('Times New Roman', 15))

title_etalons_url = Label(text = "Ievadiet E-Talona datu saiti: ", width=30, justify="left", font=('Times New Roman', 12))
etalons_url = ttk.Entry()
etalons_url.configure(width=50)
title_marsruti_url = Label(text = "Ievadiet Maršrutu datu saiti: ", width=30, justify="left", font=('Times New Roman', 12))
marsruti_url = ttk.Entry()
marsruti_url.configure(width=50)
title_month = Label(text = "Ievadiet mēnesi (piem., 01): ", width=30, justify="left", font=('Times New Roman', 12))
month = ttk.Entry()
month.configure(width=10)
title_year = Label(text = "Ievadiet gadu (piem., 2024): ", width=30, justify="left", font=('Times New Roman', 12))
year = ttk.Entry()
year.configure(width=10)

etalon_input = ttk.Label()
marsruti_input = ttk.Label()
month_input = ttk.Label()
year_input = ttk.Label()
dir_input2 = ttk.Label()


btn9 = ttk.Button(text = "Apstiprnāt darbību", command=(read_data))  # read data
data_folder = ttk.Label()

btn7 = ttk.Button(text = "Apstiprnāt ievadi", command=next_step_4)
folder_list = ttk.Combobox()    


#Kopeja jauna loga izvade
window.mainloop()


