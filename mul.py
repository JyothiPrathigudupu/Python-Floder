# 2. Write a Python program to multiply all the items in a list
# Sample Output
# [3,4,5,4,7]

# m=[3,4,5,4,7]
# mul=0
# for i in m:
#     mul*=i
#     print(i)

# 3. Write a Python program to get the largest number from a list
# Sample Output
# [1,7,10,34,2,8]

# a=[1,7,10,34,2,8]
# print(max(a))

# a=[1,7,10,34,2,8]
# """
# print("Largest Number :",max(a))
# """
# max = a[ 0 ]
# for i in a:
# 	if i > max:
# 		max = i
# print("Largest Number :",max)

# 4. Write a Python program to get the smallest number from a list
# Sample Output
# [51,7,10,34,2,8]
# Smallest Number : 2
# a=[51,7,10,34,2,8]
# print(min(a))

# a=[51,7,10,34,2,8]
# min= a[0]
# for i in a:
#     if i<min:
#         min=i
# print(min)

# 5.Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
# Sample Output
# ['abc', 'xyz', 'aba', '1221']
# First and Last Character are same : 2

# a=['abc', 'xyz', 'aba', '1221']
# ch=0
# for w in a:
#     if len(w) > 1 and w[0] == w[-1]:
#         ch+=1
# print(ch)

# 6.Write a Python program to remove duplicates from a list
# Sample Output
# [1,2,3,7,2,1,5,6,4,8,5,4]
# {1,2,3,4,5,6,7,8}

# a=[1,2,3,7,2,1,5,6,4,8,5,4]
# b=set(a)
# print(b)
# dup = set()
# uniq = []
# for x in a:
#     if x not in dup:
#         uniq.append(x)
#         dup.add(x)
# print(dup)

# def remove_duplicates(input_list):
#     # Using a set to remove duplicates
#     return list(set(input_list))

# #.Example usage
# input_list = [1, 2, 3, 4, 4, 5, 1, 2, 6, 7]
# output_list = remove_duplicates(input_list)
# print("Original list:", input_list)
# print("List after removing duplicates:", output_list)
# 7. Write a Python program to clone or copy a list
# Sample Output
# [10, 22, 44, 23, 4]
# Clone or Copy a List : [10, 22, 44, 23, 4]

# a=[10, 22, 44, 23, 4]
# print(a)
# o_l=[10, 22, 44, 23, 4]
# n_l=list(o_l)
# print("old list:",o_l)
# print("new list:",n_l)

#8. Write a Python program to check a list is empty or not
# Sample Output
# [34,45,6,5,4,56,7]
# List is Not Empty

# a=[]
# if not a:
#     print("empty")
# else:
#     print("not empty")

# 8. Write a Python program to clone or copy a list
# Sample Output
# [10, 22, 44, 23, 4]
# Clone or Copy a List : [10, 22, 44, 23, 4]

# a=[10, 22, 44, 23, 4]
# print(a)

# o_l=[10, 22, 44, 23, 4]
# n_l=list(o_l)
# print("old list:",o_l)
# print("new list:",n_l)

# 9.Write a Python program to find the list of words that are longer than n from a given list of words
# Sample Output
# Find the List of Words that are Longer than n from a given List of Words
# Given value of n = 4
# ['Words', 'Longer', 'given', 'Words']

# n=4
# str="Find the List of Words that are Longer than n from a given List of Words"
# t=str.split(" ")
# new_list=[]
# for a in t:
#     if len(a)>4:
#         new_list.append(a)
# print(new_list)


# 10. Write a Program that get two lists as input and check if they have at least one common member

# Sample Output
# [1,2,3,4,5]
# [5,6,7,8,9]
# Lists have at least one common member

# a1=[1,2,3,4,5]
# a2=[5,6,7,8,9]
# result=False
# for x in a1:
#     for y in a2:
#         if x==y:
#             result=True
#             print(result)
# if(result):
#     print("a1 have at least one common member:")
# else:
#     print("a1 not have at least one common member:")

# 11. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. (enumerate)
# Sample Output
# ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
# ['Dog', 'Elephant', 'Fox', 'Ponda']


# a=["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
# del a[5]
# del a[4]
# del a[0]
# print("list after removing the 0th, 4th and 5th elements:",a)

# a = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
# a = [x for (i,x) in enumerate(a) if i not in (0,4,5)]
# print(a)

# 12. Write a Python program to print the numbers of a specified list after removing even numbers from it
# Sample Output
# [7,32,81,20,25,14,23,27]
# [7, 81, 25, 23, 27]


# n = [7,32,81,20,25,14,23,27]
# n = [x for x in n if x%2!=0]
# print(n)

# a=[7,32,81,20,25,14,23,27]
# print("original a:")
# print(a)
# for i in a:
#     if i%2==0:
#         a.remove(i)
#         print("a after removing even numbers:")
#         print(a)

# 13. Write a Python program to shuffle and print a specified list (shuffle)
# Sample Output
# ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
# ['Fox', 'Cat', 'Tiger', 'Lion', 'Dog', 'Ponda', 'Elephant']

# from random import shuffle
# a=["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
# shuffle(a)
# print(a)

# 14. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30
# Sample Output
# First 5 elements : [1, 4, 9, 16, 25]
# Last 5 elements : [625, 676, 729, 784, 841]

# l=list()
# for i in range (1,30):
#     l.append(i**2)
# print(l[:5])
# print(l[-5:])


# 15. Write a Python program to generate all permutations of a list in Python. (itertools)
# Sample Output
# [1,2,3]
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# import itertools
# print(list(itertools.permutations([1,2,3])))

# 16. Write a Python program to convert a list of characters into a string
# Sample Output
# ['T','u','t','o','r',' ','J','o','e','s']
# Tutor Joes

# a=['T','u','t','o','r',' ','J','o','e','s']
# a1=''.join(a)
# print(a1)

# 17. Write a Python program to find the index of an item in a specified list
# Sample Output
# [20, 70, 30, 90, 10, 30, 90, 10, 80]
# Item to find the index of 30
# Index Number of Item = 2

# a=[20, 70, 30, 90, 10, 30, 90, 10, 80]
# item=a.index(30)
# print(item)

# num = [20, 70, 30, 90, 10, 30, 90, 10, 80]
# print(num.index(30))
# 18. Write a Python program to flatten a shallow list
# Sample Output
# [[20,30,70],[30,90,10], [30,20], [70,90,10,80]]
# [20, 30, 70, 30, 90, 10, 30, 20, 70, 90, 10, 80]

# import itertools
# a=[[20,30,70],[30,90,10], [30,20], [70,90,10,80]]
# merged_list = list(itertools.chain(*a))
# print(merged_list)

# 19. Write a Python program to add a list to the second list
# Sample Output
# [10, 20, 30, 40]
# ["Cat", "Dog", "Lion", "Ponda"]
# [10, 20, 30, 40, 'Cat', 'Dog', 'Lion', 'Ponda']

# a1=[10, 20, 30, 40]
# a2=["Cat", "Dog", "Lion", "Ponda"]
# c=a1+a2
# print(c)

# 20. Write a Python program to select an item randomly from a list Using random.choice()
# Sample Output
# ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
# Item randomly from a list : Fox

# import random
# l=["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
# print(random.choice(l))

# Write a python program to check whether two lists are circularly identical
# Sample Output
# [8, 8, 12, 12, 8]
# [8, 8, 8, 12, 12]
# [1, 8, 8, 12, 12]
# Compare List1 and List2 : True
# Compare List1 and List3 : False

# list1=[8, 8, 12, 12, 8]
# list2=[8, 8, 8, 12, 12]
# list3=[1, 8, 8, 12, 12]
# print("Compare List1 and List2 : ",' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
# print("Compare List1 and List3 : ",' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

# def are_circularly_identical(list1, list2):
#     # Check if lengths are equal
#     if len(list1) != len(list2):
#         return False
#     # Concatenate list1 with itself
#     double_list1 = list1 + list1
#     # Check if list2 is a substring of the concatenated list
#     return any(double_list1[i:i+len(list2)] == list2 for i in range(len(list1)))
# # Sample lists
# list1 = [8, 8, 12, 12, 8]
# list2 = [8, 8, 8, 12, 12]
# list3 = [1, 8, 8, 12, 12]
# # Checking if the lists are circularly identical
# print(f"Compare List1 and List2 : {are_circularly_identical(list1, list2)}")
# print(f"Compare List1 and List3 : {are_circularly_identical(list1, list3)}")

# 22. Write a Python program to find the second smallest number in a list
# Sample Output
# [2,4,56,78,4,34,5,8,9]
# Second Smallest Number : 4

# num = [ 2,4,56,78,4,34,5,8,9]
# if (len(num)<2):
#   print(num)
# if ((len(num)==2)  and (num[0] == num[1])):
#   print(num)
# dup_items = set()
# uniq_items = []
# for x in num:
#   if x not in dup_items:
#     uniq_items.append(x)
#     dup_items.add(x)
# uniq_items.sort()    
# print(uniq_items[1])

# 23.Write a Python program to find the second largest number in a list
# Sample Output
# [82,4,56,78,4,34,5,100,9]
# Second Largest Number : 82

# num = [ 82,4,56,78,4,34,5,100,9]
# if (len(num)<2):
#   print(num)
# if ((len(num)==2) and (num[0] == num[1])):
#   print(num)
# dup_items = set()
# uniq_items = []
# for x in num:
#   if x not in dup_items:
#     uniq_items.append(x)
#     dup_items.add(x)
# uniq_items.sort()    
# print(uniq_items[-2])

# 24. Write a Python program to get unique values from a list
# Sample Output
# [82, 4, 10, 56, 78, 4, 34, 5, 10, 9]
# [34, 4, 5, 9, 10, 78, 82, 56]

# l = [ 82,4,10,56,78,4,34,5,10,9]
# print("Original List : ",l)
# s = set(l)
# new_list = list(s)
# print("Unique Numbers : ",new_list)

# 25. Write a Python program to get the frequency of the elements in a list.
# Sample Output
# [10, 30, 50, 10, 20, 60, 20, 60, 40, 40, 50, 50, 30]
# Counter({50: 3, 10: 2, 30: 2, 20: 2, 60: 2, 40: 2})

# import collections
# l = [10,30,50,10,20,60,20,60,40,40,50,50,30]
# print("Original List : ",l)
# f = collections.Counter(l)
# print("Frequency of the Elements: ",f)
# 26.Create a list by concatenating a given list which range goes from 1 to n
# Sample Output
# ['T', 'J']
# N = 10
# ['T1', 'J1', 'T2', 'J2', 'T3', 'J3', 'T4', 'J4', 'T5', 'J5', 'T6', 'J6', 'T7', 'J7', 'T8', 'J8', 'T9', 'J9', 'T10', 'J10']

# ch = ['T', 'J']
# n = 10
# new_list = ['{}{}'.format(a, b) for b in range(1, n+1) for a in ch]
# print(new_list)

# 27. Write a Python program to get variable unique identification number or string
# Sample Output
# x = 30
# s = "Tutor Joes"
# Unique Identification Number : 7005f980
# Unique Identification String : c24bb0

# x = 30
# print(format(id(x), 'x'))
# s = "Tutor Joes"
# print(format(id(s), 'x')) 

# 28. Write a Python program to find common items from two lists
# Sample Output
# [23,45,67,78,89,34]
# [34,89,55,56,39,67]
# Common items from two lists : {89, 34, 67}

# num1 = [23,45,67,78,89,34]
# num2 = [34,89,55,56,39,67]
# print(set(num1) & set(num2))

# 29. Write a Python program to split a list based on first character of word
# Sample Output
# ["cat", "dog", "cow", "tiger", "lion", "Fox", "Shark", "Snake", "turtle", "mouse", "monkey", "bear"]
# F
#      Fox
# S
#      Shark
#      Snake
# b
#      bear
# c
#      cat
#      cow
# d
#      dog
# l
#      lion
# m
#      monkey
#      mouse
# t
#      tiger
#      turtle

# from itertools import groupby
# from operator import itemgetter
# a = ["cat","dog","cow","tiger","lion","Fox","Shark","Snake","turtle","mouse","monkey","bear"]
# for ltr, wds in groupby(sorted(a), key=itemgetter(0)):
# 	print(ltr)
# 	for w in wds:
# 		print(" ",w)
# 	print("")

# 30. Write a Python program to select the odd number of a list
# Sample Output
# [1,2,4,3,6,7,5,8,9,7,8,9,10]
# [1, 3, 7, 5, 9, 7, 9]

# a=[1,2,4,3,6,7,5,8,9,7,8,9,10]
# odd_num=[]
# for i in a:
# 	if(i%2==1):
# 		#print(i)
# 		odd_num.append(i)
# print(odd_num)

# 31. Write a Python Program to count unique values inside a list
# Sample Output
# [10, 20, 30, 50, 80, 70, 70, 80, 10]
# No of Unique Items in List : 6
# first method
# a = [10, 20, 30, 50, 80, 70, 70, 80, 10]
# s = set(a)
# print("No of Unique Items in List :", len(s))

# a = [10, 20, 30, 50, 80, 70, 70, 80, 10]
# l = []
# count = 0
# for i in a:
# 	if i not in l:
# 		count += 1
# 		l.append(i)
# print("No of Unique Items in List :", count)

# 32. Write a Python Program to List product excluding duplicates
# Sample Output
# [2, 1, 2, 4, 6, 4, 3, 2, 1]
# Duplication removal list product : 144

# a = [2,1,2,4,6,4,3,2,1]
# print ("Original list : " + str(a))
# b=list(set(a))
# p=1
# for i in b:
# 	p*=i
# print ("Duplication removal list product : " + str(p))

# 33. Write a Python Program to Extract elements with Frequency greater than K
# Sample Output
# [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]

# a = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
# print("Original list : " + str(a))
# K = 2
# res = []
# for i in a:	
# 	freq = a.count(i)
# 	if freq > K and i not in res:
# 		res.append(i)
# print("The Required Elements : " + str(res))

# 34. Write a Python Program to Test if List contains elements in Range
# Sample Output
# [4, 5, 6, 7, 3, 9]
# Does list contain all elements in range : True

# a = [4, 5, 6, 7, 3, 9]
# print("Original list is : " + str(a))
# i, j = 3, 10
# res = True
# for e in a:
# 	if e < i or e >= j :
# 		res = False
# 		break
# print ("Does list contain all elements in range : " + str(res))

# 35. Write a Python program to check if the list contains three consecutive common numbers in Python
# Sample Output
# [18, 18, 18, 6, 3, 4, 9, 9, 9]
# Three Consecutive common numbers = 18, 9

# a = [18, 18, 18, 6, 3, 4, 9, 9, 9]
# l = len(a)
# for i in range(l - 2):
# 	if a[i] == a[i + 1] and a[i + 1] == a[i + 2]:
# 		print(a[i])

# 36. Write a Python program to find the Strongest Neighbour
# Sample Output
# [10,20,30,20,30,400]
# 20 30 30 30 400

# n = 6
# a1 = [10,20,30,20,30,400]
# a2 = []	
# for i in range(1, n):
#     r = max(a1[i], a1[i-1])
#     a2.append(r)
# for i in a2 :
#     print(i,end=" ")

# 37. Write a Python Program to print all Possible Combinations from the three Digits
# Sample Output
# [1, 2, 3]
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

# a = [1, 2, 3]
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if (i!=j and j!=k and i!=k):
#                 print(a[i], a[j], a[k])	

# 38. Write a Python program to find all the Combinations in the list with the given condition
# Sample Output
# ['Tutor Joes', ['Software', 'Computer'], ['Solution', 'Education']]
# [ ['Tutor Joes', 'Software', 'Solution'], ['Tutor Joes', 'Computer', 'Education'] ]
    
# val = ["Tutor Joes",["Software","Computer"],
# 			["Solution", "Education"]]
# print("Original List : " + str(val))
# a = 2
# l = []
# c = 0
# while c <= a - 1:
# 	t = []
# 	for i in val:
# 		if not isinstance(i, list):
# 			t.append(i)
# 		else:
# 			t.append(i[c])
# 	c += 1
# 	l.append(t)
# print("\nIndex Combinations : " + str(l))

# 39. Write a Python program to get all unique combinations of two Lists

# Sample Output
# ['A','B','C']
# [1,2,3]
# [ [('A', 1), ('B', 2), ('C', 3)], [('A', 1), ('C', 2), ('B', 3)], [('B', 1), ('A', 2), ('C', 3)], [('B', 1), ('C', 2), ('A', 3)], [('C', 1), ('A', 2), ('B', 3)], [('C', 1), ('B', 2), ('A', 3)] ]

# import itertools
# from itertools import permutations
# l1 = ['A','B','C']
# l2 = [1,2,3]
# unique = []
# permut = itertools.permutations(l1, len(l2))
# for comb in permut:
# 	zipped = zip(comb, l2)
# 	unique.append(list(zipped))
# print(unique)

# 40. Write a Python program to remove all the occurrences of an element from a list
# Sample Output
# [1, 3, 4, 6, 5, 1]
# [3, 4, 6, 5]

# val = [1, 3, 4, 6, 5, 1]
# a = 1
# print ("Original list :" ,val)
# c = val.count(a)
# for i in range(c):
#     val.remove(a)
# print ("Remove operation :" , val)

# 41. Write a Python Program to Remove Consecutive K element records
# Sample Output
# [ ('A', 'B', 'C', 'D'), ('B', 'C', 'C', 'I'), ('H', 'D', 'B', 'C'), ('C', 'C', 'G', 'F') ]
# [ ('A', 'B', 'C', 'D'), ('H', 'D', 'B', 'C') ]

# val = [('A', 'B', 'C', 'D'), ('B', 'C', 'C', 'I'), ('H', 'D', 'B', 'C'), ('C', 'C', 'G', 'F')]
# print("Original List : " + str(val))
# K = 'C'
# res = [i for i in val if not any(i[j] == K and i[j + 1] == K for j in range(len(i) - 1))]
# print("After Removal : " , res)

# 42. Write a Python Program to Replace index elements with elements in Other List
# Sample Output
# ['Tutor Joes', 'Computer', 'Education']
# [2, 1, 0, 1, 0, 2, 2, 0, 1, 0, 1, 2]
# ['Education', 'Computer', 'Tutor Joes', 'Computer', 'Tutor Joes', 'Education', 'Education', 'Tutor Joes', 'Computer', 'Tutor Joes', 'Computer', 'Education']

# a = ['Tutor Joes', 'Computer', 'Education']
# b = [2 ,1 ,0 ,1 ,0 ,2 ,2 ,0 ,1 ,0 ,1 ,2]
# print("List 1 : " , a)
# print("List 2 : " , b)
# res = [a[i] for i in b]
# print ("After Index Elements Replacements is : " ,res)

# 43. Write a Python Program to Retain records with N occurrences of K
# Sample Output
# [ (4, 5, 6, 5, 4), (4, 5, 3), (5, 5, 2), (3, 4, 9) ]
# K = 5
# N = 2
# [ (4, 5, 6, 5, 4), (5, 5, 2) ]

# val = [(4, 5, 6, 5, 4), (4, 5, 3), (5, 5, 2), (3, 4, 9)]
# print(val)
# K = 5
# N = 2
# res = [e for e in val if e.count(K) == N]
# print(res)

# 44. Write a Python Program to Swap elements in String list
# Sample Output
# ['Tutor', 'joes', 'Computer', 'Education']
# ['Tutor', "Joe's", 'Software', 'Solutions']

# s = ["Tutor","joes","Computer","Education"]
# print("Before Swap :",s)
# res = [sub.replace("joes","Joe's").replace("Computer", "Software").replace("Education", "Solutions") for sub in s]
# print ("After Swap : ",res)

# 45. Write a Python program to reverse All Strings in String List
# Sample Output
# Original list = ['Tutor', 'joes', 'Computer', 'Education']
# Reversed list = ['rotuT', 'seoj', 'retupmoC', 'noitacudE']
# Reversed list = ['Education', 'Computer', 'joes', 'Tutor']

# val = ["Tutor","joes","Computer","Education"]
# print ("Original list : ", val)
# #First Methods
# res = [i[::-1] for i in val]
# print ("Reversed list : " , res)
# # #Second Methods
# # print("Reversed list : " ,val[::-1])

# 46. Write a Python program to find the character position of Kth word from a list of strings
# Sample Output
# ['Tutor', 'joes', 'Computer', 'Education']
# K = 20
# Index of character at Kth position word : 3

# val = ["Tutor","joes","Computer","Education"]
# print("The original list is : " ,val)
# K = 20
# res = [i[0] for sub in enumerate(val) for i in enumerate(sub[1])]
# res = res[K]
# print("Index of character at Kth position word : " + str(res))

# 47. Write a Python Program to Prefix frequency in string List
# Sample Output
# ['TjC', 'TjCpp', 'TjPython', 'Java']
# Prefix = 'Tj'
# Strings count with matching frequency : 3

# val = ["TjC","TjCpp","TjPython","Java"]
# print("Original List : ",val)
# sub = 'Tj'
# res = 0
# for e in val:
# 	if e.startswith(sub):
# 		res = res + 1
# print ("Strings count with matching frequency : ",res)

# 48. Write a Python Program to Split Strings on Prefix Occurrence
# Sample Output
# ['TjC', 'TjCpp', 'TjPython', 'Java', 'tj']
# Prefix = 'Tj'
# [ ['TjC'], ['TjCpp'], ['TjPython', 'Java', 'tj'] ]

# l = ["TjC","TjCpp","TjPython","Java","tj"]
# print("The original list is : ",l)
# pref = "Tj"
# res = []
# for val in l:
# 	if val.startswith(pref):
# 		res.append([val])
# 	else:
# 		res[-1].append(val)
# print("Prefix Split List : " + str(res))

# 49. Write a Python program to Replace all Characters of a List Except the given character
# Sample Output
# ['P', 'Y', 'T', 'H', 'O', 'N']
# ['@', '@', 'T', '@', '@', '@']

# val = ['P', 'Y', 'T', 'H', 'O', 'N']
# print("The original list : " + str(val))
# res = [i if i == 'T' else '@' for i in val]
# print("List after replacement : " + str(res))

# 50. Write a Python Program to Add Space between Potential Words
# Sample Output
# ['TutorJoes', 'ComputerEducations']
# [' Tutor Joes', ' Computer Educations']

val = ["TutorJoes", "ComputerEducations"]
print("Original list : " ,val)
res = []
for i in val:
	t = [[]]
	for ch in i:
		if ch.isupper():
			t.append([])
		t[-1].append(ch)
	res.append(' '.join(''.join(i) for i in t))
print("The space added list of strings : " , res)








