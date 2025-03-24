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

#                                                       Question 10: First Non-Repeating Character:
#	Identify the first character in a string that doesn’t repeat.
# text = "swiss"
# arr = []
# for i in range(len(text)):
#     if text.count(text[i]) == 1:
#         arr.append(text[i])
#         break
# print(arr)

#   Solution 2 
# text = "swiss"
# for char in text:
#     if text.index(char) == text.rindex(char):  
#         print(char)
#         break

# Solution 3
# text = "swiss"
# char_count = {}

# Step 1: Count occurrences
# for char in text:
#     char_count[char] = char_count.get(char, 0) + 1

# Step 2: Find the first non-repeating character
# text = "swiss"
# for char in text:
#     if char_count[char] == 1:
#         print(char)
#         break

                                                    #    Question 11: Count Vowels in a String:
# 11.	Count the number of vowels in a string.
# str = "Beautiful day outside"
# vowels = 'aeiou' 
# count = 0        
# for i in str.lower():    # convert to lower so both cases are counted
#     if i in vowels:      # if character is a vowel then add 1
#        count = count + 1      
# print('count of vowels:',count)             # print the count of vowels

#Solution 2 
# str = "Beautiful day outside"
# vowels = 'aeiou' 
# count = sum(1 for i in str.lower() if i in vowels) # Solving using list comprehension
# print('count of vowels:',count) 

# solutio 3
# str = "Beautiful day outside"
# vowels = 'aeiou'
# count = len(list(filter(lambda x: x in vowels, str.lower()))) # filter() keeps only vowels, and len() counts them.
# print(count)

 #                                                      Question 12:          Anagram Check:
# Write a function to check if two strings are anagrams.
# str1 = "listen"
# str2 = "silent"
#Soltuion 1 
# if sorted(str1) == sorted(str2): # if sorted version of both strings are equal
#     print("Strings are anagrams.")
# else:
#     print("Strings are not anagrams.")  

# Solution 2
# str1 = "listen"
# str2 = "silent"

# is_anagram = True

# if len(str1) != len(str2): # Check if the lengths are different
#     is_anagram = False

# freq = {}

# for char in str1:  
#     freq[char] = freq.get(char, 0) + 1 # Count characters in str1

# for char in str2:    
#     if char in freq:
#         freq[char] -= 1 # Subtract character counts using str2
#     else:
#         is_anagram = False  # Extra character found in str2

# for value in freq.values():# Ensure all values in freq are zero
#     if value != 0:
#         is_anagram = False
#         break  # No need to check further

# if is_anagram:
#     print("Strings are anagrams.")
# else:    
#     print("Strings are not anagrams.")

#                                **************               Searching & Sorting                    **************

#                                             Question 13:         Linear Search:
#  Implement linear search to find an element in an array.
# arr = [4, 8, 15, 23, 42] 
# target = 15 # lets find 15 
# # Solution 
# for i in range(len(arr)):
#     if arr[i] == target:
#         print('Element found at index:',i)
#         break
# else:    # the else block will run after loop is completed to avoid multiple print statements
#      print("Element not found")
        


#                                             Question 14:  Binary Search:
# /********** Understanding Binary Search **********/
# Binary search is a search algorithm that finds the position of a target value within a sorted array.
# Requires a Sorted Array 
# Unlike linear search, binary search only works on sorted arrays. 
# Instead of checking each element one by one, binary search:
# Starts in the middle of the array.
# If the target is smaller, it searches the left half.
# If the target is greater, it searches the right half.
# Repeats until the element is found or the range becomes empty.
# Efficient – Binary search is much faster than linear search for large arrays.

#	Implement binary search on a sorted array.
# Solution 1
# arr = [4, 8, 15, 23, 42]  # Binary search requires a sorted array
# target = 23
# lowest_number = 0 
# highest_number = len(arr) - 1

# for i in range(low, high + 1):
#     mid = (low + high) // 2
#     if arr[mid] == target:
#         print('Element found at index:',mid)
#         break
#     elif arr[mid] < target:
#         low = mid + 1
#     else:
#         high = mid - 1
# else:
#     print("Element not found")

# Solution 2 
# arr = [4, 8, 15, 23, 42]  # Binary search requires a sorted array
# target = 23
# lowest_number = 0 
# highest_number = len(arr) - 1

# while  lowest_number <= highest_number:
#     mid = (lowest_number + highest_number) // 2
#     if arr[mid] == target:
#         print('Element found at index:',mid)
#         break
#     elif arr[mid] < target:
#         lowest_number = mid + 1 
#     elif arr[mid] > target:
#         highest_number = mid - 1
# else: 
#     print("Element not found")


#                                             Question 15:  Bubble Sort:
# Sort an array using bubble sort.
# What is Bubble Sort?
# Bubble Sort is one of the simplest sorting algorithms that works by repeatedly
# swapping adjacent elements if they are in the wrong order. It’s called “Bubble”
# Sort because large numbers slowly “bubble up” to the end of the array, just like bubbles floating to the surface of water.

arr = [29, 10, 14, 37, 13, 16]
# Solution 1
for i in range(len(arr)-1): # puter loop
# it works without -i as well however it will be more efficient with -i becuase after each iteration the largest number will be at the end
     for j in range(len(arr) - 1 - i): # inner loop
        if arr[j] > arr[j+1]:                   # condition to swap
           arr[j], arr[j+1] = arr[j+1], arr[j]  # swap numbers
print(arr)


#                                             Question 16:   Insertion Sort:
#	Sort an array using insertion sort.

#                                             Question 17:  Selection Sort:
#	Sort an array using selection sort.

#                                             Question 18:  Merge Two Sorted Arrays:
#	Merge two sorted arrays into one sorted array.

#                                             Question 19:  Find Intersection of Two Arrays:
#	Identify common elements between two arrays.

#                                             Question 20:  Find Union of Two Arrays:
# Combine two arrays, removing duplicates.
