from time import sleep
from threading import Thread
from datetime import datetime

def wite_words(word_count, file_name):
    file = open(file_name,'w',encoding='utf-8')
    for word in range(1,word_count+1):
        file.write(f'Какое-то слово № {word}\n')
        sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')
start_1 = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
finish_1 = datetime.now()
start_2 = datetime.now()
a = Thread(target= wite_words, args=(10, 'example5.txt'))
b = Thread(target= wite_words, args=(30, 'example6.txt'))
c = Thread(target= wite_words, args=(200, 'example7.txt'))
d = Thread(target= wite_words, args=(100, 'example8.txt'))
a.start()
b.start()
c.start()
d.start()
a.join()
b.join()
c.join()
d.join()
finish_2 = datetime.now()
res_1 = finish_1 - start_1
res_2 = finish_2 - start_2
print(res_1)
print(res_2)