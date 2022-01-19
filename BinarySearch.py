# from decorator import time_it

# @time_it
# def binary_search(number_list, number_to_find):
#     number_list.sort()
#     left_index = 0
#     right_index = len(number_list) - 1
#     mid_index = 0
    
    
#     while left_index <= right_index:
#         mid_index = (left_index + right_index) // 2
#         mid_number = number_list[mid_index]
        
#         print(mid_number)
#         if mid_number == number_to_find:
#             return mid_index
        
#         if mid_number < number_to_find:
#             left_index = mid_index + 1
            
#         else:
#             right_index = mid_index - 1
            
#     return -1

# @time_it
# def linear_search(number_list, number_to_find):
#     for index, element in enumerate(number_list):
#         if element == number_to_find:
#             return index
#     return -1

# # @time_it
# # def binary_search_recursive(number_list, number_to_find, left_index, right_index):
# #     if right_index < left_index:
# #         return -1
# #     mid_index = (left_index + right_index) // 2
# #     mid_number = number_list[mid_index]
# #     if mid_number == number_to_find:
# #             return mid_index
        
# #     if mid_number < number_to_find:
# #         left_index = mid_index + 1
        
# #     else:
# #         right_index = mid_index - 1
        
# #     return binary_search_recursive(number_list, number_to_find, left_index, right_index)
    


# if __name__ == '__main__':
#     number_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
#     number_list.sort()
#     number_to_find = 15
#     # left_index = 0
#     # right_index = len(number_list)
    
#     index = binary_search(number_list, number_to_find)    
#     index = linear_search(number_list, number_to_find)    
#     print(f"Number found at {index} using linear search")
#     print(f"Number found at {index} using binary search")
    
#     # index = binary_search_recursive(number_list, number_to_find, left_index, right_index)
#     # print(f"Number found at {index} using binary search in recursive")


def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find: # this means number is in right hand side of the list
            left_index = mid_index + 1
        else: # number to find is on left hand side of the list
            right_index = mid_index - 1

    return -1

def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)


if __name__ == '__main__':
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15
    indices = find_all_occurances(numbers, number_to_find)
    print(f"Indices of occurances of {number_to_find} are {indices}")