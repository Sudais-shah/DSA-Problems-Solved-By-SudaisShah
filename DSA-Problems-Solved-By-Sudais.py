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



 #                                    Question 6:  Frequency Count:
# Given an array, count the frequency of each element.
# arr = [3, 1, 2, 3, 4, 1, 2, 3, 5, 1, 2, 4, 5, 3]
# frequency = {}
# for i in range(len(arr)):
#     if arr[i] in frequency:
#         frequency[arr[i]] +=1 
#     else : frequency[arr[i]] = 1
# print(frequency)

# Solution 2 Using Nested Loop
# frequency = {}
# for num in arr:
#     if num in frequency:
#         frequency[num] += 1  # If number already exists, increase count
#     else:
#         frequency[num] = 1  # If number appears for the first time, set count to 1
# print(frequency)

#                            Question 7: Remove Duplicates from an Array:
#6.	Return an array with duplicates removed
# solution 1 
# arr = [3, 1, 2, 3, 4, 1, 2, 3, 5, 1, 2, 4, 5, 3]
# unique_arr = []
# for i in range(len(arr)):
#     is_unique = True
#     for j in range(i+1,len(arr)):
#        if arr[i] == arr[j]:
#             is_unique = False
#             break
#     if is_unique:
#         unique_arr.append(arr[i])
# print(unique_arr)

# solution 2
# arr = [3, 1, 2, 3, 4, 1, 2, 3, 5, 1, 2, 4, 5, 3]
# unique_arr = []
# seen = set()
# for i in range(len(arr)):
#     if arr[i] not in seen:
#         unique_arr.append(arr[i])
#         seen.add(arr[i])
# print(unique_arr)

# solution 3 this is slower in comparison with solution 2
# arr = [3, 1, 2, 3, 4, 1, 2, 3, 5, 1, 2, 4, 5, 3]
# unique_arr = []
# for i in range(len(arr)):  
#     if arr[i] not in unique_arr:  
#         unique_arr.append(arr[i])
# print(unique_arr)

#                                       Question 8: Reverse a String:
#  Reverse the characters in a given string.

# str = "Hello World"
# str = str[::-1]
# print(str)

# str = "Hello World"
# reverse = ""
# for i in range(len(str)-1,-1,-1):
#     reverse = reverse + str[i]
# print(reverse)

# text = "Hello World"
# reverse = "".join(reversed(text)) 
# print(reverse)

 #                                                    Question 9: Check Palindrome (String):
# 	Write a function to check if a string is a palindrome
# str = 'malayalam'
# str = 'himalya'

# reverce = ''.join(reversed(str))
# if str == reverce:
#     print("String is palindrome")

# Solution 2 
# rev = ""
# for i in range(len(str) - 1 , - 1 , -1):
#      rev += str[i]
# if str == rev:
#      print("String is palindrome")
# else:
#      print("String is not palindrome")  