# WORKING
#                                       DSA Question 1:  Reverse an Array
# Task: Write a function that takes an array of numbers as input and returns the reversed array.
# def reverse_array(arr , solution_method):
#     if solution_method == 1:
#         arr.reverse()
#         return arr
#     else : return arr[::-1]
      
# arr1 = [3, 1, 4, 1, 5, 9, 2]
# arr2 = [3, 1, 4, 1, 5, 9, 2]

# print(f"Solution 1:{reverse_array(arr1,1)}")
# print(f"Solution 2:{reverse_array(arr2,2)}")

#                                         DSA Question 2: Find Maximum & Minimum:
# Find the largest and smallest elements in an array.
# arr = [3, 1, 4, 1, 5, 9, 2]
# print(f"maximum number in array is:{max(arr1)}")
# print(f"minimum number in array is:{min(arr1)}")
# max_number = arr[0]
# min_number = arr[0]
# for i in arr:
#     if i > max_number:
#         max_number = i
#     if i < min_number: min_number = i

# print(f"maximum number in array is:{max_number}")
# print(f"minimum number in array is:{min_number}")

#                                         DSA Question 3:  Sum of Array Elements:
#  Calculate the sum of all numbers in an array.
# arr = [3, 1, 4, 1, 5, 9, 2]
# Solution 1
# print(f"Sum of an array elements is:{sum(arr1)}")

# Solution 2
# sum = 0
# for i in range(len(arr1)):
#     sum = sum+arr[i]
# print("Sum of an array elements is:",sum)   

#                                         DSA Question 4: Check if Array is Sorted:
# 	Determine whether an array is sorted in ascending order.           
# arr = [1, 2, 4, 1, 5, 9, 2]
# arr1 = [1,2,3]

# for i in range(len(arr1)-1):
#        if arr1[i] > arr1[i+1]:
#             print("Array is not sorted")
#             break
#        else : 
#              print("Array is sorted")
#              break
       
# print("---Below solution is for unsorted array---")
# for i in range(len(arr)-1):
#         if arr[i] > arr[i+1]:
#             print("Array is not sorted.Becuase:",arr[i] , ">", arr[i+1])
#             break       
              
 
 #                          Question 5:Find Second Largest Element:
 #Locate the second largest number in an array.
# arr = [1, 2, 4, 1, 5, 9, 2, 6, 7]
# sorted_array = sorted(arr)
# print(f"Second largest number in array is:{sorted_array[-2]}")
# #                  OR
# print("Second largest number in array is:",sorted_array[len(sorted_array)-2])
# #                  oR
# largest = second_largest = float('-inf')  
# for i in arr:
#      if i > largest:
#           second_largest = largest
#           largest = i   
#      elif i > second_largest and i != largest:
#           second_largest = i 

# print(f"Second largest number in array is:{second_largest}")



 #                                    Question 5:  Frequency Count:
# Given an array, count the frequency of each element.
arr = [3, 1, 2, 3, 4, 1, 2, 3, 5, 1, 2, 4, 5, 3]
# frequency = {}
# for i in range(len(arr)):
#     if arr[i] in frequency:
#         frequency[arr[i]] +=1 
#     else : frequency[arr[i]] = 1
# print(frequency)

# Solution 2 

frequency = {}
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            frequency[arr[i]] +=1
        else : frequency == 1 
print(frequency)

