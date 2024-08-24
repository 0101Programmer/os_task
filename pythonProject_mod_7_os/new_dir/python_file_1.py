# import os
# import time
#
# for roots, dirs, files in os.walk('.'):
#     for file in files:
#         filepath = os.path.join(os.getcwd())
#         filetime = os.path.getmtime(file)
#         formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#         file_size = os.path.getsize(file)
#         parent_dir = os.path.dirname(file)
#         print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')