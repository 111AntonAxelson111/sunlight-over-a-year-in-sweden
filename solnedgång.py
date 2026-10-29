"""

data:
Stationsnamn;Stationsnummer;Stationsnät;Mäthöjd (meter över marken)
Stockholm Sol;98735;SMHIs stationsnät;2.0

Parameternamn;Beskrivning;Enhet
Global Irradians (svenska stationer);medelvärde 1 timma, varje timme;watt per kvadratmeter
Solskenstid;summa 1 timme, 1 gång/tim;sekund

Tidsperiod (fr.o.m);Tidsperiod (t.o.m);Höjd (meter över havet);Latitud (decimalgrader);Longitud (decimalgrader)
1983-01-01 00:00:00;2026-10-14 22:20:26;41.0;59.3534;18.0634

Datum;Tid (UTC);Global Irradians (svenska stationer);Kvalitet;Solskenstid;Kvalitet;;Tidsutsnitt:
1983-01-01;00:00:00;0.00;G;0;G;;Kvalitetskontrollerade historiska data (utom de senaste 3 mån)
1983-01-01;01:00:00;0.00;G;0;G;;Tidsperiod (fr.o.m.) = 1983-01-01 00:00:00 (UTC)
1983-01-01;02:00:00;0.00;G;0;G;;Tidsperiod (t.o.m.) = 2026-07-01 06:00:00 (UTC)
1983-01-01;03:00:00;0.00;G;0;G;;Samplingstid = 1 timme
1983-01-01;04:00:00;0.00;G;0;G;;Kvalitetskoderna:
1983-01-01;05:00:00;0.00;G;0;G;;Grön (G) = Kontrollerade och godkända värden.
1983-01-01;06:00:00;0.00;G;0;G;;Gul (Y) = Misstänkta eller aggregerade värden. Grovt kontrollerade arkivdata och okontrollerade realtidsdata (senaste 2 tim).
1983-01-01;07:00:00;0.00;G;0;G;;Nätinformation:
1983-01-01;08:00:00;0.40;G;0;G;;SMHIs Stationsnät: Data samlas in och lagras i SMHIs databaser. Data kvalitetskontrolleras vilket innebär att felaktiga data korrigeras och att databortfall kompletteras utifrån expertbedömning där det är möjligt. De flesta stationerna övervakas, inspekteras och underhålls löpande av SMHI.
1983-01-01;09:00:00;8.70;G;0;G;;Övriga stationer: Data samlas in och lagras i SMHIs databaser. Datakvaliteten är för SMHI okänd då SMHI varken utför kvalitetskontroll på data eller inspektioner på stationerna.
1983-01-01;10:00:00;17.10;G;0;G;;Möjliga orsaker till saknade data:
1983-01-01;11:00:00;27.40;G;0;G;;– stationen eller givaren har varit ur funktion.
1983-01-01;12:00:00;19.70;G;0;G;;– stationen har endast levererat värden med kvalitetskod Röd (R). Dessa levereras ej.
1983-01-01;13:00:00;9.30;G;0;G
1983-01-01;14:00:00;3.50;G;0;G
1983-01-01;15:00:00;0.10;G;0;G
...
1984-03-14;23:00:00;0.00;G;0;G
1984-03-15;00:00:00;0.00;G;0;G
1984-03-15;01:00:00;0.00;G;0;G
1984-03-15;02:00:00;0.00;G;0;G
1984-03-15;03:00:00;0.00;G;0;G
1984-03-15;04:00:00;0.00;G;0;G
1984-03-15;05:00:00;0.00;G;0;G
1984-03-15;06:00:00;13.20;G;0;G
1984-03-15;07:00:00;43.00;G;0;G
1984-03-15;08:00:00;102.10;G;0;G
1984-03-15;09:00:00;172.30;G;18;G
1984-03-15;10:00:00;244.00;G;12;G
1984-03-15;11:00:00;249.00;G;168;G
1984-03-15;12:00:00;218.70;G;36;G
1984-03-15;13:00:00;223.10;G;138;G
1984-03-15;14:00:00;172.00;G;378;G
1984-03-15;15:00:00;169.00;G;1368;G
1984-03-15;16:00:00;86.70;G;138;G
1984-03-15;17:00:00;15.40;G;0;G
1984-03-15;18:00:00;0.00;G;0;G
1984-03-15;19:00:00;0.00;G;0;G
1984-03-15;20:00:00;0.00;G;0;G
1984-03-15;21:00:00;0.00;G;0;G
1984-03-15;22:00:00;0.00;G;0;G
1984-03-15;23:00:00;0.00;G;0;G
...

2026-06-30;14:00:00;474.15;G;2514;G
2026-06-30;15:00:00;422.05;G;1739;G
2026-06-30;16:00:00;359.69;G;2661;G
2026-06-30;17:00:00;142.69;G;0;G
2026-06-30;18:00:00;85.45;G;0;G
2026-06-30;19:00:00;43.69;G;0;G
2026-06-30;20:00:00;15.95;G;0;G
2026-06-30;21:00:00;1.04;G;0;G
2026-06-30;22:00:00;0.21;G;0;G
2026-06-30;23:00:00;0.00;G;0;G
2026-07-01;00:00:00;0.00;G;0;G
2026-07-01;01:00:00;0.14;G;0;G
2026-07-01;02:00:00;3.29;G;0;G
2026-07-01;03:00:00;20.20;G;0;G
2026-07-01;04:00:00;57.90;G;0;G
2026-07-01;05:00:00;125.21;G;98;G
2026-07-01;06:00:00;302.02;G;1347;G
























"""
























import time
from matplotlib.colors import LinearSegmentedColormap, Normalize
from scipy.ndimage import zoom
import numpy as np
from typing import List,Tuple,Dict
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import matplotlib.pyplot as plt
import calendar
import os

log:List[str]=[]

def handle_paths(paths:List,input_dir="input")->List[str]:
    """
    we make sure files are alright
    we make sure input dir exists
    we get paths from input dir if user hasent manually chosen paths to run it on.  
    """
    out_paths=[]
    
    try:
        os.mkdir(input_dir)
        print(f"Directory '{input_dir}' created.")
    except FileExistsError:
        print(f"Directory '{input_dir}' already exists.")
    
    if paths==[]:                                                 #this is if user has not selected files to run it on
        filenames = next(os.walk(input_dir), (None, None, []))[2] #get all filenames in "input" directory
        if filenames==[]:                                         #if input is empty, here the files are not downloaded
            print("go to website https://www.smhi.se/data/hitta-data-for-en-plats/ladda-ner-vaderobservationer")
            print(f"download sunlight data and put it in {input_dir} directory")
            raise ValueError    
        else: #there is paths in input, so we will run it with all files in input
            for filename in filenames:
                path=rf"{input_dir}\{filename}"
                out_paths.append(path)
    else:
        out_paths=paths
    
    return out_paths

def light_f(light:float)->int:
    return int(round(light*1000))

def get_title(path)->str:
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]
    i=0
    while True:
        if not(lines[i].strip()==""):
            break
        i+=1
    
    title:str = lines[i]+"\n"+lines[i+1]
    return title    
    
def get__utcdatetime_light(path: str)-> Tuple[Tuple[datetime, float], ...]:
    """
    we take the current path,
    from it we parse and clean all lines such that 
    they are in format (...(UTC datetime object,light in seconds as float
    
    """
    
    
    global log
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]

    #find header so we can start parsing data
    match_lis = "Datum;",";Tid (UTC);",";Global Irradians (svenska stationer);"
    header_index = next(
        i for i, line in enumerate(lines)
        if ((match_lis[0] in line)and(match_lis[1] in line)and(match_lis[2] in line))
    )
    
    csv_lines = [
        line.split(";")
        for line in lines[header_index + 1:]
        if line.strip()
    ]

    utcdatetime_light:List = []
    for row in csv_lines:
        try:
            utcdatetime_light.append(
                (
                datetime(
                        *map(int, row[0].split("-")),
                        *map(int, row[1].split(":")),
                        tzinfo=timezone.utc
                    ),
                float(row[2].replace(",", "."))
                )
            )
        except:
            log.append(row)

    utcdatetime_light = tuple(utcdatetime_light)
    return utcdatetime_light

def remove_leapyear(inp__svdatetime_light)-> Tuple[Tuple[datetime, float], ...]:

    out__svdatetime_light= tuple(
        (svdatetime, light)
        for svdatetime, light in inp__svdatetime_light
        if not (
            svdatetime.month == 2
            and svdatetime.day == 29
        )
    )
    return out__svdatetime_light

def plotA(day_second_light,title="",out_path="",debug=False):
    
    grid1 = np.zeros((24, 365), dtype=np.int64)
    grid2 = np.zeros((24, 365), dtype=np.float64)

    for day, second, light in day_second_light:
        hour = second // 3600
        day_index = day - 1

        if 0 <= hour < 24 and 0 <= day_index < 365:
            grid1[hour, day_index] += 1
            grid2[hour, day_index] += light

    grid = np.full((24, 365), np.nan)
    grid = np.divide(grid2, grid1, out=grid, where=grid1 > 0)
    grid/=1000
    
    if debug:
        print("1----------")
        for i in grid[:,100]:
            print(i)
    
    grid= np.clip(grid,0,400)
    
    if debug:
        print("2----------")
        for i in grid[:,100]:
            print(i)
    
    low_grid = np.where((grid > 0) & (grid < 200), grid * 2, 0)
    low_grid = np.clip(low_grid, 0, 200)
    mask = low_grid > 0
    grid[mask] = low_grid[mask]
    
    if debug:
        print("3----------")
        for i in grid[:,100]:
            print(i)

    low_grid = np.where((grid > 0) & (grid < 100), grid * 2, 0)
    low_grid = np.clip(low_grid, 0, 100)
    mask = low_grid > 0
    grid[mask] = low_grid[mask]

    if debug:
        print("4----------")
        for i in grid[:,100]:
            print(i)

    image_width = 1000
    image_height = 400

    high_resolution_array = zoom(
        np.nan_to_num(grid, nan=0.0),
        (image_height / grid.shape[0], image_width / grid.shape[1]),
        order=0
    ).astype(np.float32)

    # Draw black horizontal lines directly on the big array
    #thickness = 2
    #for hour in range(24):
    #    
    #    r_point = round(hour * (image_height - 1) / 23)
    #    start = max(0, r_point - thickness // 2)
    #    end = min(image_height, start + thickness)
    #
    #    if hour%6==0:
    #        high_resolution_array[start:end, :] = 1000
    #    else:
    #        high_resolution_array[start:end, :] = 300


##    plt.figure(figsize=(15, 7))
##    #plt.imshow(
##    #    high_resolution_array,
##    #    origin="lower",
##    #    aspect="auto",
##    #    interpolation="nearest",
##    #    cmap="inferno",
##    #    extent=[1, 365, 0, 24]
##    #)
##    plt.title(title)
##    plt.xlabel("Day of year")
##    plt.ylabel("Hour of day")
##    plt.xticks(np.arange(1, 366, 30))
##    plt.yticks(np.arange(0, 24, 1))
##    plt.savefig(out_path)
##
##
    plt.figure(figsize=(15, 7))
    plt.imshow(                                    # <-- uncommented
        high_resolution_array,
        origin="lower",
        aspect="auto",
        interpolation="nearest",
        cmap="inferno",
        extent=[1, 365, 0, 24]
    )
    plt.title(title)
    plt.xlabel("Day of year")
    plt.ylabel("Hour of day")
    plt.xticks(np.arange(1, 366, 30))
    plt.yticks(np.arange(0, 24, 1))
    plt.tight_layout()                             # keeps labels from clipping

    if out_path is not None:
        plt.savefig(out_path, dpi=150, bbox_inches="tight")
        plt.close()                                # free memory, don't open a window
    else:
        plt.show()


def plotB(day_second_light, threshold=1, title="",out_path=""):
    lis = []  # day, time

    data = day_second_light[
        np.lexsort((day_second_light[:, 1], day_second_light[:, 0]))
    ]

    for i in range(1, len(data)):
        day, second, light = data[i]
        prev_day, prev_second, prev_light = data[i - 1]

        if day == prev_day and (prev_light <= threshold) != (light <= threshold):
            lis.append((day + second / 86400, second / 3600))

    arr = np.asarray(lis, dtype=np.float64).reshape(-1, 2)

    plt.figure(figsize=(15, 7))
    plt.scatter(arr[:, 0], arr[:, 1], s=2)
    plt.xlabel("Day of year")
    plt.ylabel("Transition time (hour)")
    plt.title(title)
    plt.yticks(np.arange(0, 25, 2))
    plt.tight_layout()
    plt.savefig(out_path)

   
def process(path,
            plotA_bool=True,
            plotB_bool=False
            ):
    
    
    title = get_title(path)
    #vi parsar pdf och hämtar ...(datetime,light)...
    utcdatetime_light = get__utcdatetime_light(path)

    # vi gör utc -> sv
    # sommartid och vinter tid finns här
    swedish_timezone = ZoneInfo("Europe/Stockholm")
    svdatetime_light = [
        (svdatetime.astimezone(swedish_timezone),light)
        for svdatetime,light in utcdatetime_light
    ]
    svdatetime_light=tuple(svdatetime_light)
    
    #vi tar bort skottår
    svdatetime_light= remove_leapyear(svdatetime_light)
    

    day_second_light= np.array(
        [
            (
            int(
            svdatetime.timetuple().tm_yday
            - int(calendar.isleap(svdatetime.year) and svdatetime.month > 2)
            ),
            int(
            svdatetime.hour * 3600
            + svdatetime.minute * 60
            + svdatetime.second
            ),
            int(
            light_f(light)
            )
            )
            for svdatetime, light in svdatetime_light
        ],
            dtype=np.int64
        )
    
    if plotA_bool:
        plotA(day_second_light, title=title,out_path=rf"output\{time.time()}.jpg")
    if plotB_bool:
        plotB(day_second_light, title=title,out_path=rf"output\{time.time()}.jpg")
    

def main():

    paths = [] #t.ex [r"input\smhi-opendata_11_41_42_10_24_98735_20261028_175644.csv"]
    
    paths = handle_paths(paths)

    
    for path in paths:
        process(path)


if __name__ == "__main__":
    main()