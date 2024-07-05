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

# Write a Python program to remove duplicates from a list
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

# Write a Python program to check a list is empty or not
# Sample Output
# [34,45,6,5,4,56,7]
# List is Not Empty








