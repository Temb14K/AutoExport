import time
import os
import subprocess
import requests

def delete_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print('Ошибка при удалении файла')

links = ['https://docs.google.com/spreadsheets/d/e/2PACX-1vSMeMZE8Vd05LfReLQBelHfxppucu-2SiS6gYa3E6wf9oR1S-54qFkURjW8iKz26bdez2r_7_3oSeWt/pub?output=xlsx',
         'https://docs.google.com/spreadsheets/d/e/2PACX-1vSskTHGF9U3msgwLWe_JWV1eCjShbjkbgkZS0Q9XGayZT7qn8QRM2bL09Zs6odd3gGM2ZkfzQ_TFRnk/pub?output=xlsx',
         'https://docs.google.com/spreadsheets/d/e/2PACX-1vRDtGdUHQGdWiXE7jjmxUHfB54kpDkAzo7eXRZvLLzBHmC_YYLr-3dqWnOUSpe_PJoGIPaDItkSSvaM/pub?output=xlsx',
         'https://docs.google.com/spreadsheets/d/e/2PACX-1vSzyhYcSld1eMLxQ2AO0lW8atDZP16ZERUD0xjRBRb9e4tC_hMT6trIQdycvm-asxFf7SeNW20Dov1k/pub?output=xlsx',
         'https://docs.google.com/spreadsheets/d/e/2PACX-1vQhNECAL9lEPHwjc9aKlngToTPmprLkMfnDe5I-SPmgrbYFzG8zrY0aittd9savxIQ34_4iUurPrtah/pub?output=xlsx']

browser_path = 'C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe'

active = True
commands = [
    [browser_path, links[0]],
    [browser_path, links[1]],
    [browser_path, links[2]],
    [browser_path, links[3]],
    [browser_path, links[4]]
]

print('Приветствую')
while active: 
    interval = input('Введите интервал загрузки в секундах: ')
    if interval.isdecimal() and int(interval) > 0:
        while active:
            try:
                all_links_ok = all(requests.get(link).ok for link in links)
                if all_links_ok:
                    delete_files('C:\\\\testfolder')
                    processes = [subprocess.Popen(cmd) for cmd in commands]
                    time.sleep(20)
                    os.system('taskkill /f /im chrome.exe')
                    time.sleep(int(interval))
            except requests.exceptions.RequestException or requests.exceptions.HTTPError or requests.exceptions.ConnectionError or requests.exceptions.Timeout:
                print('Возникли проблемы при подключении')
                time.sleep(5)
                active = False       
    else:
        print('Введите натуральное число')
        continue