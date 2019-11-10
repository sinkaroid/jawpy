import requests
import webbrowser, os
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup
from pathlib import Path

print(Fore.RED)
print("""
            _                _         __                      
  /\ /\__ _| | ___ _ __   __| | ___ _ _\ \  __ ___      ____ _ 
 / //_/ _` | |/ _ \ '_ \ / _` |/ _ \ '__\ \/ _` \ \ /\ / / _` |
/ __ \ (_| | |  __/ | | | (_| |  __/ /\_/ / (_| |\ V  V / (_| |
\/  \/\__,_|_|\___|_| |_|\__,_|\___|_\___/ \__,_| \_/\_/ \__,_| -Sin                                                        
""")
print(Style.RESET_ALL)

bulan = input("bulan: ")
tahun = input("tahun: ")
params = "kalender-jawa-untuk-bulan-"
page = requests.get('https://www.infojabodetabek.com/'+params+bulan+'-'+tahun+'-masehi/')

soup = BeautifulSoup(page.text, 'html.parser')


akhiran = soup.find(class_='entry-tags clearfix')
akhiran.decompose()

cal_list = soup.find(class_='entry-content clearfix')
cal_list_items = cal_list.find_all('td')
print ('OK '+ Fore.GREEN +bulan+ Style.RESET_ALL)



for cal in cal_list_items:
    
    
    with open(''+bulan+'.html', 'w') as f:
        for cal in cal_list_items:
             f.write("%s\n" % str(cal.prettify().replace('<td width="115">', '<center><br>')))

webbrowser.open('file://' + os.path.realpath(''+bulan+'.html'))
          