"""
Программа, которая читая данные из входного потока, выводит на экран числа, содержащее нечетное количество цифр,
переведя их в К-ичную (от 2 до 35 включительно) систему счисления.
Входной поток моделируется конечным файлом произвольной длины. Длина файла определяется доступной памятью на диске.
Чтение посимвольно. Максимальный размер рабочего буфера для накопления чисел - 100 символов (максимальная длина числа).
Вывод результата работы программы осуществляется на экран.
"""
import time
max_buffer_len = 100    # Максимальный размер рабочего буфера
buffer_len = 1          # Размер буфера чтения
work_buffer = ""                # Рабочий буфер
digit_flag = False              # Флаг наличия цифры
try:
    print("----- Локальное время", time.ctime(), "-----")
    while 1:
        k = int(input('Введите число k:'))
        if (k > 1) and (k <= 36):
            break
        else:
            print('Программа не может переводить числа в такую систему счисления, '
                  'либо такой системы счисления не существует.')
    start = time.time()
    with open("text.txt", 'a') as file:   # Открываем файл
        file.write('\n')
    with open("text.txt", 'r+') as file:  # Открываем файл
        print("\n-----Результат работы программы-----\n")
        buffer = file.read(buffer_len)  # Читаем первый блок
        while buffer:  # Пока файл не пустой
            if (buffer >= '0') and (buffer <= '9'):  # Обрабатываем текущий блок
                digit_flag = True
                work_buffer += buffer
            if buffer.find(".") >= 0 or buffer.find(",") >= 0 or \
                    buffer.find(" ") >= 0 or buffer.find("\n") >= 0:  # Если символ - окончание числа
                if digit_flag:  # Если в буфере сформировалось число
                    if len(work_buffer) % 2 != 0:
                        for i in range(0, len(work_buffer)):
                            n = int(work_buffer)
                            s = ''
                            h = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                            while n > 0:
                                s = h[n % k] + s
                                n = n // k
                        print(int(work_buffer), '=', s)  # Печатаем предложение и готовим новый цикл
                digit_flag = False
                work_buffer = ''
            buffer = file.read(buffer_len)  # Читаем очередной блок
        finish = time.time()
        result = finish - start
        print("Program time: " + str(result) + " seconds.")
except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен."
          "\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
