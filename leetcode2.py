# class Solution(object):
#     def searchInsert(self, nums, target):
# nums = [1,2,4,6,7,9]
# target = 6
# left = 0
# right = len(nums)-1
# # mid = (left+right)/2
# while left <= right:
#     mid = (left+right)//2
#     if nums[mid] == target:
#         print(mid)
#         break
#     elif nums[mid] < target:
#         left = mid +1
#     else:
#         right = mid -1
# else:
#     print(-1)

# nums = [1,2,4,6,7,9]
# target = 6
# obj = Solution()
# print(obj.searchInsert(nums,target))