# arr = [10,20,30,40,50]  # traversal 
# for i in range(len(arr)):
#     print(arr[i])

# tar = 30 
# for i in range(len(arr)):   # updation first find index then insert at that index
#     if arr[i] == tar:
#         arr[i] = 100
# print(arr)
#@ find the index of the target element and then shift the elements
#@ and then inset and edge case if target not available handle it

# arr = [10,20,30,40,50]
# tar = 100
# value = 25
# index = -1
# # find index of target
# for i in range(len(arr)):
#     if arr[i] == tar:
#         index = i
#         break

# if index != -1:
#     arr.append(None) # create extra slot for shifting 
#     for i in range(len(arr)-1,index,-1):# shift elements on right side
#         arr[i] = arr[i-1]
# # insert 
#     arr[index] = value
#     print(arr)
# else:
#     print("Target not found")

# arr = [7, 2, 9, 4, 1, 6]
# maxi = arr[0]
# for i in range(len(arr)):
#     if arr[i] >= maxi:
#         maxi = arr[i]
# print(maxi)

# mini = arr[0]
# for i in range(len(arr)):
#     if arr[i] <= mini:
#         mini = arr[i]
# print(mini)

#@ second largest element in the array
# arr = [5, 2, 9, 4, 1, 6]
# # arr = [9,7,8]
# # # arr = [-5, -2, -8, -1]
# maxi = arr[0]
# secondmaxi = float('-inf')
# for i in range(len(arr)):
#     if arr[i] > maxi:
#         secondmaxi = maxi
#         maxi = arr[i]
#     # deals agr arr[i] maxi se bda ho but second se chota ho tb
#     elif arr[i] > secondmaxi and arr[i] != maxi:
#         secondmaxi = arr[i]
# print(maxi)
# print(secondmaxi)

#@ frequency of an element
# arr = [2, 5, 2, 8, 2, 5, 9]
# target = 2
# count = 0
# for i in range(len(arr)):
#     if arr[i] == target:
#         count += 1
# print(count,"times occur",target)

#@ remove duplicates from sorted array : tc- o(n) and space - o(1)
# Logic:
# i = 0 → unique elements ki position
# j = 1 → array ko scan karta hai

# j har iteration mein automatically aage badhta hai, while i sirf new unique element milne par badhta hai.

# IF arr[i] != arr[j]:
#     → new unique element mila
#     → i += 1
#     → arr[i] = arr[j]
# arr[i] = arr[j] ka meaning:

# j jis new element ko find karta hai, usko i ki next position par copy/place kar dete hain.

# Agar same element ho:
# arr[i] == arr[j]

# → duplicate hai
# → kuch nahi karna
# → i wahi rahega, j next element par chala jayega.

# arr = [1, 2, 2, 3, 4, 4, 5]
# i = 0
# for j in range(1,len(arr)):
#     if arr[i]!= arr[j]:
#         i+= 1
#         arr[i] = arr[j]
# print(arr)
# print(arr[:i+1])  # only unique elements

#@ reverse an array : tc - o(n) and space - o(1)
# left → beginning
# right → ending

# jab tak left < right:
#     left aur right ke elements swap karo
#     left++
#     right--
# arr = [1,2,3,4,5]
# left = 0
# right = len(arr) -1
# while left < right:
#     arr[left],arr[right] = arr[right],arr[left]
#     left += 1
#     right -= 1
# print(arr)

#@ chjeck if array is sorted : tc- o(n) and space-o(1)
# arr = [1,2,2,3,4,5]
# # arr = [1,3,2,4]
# i = 0
# for j in range(1,len(arr)):
#     if arr[i] <= arr[j]:
#         i+=1
#     else:
#         break
# if i == len(arr)-1:
#     print("sorted")
# else:
#     print("not sorted")

#@ freuency of each element in the array 
# arr = [1, 2, 2, 3, 3, 3, 4]
# freq = {}
# for num in arr:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
# print(freq)
# for key,value in freq.items():
#     print(key,"-->",value)

#@ seond smallest eleemnt : tc - o(n), space - o(1)
# arr = [7, 2, 9, 4, 1, 6]
# arr = [2,2,2,2]
# arr = [1, 1, 2, 3]
# small = float("inf")
# secondsmall = float("inf")
# for i in range(len(arr)):
#     if arr[i] < small:
#         secondsmall = small
#         small = arr[i]
#     elif arr[i] < secondsmall and arr[i] != small:
#         secondsmall = arr[i]
# if secondsmall == float("-inf"):
#     print("no second smallest element exist & and smallest element = ",small)
# else:
#     print("smallest element :",small,"&","secondsmallest element: ",secondsmall)

#@ check if array is palindrome
# arr = [1, 2, 3, 2, 1] 
# arr = [1, 2, 3, 4]  
# left = 0      #@ two pinter apprioacxh with tc - o(n)
# right = len(arr)-1    #@ space - o(1)
# while left<right:
#     if arr[left] != arr[right]:
#         print("not palindrome")
#         break
#     left +=1
#     right -=1
# else:
#     print("palindrome")   
# result = []    #@ using reverse - tc - o(n) & space- o(1)
# for i in range(len(arr)-1,-1,-1):
#     result.append(arr[i])
# # print(result)
# if arr == result:
#     print("palindrome")
# else:
#     print("not palindrome")

#@ missing numberr using hashmap - tc - o(n) & sc- o(n)
arr = [1, 2, 4, 5]
# freq = {}
# n = len(arr)+1
# for num in range(1,n+1):
#     freq[num] = 0
# for num in arr:
#     freq[num] += 1
# for key,value in freq.items():
#     if value == 0:
#         print("missing number: ",key)

# REDUCE PACE COMPLEXITY - O(N) TO O(1) & tc - o(n)
# n = len(arr) + 1
# expected = (n * (n+1)// 2)
# actual = 0
# for num in arr:
#     actual += num
# missing = expected - actual
# print("Missing number :", missing)




