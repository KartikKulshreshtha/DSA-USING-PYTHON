from decorator import time_it

@time_it
def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break
        
@time_it      
def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i-1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor
        
@time_it    
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    print(left)
    print(right)
    
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    print(left)
    print(right)
    
    return merge_two_sorted_array(left, right)



def merge_two_sorted_array(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
            
            
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1
        
    return sorted_list



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

@time_it 
def quick_sort(elements, start, end):
    if start<end:
        partition_index = partition(elements, start, end)
        quick_sort(elements, start, partition_index-1) 
        quick_sort(elements, partition_index+1, end)
        
        
        

if __name__ == '__main__':
    test = [11, 9, 29, 7, 2, 15, 28]
    
    bubble_sort(test)
    insertion_sort(test)
    merge_sort(test)
    quick_sort(test, 0, len(test)-1)
    