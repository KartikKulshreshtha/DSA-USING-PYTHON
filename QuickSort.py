def swap(a, b, elements):
    if a!=b:
        temp = elements[a]
        elements[a] = elements[b]
        elements[b] = temp

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]
    
    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
            
        while elements[end] > pivot:
            end -= 1
            
        if start < end:
            swap(start, end, elements)
    
    swap(pivot_index, end, elements)
    
    return end

def quick_sort(elements, start, end):
    if start<end:
        partition_index = partition(elements, start, end)
        quick_sort(elements, start, partition_index-1) 
        quick_sort(elements, partition_index+1, end)


if __name__ == '__main__':
    tests = [
        [11, 9, 29, 7, 2, 15, 28], 
        [3, 7, 9, 11], 
        [25, 22, 21, 10], 
        [29, 15, 28], 
        [], 
        [6]
    ]
    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'Sorted array: {elements}')