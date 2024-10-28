''''''
'''
Домашнее задание по теме "Введение в потоки".

Цель: понять как работают потоки на практике, решив задачу

Задача "Потоковая запись в файлы":
Необходимо создать функцию write_words(word_count, file_name), 
где word_count - количество записываемых слов,
 file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов
 "Какое-то слово № <номер слова по порядку>" 
 в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
10, example1.txt
30, example2.txt
200, example3.txt
100, example4.txt
После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
10, example5.txt
30, example6.txt
200, example7.txt
100, example8.txt
Пример результата выполнения программы:
Вывод на консоль:
Завершилась запись в файл example1.txt
Завершилась запись в файл example2.txt
Завершилась запись в файл example3.txt
Завершилась запись в файл example4.txt
Работа потоков 0:00:34.003411 # Может быть другое время
Завершилась запись в файл example5.txt
Завершилась запись в файл example6.txt
Завершилась запись в файл example8.txt
Завершилась запись в файл example7.txt
Работа потоков 0:00:20.071575 # Может быть другое время

Файл module_10_1.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
'''
from  datetime import datetime
'''datetime для работы с час минута сек '''
from time import sleep
'''sleep для работы с сек для установки задержки'''
import threading
'''для работы с потоком'''

def write_words(word_count, file_name):
    '''
    функция для записи строк в файл
    :param word_count: номер слова по порядку
    :param file_name: наименование файла для записи
    '''
    with open(file_name, 'w', encoding='utf-8') as file:
        #открываем файл в режиме записи с кодировкой utf-8 и сохраняем как объект file,
        #по завершении кода закрываем файл
        for n  in range(word_count):
            # проходим по числам от 0 до word_count
           file.write(f'Какое-то слово № {n+1}\n')
            #в объект файл запись строки "Какое-то слово №" n+1
           sleep(0.1)
           #Задержка на 0.1сек
        print(f'Завершилась запись в файл {file_name}')
        #Вывод записи 'Завершилась запись в файл {file_name}'

        #print(file_name, threading.current_thread())
        #использовать для отладки


time_start = datetime.now()
#время начала работы функций
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
#Вызов функций с параметрами
print()
print(f'Время работы функций: {datetime.now() - time_start}\n')
#вывод времени работы функции

time_start = datetime.now()
#время начала работы потоков
thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
#создание потоков с функцией write_words, и аргументами word_count и file_name
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
#запуск потоков

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
#остановка основного потока

print()
print(f'Время работы потоков: {datetime.now() - time_start}')
#вывод времени работы потоков
