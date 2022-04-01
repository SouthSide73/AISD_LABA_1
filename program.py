"""
Программа, которая читая данные из входного потока, выводит на экран числа, содержащее нечетное количество цифр,
переведя их в К-ичную (от 2 до 35 включительно) систему счисления.
Входной поток моделируется конечным файлом произвольной длины. Длина файла определяется доступной памятью на диске.
Чтение посимвольно. Вывод результата работы программы осуществляется на экран.
"""
import time
import re
buffer_len = 1                  # Размер буфера чтения
work_buffer = ""                # Рабочий буфер
digit_flag = False              # Флаг наличия цифры
stop_flag = False               # Флаг пустого буфера
symbol_flag = False             # Флаг слитного написания буквенных символов с числом
try:
    print("----- Локальное время", time.ctime(), "-----")
    while 1:
        k = int(input('Введите число k:'))  # Ввод значения переменной с клавиатуры
        if (k > 1) and (k <= 36):
            break
        else:   # Если число выходит за промежутки
            print('\nПрограмма не может переводить числа в такую систему счисления, '
                  'либо такой системы счисления не существует.'
                  '\nВведите число в десятичной системе счисления от 1 до 36')
    start = time.time()
    with open("text.txt", 'r+', encoding='utf-8') as file:   # Открываем файл
        print("\n-----Результат работы программы-----\n")
        buffer = file.read(buffer_len)  # Читаем первый блок
        if not buffer:  # Если файл пустой
            print("\nФайл text.txt в директории проекта пустой."
                  "\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
        while buffer:  # Пока файл не пустой
            if re.findall(r'[а-яё]|[А-ЯЁ]|[a-z]|[A-Z]', buffer):  # Проверка буфера на наличие буквы
                symbol_flag = True
            if (buffer >= '0') and (buffer <= '9'):  # Обрабатываем текущий блок
                work_buffer += buffer
                digit_flag = True
            if re.findall(r'[а-яё]|[А-ЯЁ]|[a-z]|[A-Z]', buffer) and digit_flag:  # Если буквенные символы между цифрами
                print("\nВ файле числа должны быть представлены в десятичной системе счисления."
                      "\nМежду цифрами или после чисел пишутся слитно буквенные символы. Измените существующий text.txt файл.")
                break
            if re.findall(r'[\W]|[_]', buffer):    # Если символ - окончание числа
                if digit_flag:  # Если в буфере сформировалось число
                    if len(work_buffer) % 2 != 0:
                        for i in range(0, len(work_buffer)):  # Цикл перевода числа в К-ичную систему счисления
                            n = int(work_buffer)
                            s = ''
                            h = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                            if n == 0:
                                s = '0'
                            while n > 0:
                                s = h[n % k] + s
                                n = n // k
                        print(int(work_buffer), '=', s)  # Печатаем предложение и готовим новый цикл
                        if stop_flag:  # Остановка программы, если дошли до конца файла
                            break
                digit_flag = False
                work_buffer = ''
            buffer = file.read(buffer_len)  # Читаем очередной блок
            if re.findall(r'[\d]', buffer) and symbol_flag:  # Если буквенные символы пишутся слитно с числом
                print("\nВ файле слитно с числом пишутся буквенные символы."
                      "\nИзмените существующий text.txt файл.")
                break
            else:
                symbol_flag = False
            if (not buffer) and (len(work_buffer) % 2 != 0):   # Если дошли до конца файла
                buffer = " "
                stop_flag = True
        finish = time.time()
        result = finish - start
        print("Program time: " + str(result) + " seconds.")  # Вывод времени программы
except FileNotFoundError:     # Если файл отсуствует в директории
    print("\nФайл text.txt в директории проекта не обнаружен."
          "\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
except ValueError:  # Если вводится не целое число или буквенные символы
    print("\nВводятся недопустимые символы."
          "\nВведите число в десятичной системе счисления от 1 до 36.")
