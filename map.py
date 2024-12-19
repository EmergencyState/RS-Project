def funkc_map(data_folder):
    import pandas as pd   # datu analize
    import zipfile        # zip lasīšana
    import folium         # map izveide
    import os             # failu direktorijas atrašana
    import webbrowser     # map atveršana WEB
    import matplotlib.pyplot as plt    # vizualizācija
    from matplotlib.animation import FuncAnimation
    import matplotlib.colors as mcolors
    from matplotlib import colormaps   # heatmap

    # Get data to dataframe
 

    data_folder = data_folder.replace("validacija.zip", '')
    data_folder = data_folder.replace("marsruti.zip", '')
 
    dir = os.path.join(data_folder, 'marsruti.zip')
    dir = dir.replace("\\", '/')

    zf = zipfile.ZipFile(dir)  
    routes = (pd.read_csv(zf.open('routes.txt'))).iloc[:,[0,1,2,4]]                             # read + kolonnu filtrs
    #trips = (pd.read_csv(zf.open('trips.txt'))).iloc[:,[0,2,3,5,6]]                             # read + kolonnu filtrs
    stops = (pd.read_csv(zf.open('stops.txt'))).iloc[:,[0,2,4,5]]                               # read + kolonnu filtrs
    shapes =  (pd.read_csv(zf.open('shapes.txt'))).iloc[:,[0,1,2,3]]                            # read + kolonnu filtrs
    #stop_times =  (pd.read_csv(zf.open('stop_times.txt')))   

    #user input
    dict1 = {'Autobuss': 3, 'Tramvajs': 900, 'Trolejbuss': 800,}
    while True:
        tr_veids = input(f'Ievadiet transporta veidu {list(dict1.keys())}: ')
        if tr_veids in dict1:
            tr_veids_new = dict1[tr_veids]
            break
        print("Ievadītie dati nepareizi (ievādiet korekto transporta veidu)")
    tr_num = input("Ievadiet maršruta numuru: ")
    route =  routes[(routes['route_type'] == tr_veids_new) & (routes['route_short_name'] == int(tr_num) )]
    print(f'Tavs maršŗuts ir {tr_num} {tr_veids}: "{route['route_long_name'].to_string(index=False)}"')

    dict2 = {'From': '_a-b', 'To': '_b-a'}
    while True:
        tr_virziens = input("Ievadiet maršruta virzienu (From, To): ")
        if tr_virziens in dict2:
            suffix = dict2[tr_virziens]
            break
        print("Ievadītie dati nepareizi (ievādiet korekto maršruta virzienu)")
    
    # map izveide
    marsrut = route['route_id'].to_string(index=False) + suffix
    user_shape_all = shapes[(shapes['shape_id'] == marsrut)] 

    user_shape = user_shape_all.merge(stops, left_on = ['shape_pt_lat', 'shape_pt_lon'],  right_on = ['stop_lat', 'stop_lon'], how='inner')


    center =  [56.946285, 24.105078] # [56.941984, 24.114647]
    user_map = folium.Map(location=center,  zoom_start=12,  tiles="OpenStreetMap")

    for i in range(len(user_shape)):
        if user_shape.iloc[i, 3] == 1:
            folium.Marker(location=[user_shape.iloc[i, 1], user_shape.iloc[i, 2]], popup='START '+user_shape.iloc[i,5], icon=folium.Icon(color='red')
                     ).add_to(user_map)
        else:
            folium.Marker(location=[user_shape.iloc[i, 1], user_shape.iloc[i, 2]], popup=user_shape.iloc[i,5]
                    ).add_to(user_map)

    for i in range(len(user_shape_all)):
        prev = i - 1
        if user_shape_all.iloc[i, 3] > 1 and prev != 1:
            folium.PolyLine(
                locations=[(user_shape_all.iloc[i, 1], user_shape_all.iloc[i, 2]), (user_shape_all.iloc[prev, 1], user_shape_all.iloc[prev, 2])]
                ).add_to(user_map)
            
    user_map.save('image.html')
    webbrowser.open_new_tab('image.html') 
    print('Izvēlēta transports maršruts vizuālizēts WEB lapā')
    print('Lūdzu uzgaidīt, notiek datu analīze, gatavojas analīanimācija')


    dir2 = os.path.join(data_folder, 'validacija.zip')
    dir2 = dir2.replace("\\", '/')
    
    # validācjas faila analize

    zf = zipfile.ZipFile(dir2) #(".../data/09_2024/validacija.zip") 
    lst = []
    for i in zf.namelist():
        df_file = pd.read_csv(zf.open(i))
        lst.append(df_file)  
    df = pd.concat(lst) 
    df.reset_index(drop=True, inplace=True)
    
    
    # # Darbs ar kolonnam
    df['Laiks'] = pd.to_datetime(df['Laiks'], dayfirst=True)  # Konvertē 'Laiks' kolonnu uz datetime
    #df['Laiks'] = pd.to_datetime(df['Laiks'])  
    df['Stunda'] = df['Laiks'].dt.hour  # Izvelk stundu no laika zīmoga
    df['Datums'] = df['Laiks'].dt.strftime('%d').astype(int)  # Izvelk dienu no laika zīmoga
    df['GarNr'] = df['GarNr'].astype(str) 
    df['TMarsruts'] = df['TMarsruts'].str.split(' ', expand=True)[1]
    
    dict3 = {'From': 'Forth', 'To': 'Back'}
    df = df[(df['TMarsruts'] == tr_num) & (df['TranspVeids'] == tr_veids) & (df['Virziens'] == dict3[tr_virziens]) ]

    
    # var anakizēt datus par 1 dienu
    # table = pd.pivot_table(df, values='ValidTalonaId', index=['GarNr'],
    #                         columns=['Laiks_H'],  aggfunc="count", fill_value=0)
    # #table
    # table.style.background_gradient(cmap="Reds")   # https://matplotlib.org/2.0.2/examples/color/colormaps_reference.html  
    # #table.sort_values(by=['Back'], ascending=False)
    

    # Vaidāciju skaits katrai dienai un katrai stundai 
    daily_hourly_counts = df.groupby(['Datums', 'Stunda']).size().reset_index(name='Counts')
    
    # Animacijas izvetde (tukša)
    fig, ax = plt.subplots(figsize=(12, 6))

    # heatmap - krāsu kartes sagatavošana, pamatojoties uz vērtību Skaits  - heatmap  (noslodze)
    norm = mcolors.Normalize(vmin=0, vmax=daily_hourly_counts['Counts'].max())
    color_map = colormaps['OrRd']  # Получаем палитру "OrRd"

    def update(day):
        ax.clear()
        daily_data = daily_hourly_counts[daily_hourly_counts['Datums'] == unique_dates[day]]
        # Используем цвет на основе количества валидаций
        ax.bar(daily_data['Stunda'], daily_data['Counts'],
        color=[color_map(norm(count)) for count in daily_data['Counts']])
        ax.set_title(f"Validāciju skaits {tr_num}. {tr_veids} — datums: {unique_dates[day]}")
        ax.set_xlabel("Stunda")
        ax.set_ylabel("Validāciju skaits")
        ax.set_xlim(-1, 24)  # Ограничиваем ось X от 0 до 23
        ax.set_ylim(0, daily_hourly_counts['Counts'].max() + 10)
    
    unique_dates = sorted(daily_hourly_counts['Datums'].unique())
    ani = FuncAnimation(fig, update, frames=len(unique_dates), repeat=False)
    
    # Animācijas saglabāšana
    ani.save(f"Datu analize {tr_num}. {tr_veids}.gif", writer='pillow', fps=1)
    print("Paldies! Lai pabeigt programmu jāaizver animaciju.\n")
    plt.show()