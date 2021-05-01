from bs4 import BeautifulSoup
import requests
from googlesearch import search
import csv
import pandas as pd 

def scrapwebsite():
    df = pd.read_html('https://www.gsmarena.com/motorola_moto_e7-10511.php')
    print(df)

    with open  ('moblist.txt', 'r') as file:
        reader = csv.reader(file)
        mob_list = [f'gsmarena {i[0]}' for i in reader]
        
    website = []
    for mob in mob_list:    
        for j in search(mob,num=1,stop=1,pause=5.0):
            website.append(j)


website = ['https://www.maxcom.pl/en/desktop-phones-for-sim-card/290-maxcom-comfort-mm29-3g-biurkowy-telefon-gsm-3g-5908235973906.html', 
'https://www.gsmchoice.com/en/catalogue/maxcom/classicmm3303g/',
 'https://www.myphone.pl/en/product/hammer-5-smart/',
  'https://www.gsmarena.com/xiaomi_redmi_9c_nfc-10277.php', 
  'https://www.gsmarena.com/lg_k22-10597.php', 'https://www.gsmarena.com/xiaomi_redmi_9-10233.php', 
  'https://www.gsmarena.com/motorola_moto_e7-10511.php', 'https://www.gsmarena.com/oppo_a15-10497.php', 'https://www.gsmarena.com/samsung_galaxy_a02s-10603.php', 
  'https://www.gsmarena.com/oppo_a15s-10644.php', 'https://www.gsmarena.com/lg_k42-10459.php', 'https://www.gsmarena.com/motorola_moto_g30-10724.php', 
  'https://www.gsmarena.com/samsung_galaxy_a12-10604.php', 'https://www.gsmarena.com/samsung_galaxy_a21s-10239.php', 
  'https://www.gsmarena.com/motorola_moto_g9_play-10387.php', 'https://www.gsmarena.com/xiaomi_redmi_note_9-10192.php', 
  'https://www.gsmarena.com/motorola_moto_g50-10789.php', 'https://www.gsmchoice.com/en/catalogue/hammer/explorer/', 
  'https://www.gsmarena.com/samsung_galaxy_a32_5g-10648.php', 'https://www.gsmarena.com/samsung_galaxy_xcover_4s-9730.php']   
page = requests.get(website[6]).text
content = BeautifulSoup(page,'lxml').encode('utf-8')
table = content.find("table")