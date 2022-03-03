k = int(input('Введите число k: '))
with open("text.txt", "r") as f:
    data = f.read()
lst = data.split()
new_lst = []
i = 1
for i in range(0, len(lst)):
    if len(lst[i]) % 2 != 0:
        new_lst.append(lst[i])
    i += 1
for i in range(0, len(new_lst)):
    n = int(new_lst[i])
    s = ''
    h = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if n == 0:
        s = 0
    while n > 0:
        s = h[n % k] + s
        n = n // k
    print(new_lst[i], '=', s)
