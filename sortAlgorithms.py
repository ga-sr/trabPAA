def bubbleSort(array):
    size = len(array)
    for j in range(size):
        for i in range(size - j - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]


def bubbleSortXd(array):
    size = len(array)
    for j in range(size):
        switch = False
        for i in range(size - j - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                switch = True
        if switch == False:
            break


def elParticion(array, p, r):
    x = array[p]
    up = r
    down = p
    while (down < up):
        while(array[down] <= x):
            down += 1
        while(array[up] > x):
            up -= up
        if down < up:
            array[down], array[up] = array[up], array[down]
    array[p] = array[up]
    array[up] = x
    return(up)


def quickSort(array, p, r):
    if p < r:
        q = elParticion(array, p, r)
        quickSort(array, p, q-1)
        quickSort(array, q+1, r)


def merge(array, e, q, d):
    n1 = q - e + 1
    n2 = d - q

    E = [0] * (n1)
    D = [0] * (n2)

    for i in range(0, n1):
        E[i] = array[e + i]

    for j in range(0, n2):
        D[j] = array[q + 1 + j]

    i = j = 0
    k = e

    while i < n1 and j < n2:
        if E[i] <= D[j]:
            array[k] = E[i]
            i += 1
        else:
            array[k] = D[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = E[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = D[j]
        j += 1
        k += 1


def mergeSorte(array, e, d):
    if e < d:
        q = (e+(d-1))/2
        mergeSorte(array, e, q)
        mergeSorte(array, q+1, d)
        merge(array, e, q, d)



