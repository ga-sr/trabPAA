def insertionSort(array):
    size = len(array)
    for i in range(1, size):
        elem = array[i]
        j = i-1
        while(j >= 0 and array[j] > elem):
            array[j+1] = array[j]
            j-=1
        array[j+1] = elem

def selectionSort(array):
    size = len(array)
    for i in range(size-1):
        menor = array[i]
        index = i
        for j in range(i+1, size):
            if array[j] < menor:
                menor = array[j]
                index = j
        array[index] = array[i]
        array[i] = menor

def shellSort(array, incs):
    sizear = len(array)
    sizein = len(incs)
    for inc in range(sizein):
        span = incs[inc]
        for i in range(span, sizear):
            x = array[i]
            j = i-span
            while j >= 0 and array[j] > x:
                array[j+span] = array[j]
                j-=span
            array[j+span] = x

def heapify(arr, n, i): 
    largest = i 
    l = 2 * i + 1 
    r = 2 * i + 2 

    if l < n and arr[i] < arr[l]: 
        largest = l 

    if r < n and arr[largest] < arr[r]: 
        largest = r 

    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]

        heapify(arr, n, largest) 

def heapSort(arr): 
    n = len(arr)

    for i in range(n, -1, -1): 
        heapify(arr, n, i) 

    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)