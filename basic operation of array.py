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

#


