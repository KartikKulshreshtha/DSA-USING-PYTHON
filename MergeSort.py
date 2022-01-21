# NOTE: THERE ARE TWO STEPS TO SORT THE LIST USING MERGE SORT SO FIRST WE HAVE TO DIVIDE THE GIVEN LIST INTO IT'S SUB LIST UNTIL WE LEFT WITH ONLY ONE ELEMENT


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

if __name__ == '__main__':
    arr = [9,8,7,2]
    
    print(merge_sort(arr))
    # print(a, b)
    