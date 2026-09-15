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
# nums = [0,0,1,1,1,2,2,3,3,4]
# i = 0
# for j in range(1,len(nums)):
#     if nums[i] != nums[j]:
#         i += 1
#         nums[i] = nums[j]
#         # print(nums)
# print(nums[:i+1])

<<<<<<< HEAD
# class Solution(object):
#     def threeSum(self, nums):
#         result = set()
#         for i in range(len(nums)):
#             seen = set()
#             for j in range(i+1,len(nums)):
#                 required = -(nums[i] + nums[j])
#                 if required in seen:
#                     result.add(tuple(sorted([nums[i],nums[j],required])))
#                 else:
#                     seen.add(nums[j])
#         return(list(result))
# nums  = [-1,0,1,2,-1,-4]
# obj = Solution()
# print(obj.threeSum(nums))
        
=======

>>>>>>> c64f0260089dcd9d57411837518b448ff02bf04d
 