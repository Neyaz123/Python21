import random

# 1. Быстрая сортировка
def qcksrt(arr, first, last):
    """Метод быстрой сортировки одномерного массива"""
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

some_arr = [random.randint(1, 10) for i in range(15)]
print('1. Исходный массив: ', some_arr)
qcksrt(some_arr, 0, len(some_arr)-1)
print('1. Быстрая сортировка: ', some_arr)

# 2. Сортировка слиянием(не удалось реализовать)

# 3. Сортировка Шелла
def shellsort(arr):
    """Метод сортировки Шелла для одномерного массива"""
    dist = len(arr) // 2
    while dist > 0:
        for i in range(len(arr)-dist):
            j = i
            while j >= 0 and arr[j] > arr[j+dist]:
                arr[j], arr[j+dist] = arr[j+dist], arr[j]
                j -= 1
        dist = int(dist/2)
    return arr
randarr = [random.randint(1, 10) for i in range(15)]
print('3. Исходный массив: ', randarr)
print('3. Сортировка Шелла: ', shellsort(randarr))

# 4. Сортировка выбором
def selectionsort(arr):
    """Метод сортировки одномерного массива выбором"""
    for i in range(len(arr) - 1):
        arrmin = i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[arrmin]:
                arrmin = j
            j += 1
        arr[i], arr[arrmin] = arr[arrmin], arr[i]
    return arr
thisarr = [random.randint(1, 10) for i in range(15)]
print('4. Исходный массив: ', thisarr)
print('4. Сортировка выбором: ', selectionsort(thisarr))

# 5. Сортировка пузырьком
thatarr = [random.randint(1, 10) for i in range(15)]
print('5. Исходный массив: ', thatarr)
def bubblesort(arr):
    """Метод сортировки одномерного массива пузырьком"""
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print('5. Сортировка пузырком: ', bubblesort(thatarr))

# 6. Сортировка вставками
def insertsort(arr):
    for i in range(len(arr)):
        curr = arr[i]
        j = i-1
        while j >=0 and curr < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = curr 
    return arr
anyarr = [random.randint(1, 10) for i in range(15)]
print('6. Исходный массив: ', anyarr)
print('6. Сортировка вставками: ', insertsort(anyarr))
