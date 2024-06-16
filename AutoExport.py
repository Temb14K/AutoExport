import time
import os
import requests
import re
from urllib.parse import unquote
import json

links = []
folder_path = ''

active = True

def delete_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print('Ошибка при удалении файла')

def get_response(links):
    for url in links:
        response = requests.get(url, allow_redirects=True)
        response.raise_for_status()  # Проверяем, что запрос прошел успешно

def download_files(links):
    for url in links:
        response = requests.get(url, allow_redirects=True)
        if 'content-disposition' in response.headers:
            filename = re.findall('filename=(.+)', response.headers['content-disposition'])[0]
        else:
            filename = 'default_filename'  # Используем стандартное имя, если имя файла не указано

        filename = unquote(filename)  # Декодируем имя файла, если оно было закодировано
        filename = filename.split("''", 1)[1]
        print(filename)
        with open(folder_path + filename, 'wb') as file:
            file.write(response.content)
        print(f'Файл успешно скачан и сохранен как {filename}')

while True:
    print('Приветствую')
    first_answer = input('Вы хотите изменить папку загрузки? Введите Y если хотите. Если нет, введите любое значение\n ').upper()
    if first_answer == 'Y':
       folder_path = input('Введите путь к папке в формате C:/path/test/\n ')
       with open('folder_path.json', 'w') as f:
           json.dump(folder_path, f)
    while active:
        second_answer = input('Вы хотите добавить ссылки? Введите Y если хотите. Если нет, введите любое значение.\n ').upper()
        second_answer.upper()
        if second_answer == 'Y':
            links.append(input('Введите URL адрес ссылки:\n '))
            with open('links.json', 'w') as l:
                json.dump(links, l)
            continue
        else:
            break
    interval = input('Введите интервал загрузки в секундах: ')
    if interval.isdecimal() and int(interval) > 0:
        while True:
            try:
                with open ('folder_path.json') as f:
                    folder_path = json.load(f)
            except:
                print('Файл folder_path.json поврежден или отсутствует')
            try:
                with open ('links.json') as l:
                    links = json.load(l)
            except:
                print('Файл links.json поврежден или отсутствует')
            try:
                get_response(links)
            except Exception as e:
                print(f'Возникли проблемы при подключении:\n {e}')
                continue
            else:
                delete_files(folder_path)     
                download_files(links)
                time.sleep(int(interval))
                continue
    else:
        print('Введите натуральное число')
        continue



