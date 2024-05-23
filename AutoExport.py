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
         'https://docs.google.com/spreadsheets/d/e/2PACX-1vQhNECAL9lEPHwjc9aKlngToTPmprLkMfnDe5I-SPmgrbYFzG8zrY0aittd9savxIQ34_4iUurPrtah/pub?output=xlsx',
         'https://docs.google.com/spreadsheets/d/e/2PACX-1vTzirMiIld82QHfkIgTwXNbpprU8b4tWiud4VSjvcLATE1fT9vBuXcQcXRAuDTkXoKFahT7oD3Ubzpq/pub?output=xlsx',
         'https://docs.google.com/spreadsheets/d/e/2PACX-1vQxX-9VpGCRKtlfEWYNNLsqfEykCwbgX3ozMaInRu2ezTsF10HtCFxQHPgYCCkyBVmFhKz8KmCMzT-y/pub?output=xlsx',
         'https://docs.google.com/spreadsheets/d/e/2PACX-1vSE4udJYp-JBKbFHpWesYHpdA73ZKXjQ4Is8-VdDzg3u_bUM6VR3sK_3O34QSIwtK58u_r3LO1wRils/pub?output=xlsx',
         'https://docs.google.com/spreadsheets/d/e/2PACX-1vTqw_1k2T4zd6gQqXXMx2Tv4YWiqLx72vEqP7xqn7RGwNIwiFhaYS97dwPzKb-dsN-v27HIttpyNQZY/pub?output=xlsx',
         'https://docs.google.com/spreadsheets/d/e/2PACX-1vSnsrj4GYHmHTD-lfU66HVEtfPzoKEatLuRag_j1s9O06PQ-4E8GcqXrlKWykJoU9I8WbfJPAwhD0Iu/pub?output=xlsx']

browser_path = 'C:\\\\Users\\\\Артем\\\\AppData\Local\\\\Programs\\\\Opera\\\\opera.exe'
folder_path = 'C:\\\\testfolder'

active = True
commands = [[browser_path, link] for link in links]

print('Приветствую')
while active: 
    interval = input('Введите интервал загрузки в секундах: ')
    if interval.isdecimal() and int(interval) > 0:
        while active:
            try:
                all_links_ok = all(requests.get(link).ok for link in links)
                if all_links_ok:
                    delete_files(folder_path)
                    processes = [subprocess.Popen(cmd) for cmd in commands]
                    time.sleep(20)
                    os.system('taskkill /f /im opera.exe')
                    time.sleep(int(interval))
            except requests.exceptions.RequestException or requests.exceptions.HTTPError or requests.exceptions.ConnectionError or requests.exceptions.Timeout:
                print('Возникли проблемы при подключении')
                time.sleep(5)
                active = False       
    else:
        print('Введите натуральное число')
        continue