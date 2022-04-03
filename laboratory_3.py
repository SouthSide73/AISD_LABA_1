"""
Программа, которая читая данные из входного потока, выводит на экран числа, содержащее нечетное количество цифр,
переведя их в К-ичную (от 2 до 35 включительно) систему счисления.
Входной поток моделируется конечным файлом произвольной длины. Длина файла определяется доступной памятью на диске.
Чтение посимвольно. Вывод результата работы программы осуществляется на экран.
"""
import time
import re
import sys
buffer_len = 1                  # Размер буфера чтения
work_buffer = ""                # Рабочий буфер
digit_flag = False              # Флаг наличия цифры
stop_flag = False               # Флаг пустого буфера
symbol_flag = False             # Флаг слитного написания буквенных символов с числом
hope_flag = False               # Флаг дробных чисел
h = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'      # Алфавит
def toBASEint(num, base):                       # Функция для перевода сс дробей (1)
    n = abs(num)
    b = h[n % base]
    while n >= base:
        n = n // base
        b += h[n % base]
    return ('' if num >= 0 else '-') + b[::-1]
def toBaseFrac(frac, base, n=10):              # Функция для перевода сс дробей (2)
    b = ''
    while n:
        frac *= base
        frac = round(frac, n)
        b += (h[int(frac)])
        frac -= int(frac)
        n -= 1
    return b
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
            if buffer == ".":            # Если находится точка
                if not "." in work_buffer:
                    work_buffer += buffer
                else:
                    print("\nВ файле найдена ошибка с пунктуацией при нахождении дроби."
                          "\nИзмените существующий text.txt файл.")
                    break
                hope_flag = True
            if buffer == "-":
                if not "-" in work_buffer:
                    work_buffer += buffer
                else:
                    print("\nВ файле найдена ошибка с пунктуацией при нахождении дроби."
                          "\nИзмените существующий text.txt файл.")
                    break
                tire_flag = True
            if re.findall(r'[а-яё]|[А-ЯЁ]|[a-z]|[A-Z]', buffer) and digit_flag:  # Если буквенные символы между цифрами
                print("\nВ файле числа должны быть представлены в десятичной системе счисления."
                      "\nМежду цифрами или после чисел пишутся слитно буквенные символы."
                      " Измените существующий text.txt файл.")
                break
            if re.findall(r'[^а-яёА-ЯЁa-zA-Z0-9.-]', buffer):    # Если символ - окончание числа
                if hope_flag:       # Если в буфере сформировалась дробь
                    digit_flag = False
                if work_buffer[0] == "-" and len(work_buffer) % 2 == 0 and re.findall(r'[-]*[0-9]', work_buffer)\
                        and digit_flag:
                    s = work_buffer
                    print(s, '=', toBASEint(int(work_buffer), k))
                if digit_flag:  # Если в буфере сформировалось целое число
                    if len(work_buffer) % 2 != 0:
                        for i in range(0, len(work_buffer)):  # Цикл перевода числа в К-ичную систему счисления
                            n = int(work_buffer)
                            s = ''
                            if n == 0:
                                s = '0'
                            while n > 0:
                                s = h[n % k] + s
                                n = n // k
                        print(int(work_buffer), '=', s)  # Печатаем предложение и готовим новый цикл
                    if stop_flag:  # Остановка программы, если дошли до конца файла
                        break
                if hope_flag:       # Если в буфере сформировалась дробь
                    if float(work_buffer) > 0:     # Если дробь положительная
                        if work_buffer[0] == '.':
                            work_buffer = '0' + work_buffer    # Добавление нуля
                        if len(work_buffer) % 2 == 0:
                            num, frac = map(str, work_buffer.split('.'))    # Цикл перевода числа в другую сс
                            num = int(num, 10)
                            a = toBASEint(num, k)
                            b = 0
                            f = 10
                            for i in frac:
                                b += h.index(i) / f
                                f *= 10
                            b = str(toBaseFrac(b, k)).rstrip('0')
                            if b == "":
                                print(work_buffer, "=", a)
                            else:
                                print(work_buffer, "=", a + '.' + b)
                    if float(work_buffer) < 0:     # Если дробь отрицательная
                        work_buffer = work_buffer[1:]    # Удаление минуса
                        if work_buffer[0] == ".":
                            work_buffer = "0" + work_buffer    # Добавление нуля
                        num, frac = map(str, work_buffer.split('.'))    # Цикл перевода числа в другую сс
                        num = int(num, 10)
                        a = toBASEint(num, k)
                        a = '-' + a
                        b = 0
                        f = 10
                        for i in frac:
                            b += h.index(i) / f
                            f *= 10
                        b = str(toBaseFrac(b, k)).rstrip('0')
                        work_buffer = '-' + work_buffer
                        if b == "":
                            print(work_buffer, "=", a)
                        else:
                            print(work_buffer, "=", a + '.' + b)
                    if stop_flag:  # Остановка программы, если дошли до конца файла
                        break
                hope_flag = False
                digit_flag = False
                work_buffer = ''
            buffer = file.read(buffer_len)  # Читаем очередной блок
            if re.findall(r'[\d]', buffer) and symbol_flag:  # Если буквенные символы пишутся слитно с числом
                print("\nВ файле слитно с числом пишутся буквенные символы."
                      "\nИзмените существующий text.txt файл.")
                break
            else:
                symbol_flag = False
            if not buffer:   # Если дошли до конца файла
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
except KeyboardInterrupt:
    print("\nУберите лишние символы в конце файла для правильного завершения программы."
          "\nЛишние символы: пробелы, переход на следующие строки.")
print ('Memory: {0}Mb'.format(sys.getsizeof([])))
