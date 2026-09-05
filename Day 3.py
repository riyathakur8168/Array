#@ two sum :
# brute approach wth time - o(n^2) & space - o(1)
# arr = [2,7,11,15,5,4]
# target = 9
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] + arr[j] == target:
#             print(i,j)

# hashmap = {}   #using hashmaptc- o(n) and spcae - o(n) 
# for num in arr:
#     required = target - num
#     if required in hashmap:
#         print(hashmap[required],num)
#     else:
#         hashmap[num] = index(edar index likha jayga ya to i)

#@ approach with tc -o(n) & sc - o(1)
# count = 0
# i = 0
# for j in range(1,len(arr)):
#     if arr[i] + arr[j] == target:
#         print(i,j)
#         count  += 1
#         i += 1
#     else:
#         i += 1
# if count == 0:
#     print("pair not exist")

#@ -first unique element 
# arr = [4, 5, 1, 2, 1, 4, 5]
# hash1 = {}
# for num in arr:
#     if num in hash1:
#         hash1[num] += 1
#     else:
#         hash1[num] = 1
# for key , value in hash1.items():
#     if value == 1:
#         print("first unique element: ",key)
#         break

#@ intersection of 2 arrays: 
#-- dono ki compleaxity - tc- o(n^2) and space-o(n)
#-- esse duplicate bhi aayenge to hata nhi payenge
# arr1 = [1, 2, 2, 3, 4]
# arr2 = [2, 2, 4, 6]
# res = []
# for i in range(len(arr1)):
#     for j in range(len(arr2)):
#         if arr1[i] == arr2[j]:
#             res.append(arr1[i])
#         else:
#             continue
# print(res)

#-- agr sirf unique intersected eleemnts chiye hai to 
# arr1 = [1, 2, 2, 3, 4]
# arr2 = [2, 2, 4, 6]
# res = []
# for i in range(len(arr1)):
#     for j in range(len(arr2)):
#         if arr1[i] == arr2[j]:
#             if arr1[i] not in res:
#                 res.append(arr1[i])
# print(res)

#@ - longest consecutive subsequence 
arr = [100, 4, 200, 1, 3, 2]
count = 0
nums = set(arr)
longest = 0
for num in nums:
    if num-1 not in nums:
        count = 1
        current = num
        while current + 1 in nums:
            current += 1
            count += 1
        longest = max(longest,count)
print(longest) 
