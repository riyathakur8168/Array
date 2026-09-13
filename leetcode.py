# nums = [3,2,2,3]
# nums = [0,1,2,2,3,0,4,2]
# val = 3
# i = 0
# k = 0
# for j in range(len(nums)):
#     if nums[i] == val and nums[j]== val:
#         j += 1
#     elif nums[i] == val and nums[j] != val:
#         nums[i], nums[j] = nums[j], nums[i]
#         i += 1
#         j += 1
#         k += 1
#     elif nums[i]!= val and nums[j] == val and i < j:
#         j +=1
#     elif nums[i] != val and nums[j] != val and i < j:
#         i +=1
#         j +=1 
# print(nums)
# for i in range(k):
#     print(nums[i],end=" ")
nums = [0,0,1,1,1,2,2,3,3,4]
i = 0
for j in range(1,len(nums)):
    if nums[i] != nums[j]:
        i += 1
        nums[i] = nums[j]
        # print(nums)
print(nums[:i+1])

 