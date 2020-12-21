import random
arr = list(range(1, 101))
arr.pop(random.randint(1, 100))
random.shuffle(arr)
print('Исходный массив: ',arr)

# 1. Как найти пропущенное число в заданном массиве целых чисел от 1 до 100?
print('1. Пропущенное число: ', 5050 - sum(arr))

# 2.  Как найти повторяющееся число в заданном массиве целых чисел?
for i in range(99):
    for j in range(i+1, 99):
        if arr[i] == arr[j]:
            print("2. Есть повторяющиеся элементы")
            quit()
print("2. Нет повторяющихся элементов")

# 3. Как найти наибольшее и наименьшее число в неотсортированном массиве?
arrmax = 1
arrmin = 1
for i in range(len(arr)):
    if arr[i] < arrmin:
        arrmin = arr[i]
    if arr[i] > arrmax:
        arrmax = arr[i]
print('3. Максимальный элемент:',arrmax,'\n3. Минимальный элемент:', arrmin)

# 4. Как найти все пары в массиве целых чисел, сумма которых равна заданному числу?
qsum = int(input('4. Введите искомую сумму: '))
arr.sort()
first = 1;
last = len(arr) - 1
while first < last:
    s = arr[first] + arr[last]
    if s == qsum:
        print(arr[first], arr[last])
        first += 1
        last -= 1
    else:
        if s < qsum:
            first += 1
        else:
            last -= 1
if qsum != s:
    print('Числа не найдены')

# 5. Как найти повторяющиеся числа в массиве, если их несколько?
arr2 = [random.randint(1, 25) for i in range(50)]
print('5. Исходный массив: ', arr2)
arr2.sort()
deleted_arr2 = []
for i in range(len(arr2) - 1):
    if (arr2[i] == arr2[i+1]) and (arr2[i] not in deleted_arr2):
        deleted_arr2.append(arr2[i])
        print(arr2[i])

# 6. Как удалить повторяющиеся элементы из заданного массива?
arr3 = [random.randint(1, 25) for i in range(50)]
print('6. Исходный массив: ', arr3)
deleted_arr3 = []
for i in arr3:
    if i not in deleted_arr3:
        deleted_arr3.append(i)
print('Массив без повторяющихся элементов: ', deleted_arr3)

# 7. Как сортировать массив целых чисел без дополнительной памяти при помощи алгоритма быстрой сортировки?
def qcksrt(arr, first, last):
    if first >= last:
        return
    mid = arr[(first + last)//2]
    f, l = first, last
    while f <= l:
        while arr[f] < mid:
            f = f + 1
        while arr[l] > mid:
            l = l - 1
        if f <= l:
            arr[f], arr[l] = arr[l], arr[f]
            f, l = f +1, l -1        
    qcksrt(arr, first, l)
    qcksrt(arr, f, last)
qcksrt(arr3, 0, len(arr3)-1)
print('7. Быстрая сортировка: ', arr3)

# 8. Как удалить повторяющиеся элементы из массива без дополнительной памяти?
print('8. Массив без повторяющихся элементов: ', list(set(arr3)))

# 9. Как сделать поменять порядок элементов в массиве на обратный без дополнительной памяти?
print('9. Массив в обратном порядке: ', list(reversed(arr3)))

# 10. Как удалить повторяющиеся элементы из массива без использования коллекций?
for i in range(len(arr3)-1,-1,-1):       #работает только в отсортированном массиве
        if arr3[i] == arr3[i-1]: del arr3[i]
print('10. Массив без повторяющихся элементов: ', arr3)
